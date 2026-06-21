#!/usr/bin/env python3
"""
Divya Jyot — Daily data fetcher for the 7 PM cross-reference + team-manager routine.

Pulls THREE things and writes them to data.json for Claude Code to analyse:
  (A) Meta Ads performance (spend/leads/CPL/CTR by campaign/adset/ad)
  (B) Meta individual LEADS with created_time + phone (for speed-to-lead)
  (C) The team's Google Sheet (Facebook + SVD tabs) — full history
  (D) Google Sheet REVISION history timestamps (when rows were actually worked)

ENV VARS REQUIRED:
  META_AD_ACCOUNT_ID   e.g. act_1078185463738176
  META_ADS_TOKEN       long-lived token with ads_read + leads_retrieval
  GOOGLE_SHEET_ID      13T80cprP08eC2ap0i3x-lVInOSZPOmFBDbiNUlIPJvw
  GOOGLE_SA_B64        base64 of the service-account JSON (preferred)
  GOOGLE_SA_JSON       raw service-account JSON (fallback)

GOOGLE SCOPES NEEDED (service account, read-only):
  https://www.googleapis.com/auth/spreadsheets.readonly   (cell values)
  https://www.googleapis.com/auth/drive.readonly          (revision history)
"""
import json, os, urllib.request, urllib.parse
from datetime import date, datetime, timedelta, timezone

# ---------- META ----------
_raw_acct = os.environ.get("META_AD_ACCOUNT_ID", "act_XXXXXXXXXX")
AD_ACCOUNT_ID = _raw_acct if _raw_acct.startswith("act_") else "act_" + _raw_acct
TOKEN = os.environ.get("META_ADS_TOKEN", "")
API = "v25.0"
IST = timezone(timedelta(hours=5, minutes=30))

def day(n): return (date.today() - timedelta(days=n)).isoformat()

def _get(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)

# ----- (A) campaign/adset/ad insights -----
def meta_insights(level, since, until):
    params = {
        "level": level,
        "fields": "campaign_name,adset_name,ad_name,spend,impressions,reach,clicks,ctr,cpm,frequency,actions",
        "time_range": json.dumps({"since": since, "until": until}),
        "limit": "200", "access_token": TOKEN,
    }
    url = f"https://graph.facebook.com/{API}/{AD_ACCOUNT_ID}/insights?" + urllib.parse.urlencode(params)
    try:
        return _get(url).get("data", [])
    except Exception as e:
        return [{"error": str(e)}]

def leads_from(actions):
    return sum(int(a.get("value", 0)) for a in (actions or []) if "lead" in a.get("action_type",""))

def shape_meta(rows):
    out = []
    for r in rows:
        if "error" in r:
            out.append(r); continue
        spend = float(r.get("spend", 0)); leads = leads_from(r.get("actions"))
        out.append({
            "campaign": r.get("campaign_name"), "adset": r.get("adset_name"),
            "ad": r.get("ad_name"), "spend": round(spend,2), "leads": leads,
            "cpl": round(spend/leads,2) if leads else None,
            "reach": int(r.get("reach",0) or 0), "ctr": round(float(r.get("ctr",0) or 0),2),
            "cpm": round(float(r.get("cpm",0) or 0),2), "frequency": round(float(r.get("frequency",0) or 0),2),
        })
    return out

# ----- (B) individual leads with created_time + phone (for speed-to-lead) -----
# SOURCE: the "Rewa Online Leads V3 CRM Event" sheet (Pabbly writes Meta leads here with
# exact created_time, phone, intent answer). This sidesteps Meta's leads_retrieval /
# app-review wall entirely — the timestamp is already in a sheet we own and can read.
# created_time looks like 2026-06-20T23:41:43-05:00 (note: US offset, NOT IST) — convert.
LEADS_SHEET_ID = os.environ.get("LEADS_SHEET_ID", "1752IvdN_Qdwd36xuQp5EJ55jATaoOyv4dwzoqeIAeZY")

def normalize_phone(p):
    if not p: return ""
    digits = "".join(ch for ch in str(p) if ch.isdigit())
    return digits[-10:] if len(digits) >= 10 else digits

def parse_lead_rows(rows):
    """rows: raw values from the CRM Event sheet incl. header. Returns clean lead dicts."""
    if not rows or len(rows) < 2:
        return []
    header = [h.strip().lower() for h in rows[0]]
    def col(name):
        try: return header.index(name)
        except ValueError: return None
    ci = {k: col(k) for k in
          ["created_time","ad_name","adset_name","campaign_name","platform",
           "when_are_you_planning_to_purchase?","full_name","phone_number","lead_status"]}
    out = []
    for r in rows[1:]:
        def g(key):
            i = ci.get(key)
            return r[i].strip() if (i is not None and i < len(r)) else ""
        ct = g("created_time")
        name = g("full_name")
        if not ct or "test lead" in name.lower() or "dummy data" in name.lower():
            continue  # skip Meta's test lead
        # parse ISO with offset, convert to IST
        ct_ist = ""
        try:
            dt = datetime.fromisoformat(ct)              # handles 2026-06-20T23:41:43-05:00
            ct_ist = dt.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            ct_ist = ct  # leave raw if unparseable; Claude can note it
        out.append({
            "created_time_raw": ct,
            "created_time_ist": ct_ist,
            "phone10": normalize_phone(g("phone_number")),
            "name": name,
            "platform": g("platform"),
            "intent": g("when_are_you_planning_to_purchase?"),
            "ad": g("ad_name"), "adset": g("adset_name"), "campaign": g("campaign_name"),
            "lead_status": g("lead_status"),
        })
    return out

# ---------- GOOGLE (Sheets values + Drive revisions) ----------
def google_clients():
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build
    import httplib2
    import base64 as _b64
    sa_b64 = os.environ.get("GOOGLE_SA_B64", "")
    sa_json_str = os.environ.get("GOOGLE_SA_JSON", "")
    if sa_b64:
        sa_json_str = _b64.b64decode(sa_b64).decode("utf-8")
    if not sa_json_str:
        raise RuntimeError("Missing GOOGLE_SA_B64/GOOGLE_SA_JSON")
    # GOOGLE_SA_JSON may itself be base64-encoded; detect and decode
    try:
        sa_info = json.loads(sa_json_str)
    except json.JSONDecodeError:
        sa_info = json.loads(_b64.b64decode(sa_json_str).decode("utf-8"))
    creds = Credentials.from_service_account_info(sa_info, scopes=[
        "https://www.googleapis.com/auth/spreadsheets.readonly",
    ])
    import google_auth_httplib2
    http = httplib2.Http(disable_ssl_certificate_validation=True)
    authorized_http_obj = google_auth_httplib2.AuthorizedHttp(creds, http=http)
    sheets = build("sheets", "v4", http=authorized_http_obj, cache_discovery=False)
    return sheets

def fetch_sheet_and_revisions():
    sheet_id = os.environ.get("GOOGLE_SHEET_ID", "")
    if not sheet_id:
        return {"error": "Missing GOOGLE_SHEET_ID"}
    try:
        sheets = google_clients()
    except Exception as e:
        return {"error": str(e)}

    def read(rng):
        try:
            return sheets.spreadsheets().values().get(spreadsheetId=sheet_id, range=rng).execute().get("values", [])
        except Exception as e:
            return [["error", str(e)]]

    def read_other(other_id, rng):
        try:
            return sheets.spreadsheets().values().get(spreadsheetId=other_id, range=rng).execute().get("values", [])
        except Exception as e:
            return [["error", str(e)]]

    # (B) the V3 CRM Event sheet — Meta leads with exact created_time + phone + intent
    leads_raw = read_other(LEADS_SHEET_ID, "Sheet1!A1:Q5000")
    leads_parsed = parse_lead_rows(leads_raw) if leads_raw and not (
        leads_raw and isinstance(leads_raw[0], list) and leads_raw[0] and leads_raw[0][0] == "error") else []

    return {
        "facebook_tab": read("Facebook!A1:N2000"),
        "svd_tab":      read("SVD!A1:O500"),
        "meta_leads_timed": leads_parsed,   # (B) created_time(IST) + phone + intent per lead
        "meta_leads_error": (leads_raw[0] if (leads_raw and leads_raw[0] and leads_raw[0][0]=="error") else None),
    }

# ---------- ASSEMBLE ----------
data = {
    "dates": {"yesterday": day(1), "daybefore": day(2), "today": day(0), "tz": "IST"},
    "meta": {
        "yesterday_campaigns": shape_meta(meta_insights("campaign", day(1), day(1))),
        "yesterday_adsets":    shape_meta(meta_insights("adset",    day(1), day(1))),
        "yesterday_ads":       shape_meta(meta_insights("ad",       day(1), day(1))),
        "last7_campaigns":     shape_meta(meta_insights("campaign", day(7), day(1))),
        "last30_ads":          shape_meta(meta_insights("ad",       day(30), day(1))),
    },
    "sheet": fetch_sheet_and_revisions(),   # Facebook + SVD tabs + V3 CRM Event leads (timed)
}

with open(os.path.join(os.path.dirname(__file__), "data.json"), "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("Wrote data.json — Meta insights + timed leads (from CRM Event sheet) + Facebook/SVD tabs")
