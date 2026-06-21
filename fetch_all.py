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
AD_ACCOUNT_ID = os.environ.get("META_AD_ACCOUNT_ID", "act_XXXXXXXXXX")
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
def normalize_phone(p):
    if not p: return ""
    digits = "".join(ch for ch in str(p) if ch.isdigit())
    return digits[-10:] if len(digits) >= 10 else digits

def fetch_recent_leads(days_back=2):
    """
    Walk the account's lead-gen forms and pull leads created in the last N days,
    capturing created_time (to the second) and phone number for matching.
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    out, errors = [], []
    try:
        # 1) find the ad account's lead forms
        forms_url = (f"https://graph.facebook.com/{API}/{AD_ACCOUNT_ID}/leadgen_forms"
                     f"?fields=id,name&limit=100&access_token={urllib.parse.quote(TOKEN)}")
        forms = _get(forms_url).get("data", [])
    except Exception as e:
        return {"error_forms": str(e), "leads": []}

    for f in forms:
        fid = f.get("id")
        after = None
        for _ in range(10):  # paginate, cap pages
            q = (f"https://graph.facebook.com/{API}/{fid}/leads"
                 f"?fields=created_time,field_data&limit=100&access_token={urllib.parse.quote(TOKEN)}")
            if after:
                q += f"&after={after}"
            try:
                resp = _get(q)
            except Exception as e:
                errors.append(f"form {fid}: {e}"); break
            stop = False
            for lead in resp.get("data", []):
                ct = lead.get("created_time")  # e.g. 2026-06-20T13:45:07+0000
                try:
                    ct_dt = datetime.strptime(ct, "%Y-%m-%dT%H:%M:%S%z")
                except Exception:
                    continue
                if ct_dt < cutoff:
                    stop = True; break  # leads come newest-first; older than window -> stop
                phone, name = "", ""
                for fld in lead.get("field_data", []):
                    n = (fld.get("name") or "").lower()
                    val = (fld.get("values") or [""])[0]
                    if "phone" in n or "mobile" in n: phone = val
                    if n in ("full_name","name","first_name"): name = val or name
                out.append({
                    "created_time_utc": ct,
                    "created_time_ist": ct_dt.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S"),
                    "phone10": normalize_phone(phone),
                    "name": name,
                    "form": f.get("name"),
                })
            if stop: break
            after = resp.get("paging", {}).get("cursors", {}).get("after")
            if not after: break
    return {"leads": out, "errors": errors}

# ---------- GOOGLE (Sheets values + Drive revisions) ----------
def google_clients():
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build
    sa_b64 = os.environ.get("GOOGLE_SA_B64", "")
    sa_json_str = os.environ.get("GOOGLE_SA_JSON", "")
    if sa_b64:
        import base64
        sa_json_str = base64.b64decode(sa_b64).decode("utf-8")
    if not sa_json_str:
        raise RuntimeError("Missing GOOGLE_SA_B64/GOOGLE_SA_JSON")
    sa_info = json.loads(sa_json_str)
    creds = Credentials.from_service_account_info(sa_info, scopes=[
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly",
    ])
    sheets = build("sheets", "v4", credentials=creds)
    drive  = build("drive", "v3", credentials=creds)
    return sheets, drive

def fetch_sheet_and_revisions():
    sheet_id = os.environ.get("GOOGLE_SHEET_ID", "")
    if not sheet_id:
        return {"error": "Missing GOOGLE_SHEET_ID"}
    try:
        sheets, drive = google_clients()
    except Exception as e:
        return {"error": str(e)}

    def read(rng):
        try:
            return sheets.spreadsheets().values().get(spreadsheetId=sheet_id, range=rng).execute().get("values", [])
        except Exception as e:
            return [["error", str(e)]]

    # (D) revision history timestamps. Drive returns coarse revisions (batched edits),
    # each with a modifiedTime. We expose the list so Claude can bound when rows were worked.
    revisions = []
    try:
        page = None
        for _ in range(10):
            kwargs = {"fileId": sheet_id, "fields": "revisions(id,modifiedTime),nextPageToken", "pageSize": 1000}
            if page: kwargs["pageToken"] = page
            resp = drive.revisions().list(**kwargs).execute()
            for rev in resp.get("revisions", []):
                revisions.append({"id": rev.get("id"), "modifiedTime": rev.get("modifiedTime")})
            page = resp.get("nextPageToken")
            if not page: break
    except Exception as e:
        revisions = [{"error": str(e)}]

    return {
        "facebook_tab": read("Facebook!A1:N2000"),
        "svd_tab":      read("SVD!A1:O500"),
        "revisions":    revisions,   # list of {id, modifiedTime} — coarse edit timeline
        "revisions_note": ("Google batches edits into revisions; each modifiedTime marks "
                           "when a batch of edits was saved, not each keystroke. Use to bound "
                           "first-contact timing to within a few minutes, not to the exact second."),
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
    "meta_leads": fetch_recent_leads(days_back=2),   # (B) created_time + phone for speed-to-lead
    "sheet": fetch_sheet_and_revisions(),             # (C)+(D) values + revision timeline
}

with open(os.path.join(os.path.dirname(__file__), "data.json"), "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("Wrote data.json — Meta insights + Meta leads + Sheet + revisions")
