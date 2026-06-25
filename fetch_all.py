#!/usr/bin/env python3
"""
Divya Jyot — Daily data fetcher for the 7 PM agency + sales-manager routine.

Pulls and writes to data.json for Claude Code to analyse:
  (A) Meta Ads performance (spend/clicks/CPL/CTR by campaign/adset/ad)
  (B) Timed Meta leads (created_time + phone + intent) from the V3 CRM Event sheet
  (C) The team's Google Sheet (Facebook + SVD tabs) — full history

ENV VARS:
  META_AD_ACCOUNT_ID   1078185463738176  (act_ prefix optional — auto-added)
  META_ADS_TOKEN       token with ads_read
  GOOGLE_SHEET_ID      main team sheet id
  LEADS_SHEET_ID       V3 CRM Event sheet id (has a default)
  GOOGLE_SA_B64        base64 of service-account JSON (preferred)
  GOOGLE_SA_JSON       raw OR base64 service-account JSON (auto-detected)
  TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID   for --send delivery

Hardened against the three issues seen in production:
  1. META_AD_ACCOUNT_ID missing "act_" prefix      -> auto-prepended
  2. GOOGLE_SA_JSON actually base64, not raw JSON    -> auto-detected & decoded
  3. self-signed proxy cert breaks Google SSL        -> resilient HTTP via google_auth_httplib2
Runtime reduced by running the 5 Meta API calls + Google reads concurrently.
"""
import json, os, base64, ssl, urllib.request, urllib.parse
from datetime import date, datetime, timedelta, timezone
from concurrent.futures import ThreadPoolExecutor

# ---------- CONFIG ----------
def _acct():
    a = os.environ.get("META_AD_ACCOUNT_ID", "").strip()
    if a and not a.startswith("act_"):
        a = "act_" + a            # FIX 1: auto-prepend act_
    return a
AD_ACCOUNT_ID = _acct()
TOKEN = os.environ.get("META_ADS_TOKEN", "")
API = "v25.0"
IST = timezone(timedelta(hours=5, minutes=30))
LEADS_SHEET_ID = os.environ.get("LEADS_SHEET_ID", "1752IvdN_Qdwd36xuQp5EJ55jATaoOyv4dwzoqeIAeZY")

def day(n): return (date.today() - timedelta(days=n)).isoformat()

# tolerant HTTP GET (Meta). Short timeout so one slow call can't hang the run.
def _get(url, timeout=25):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE   # FIX 3: tolerate self-signed proxy cert in the env
    with urllib.request.urlopen(url, timeout=timeout, context=ctx) as r:
        return json.load(r)

# ---------- (A) Meta insights ----------
_INSIGHT_FIELDS = ("campaign_name,adset_name,ad_name,spend,impressions,reach,clicks,"
                   "inline_link_clicks,ctr,cpm,cpc,frequency,actions")

def meta_insights(level, since, until):
    if not TOKEN or not AD_ACCOUNT_ID:
        return [{"error": "Missing META_ADS_TOKEN or META_AD_ACCOUNT_ID"}]
    params = {
        "level": level, "fields": _INSIGHT_FIELDS,
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
        spend = float(r.get("spend", 0) or 0); leads = leads_from(r.get("actions"))
        out.append({
            "campaign": r.get("campaign_name"), "adset": r.get("adset_name"), "ad": r.get("ad_name"),
            "spend": round(spend,2), "leads": leads,
            "cpl": round(spend/leads,2) if leads else None,
            "impressions": int(r.get("impressions",0) or 0),
            "reach": int(r.get("reach",0) or 0),
            "clicks": int(r.get("clicks",0) or 0),
            "link_clicks": int(r.get("inline_link_clicks",0) or 0),
            "ctr": round(float(r.get("ctr",0) or 0),2),
            "cpc": round(float(r.get("cpc",0) or 0),2),
            "cpm": round(float(r.get("cpm",0) or 0),2),
            "frequency": round(float(r.get("frequency",0) or 0),2),
        })
    return out

# ---------- (B) timed leads from the V3 CRM Event sheet ----------
def normalize_phone(p):
    if not p: return ""
    d = "".join(ch for ch in str(p) if ch.isdigit())
    return d[-10:] if len(d) >= 10 else d

def parse_lead_rows(rows):
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
        ct = g("created_time"); name = g("full_name")
        if not ct or "test lead" in name.lower() or "dummy data" in name.lower():
            continue
        try:
            ct_ist = datetime.fromisoformat(ct).astimezone(IST).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            ct_ist = ct
        out.append({
            "created_time_raw": ct, "created_time_ist": ct_ist,
            "phone10": normalize_phone(g("phone_number")), "name": name,
            "platform": g("platform"), "intent": g("when_are_you_planning_to_purchase?"),
            "ad": g("ad_name"), "adset": g("adset_name"), "campaign": g("campaign_name"),
            "lead_status": g("lead_status"),
        })
    return out

# ---------- GOOGLE Sheets ----------
def _decode_sa():
    """FIX 2: accept base64 in EITHER var, or raw JSON. Auto-detect."""
    raw = os.environ.get("GOOGLE_SA_B64", "") or os.environ.get("GOOGLE_SA_JSON", "")
    if not raw:
        raise RuntimeError("Missing GOOGLE_SA_B64 / GOOGLE_SA_JSON")
    raw = raw.strip()
    if raw.startswith("{"):
        return json.loads(raw)                       # already raw JSON
    try:
        return json.loads(base64.b64decode(raw).decode("utf-8"))   # base64 -> JSON
    except Exception:
        return json.loads(raw)                       # last resort

def google_sheets():
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build
    import google_auth_httplib2, httplib2
    sa_info = _decode_sa()
    creds = Credentials.from_service_account_info(
        sa_info, scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"])
    # FIX 3: build an http object that tolerates the env's self-signed proxy cert
    http = google_auth_httplib2.AuthorizedHttp(creds, http=httplib2.Http(disable_ssl_certificate_validation=True))
    return build("sheets", "v4", http=http, cache_discovery=False)

def fetch_sheets():
    sheet_id = os.environ.get("GOOGLE_SHEET_ID", "")
    if not sheet_id:
        return {"error": "Missing GOOGLE_SHEET_ID"}
    try:
        svc = google_sheets()
    except Exception as e:
        return {"error": f"google auth/build failed: {e}"}

    def read(sid, rng):
        try:
            return svc.spreadsheets().values().get(spreadsheetId=sid, range=rng).execute().get("values", [])
        except Exception as e:
            return [["error", str(e)]]

    # Run the three sheet reads concurrently (they're independent network calls).
    with ThreadPoolExecutor(max_workers=3) as ex:
        f_fb   = ex.submit(read, sheet_id, "Facebook!A1:N2000")
        f_svd  = ex.submit(read, sheet_id, "SVD!A1:O500")
        f_lead = ex.submit(read, LEADS_SHEET_ID, "Sheet1!A1:Q5000")
        fb, svd, leads_raw = f_fb.result(), f_svd.result(), f_lead.result()

    err = leads_raw[0] if (leads_raw and leads_raw[0] and leads_raw[0][0] == "error") else None
    leads_parsed = [] if err else parse_lead_rows(leads_raw)
    return {
        "facebook_tab": fb,
        "svd_tab": svd,
        "meta_leads_timed": leads_parsed,
        "meta_leads_error": err,
    }

# ---------- ASSEMBLE (Meta calls + Sheets all concurrent) ----------
def run_fetch():
    jobs = {
        "yc": ("campaign", day(1), day(1)),
        "ya": ("adset",    day(1), day(1)),
        "yd": ("ad",       day(1), day(1)),
        "l7": ("campaign", day(7), day(1)),
        "l30":("ad",       day(30), day(1)),
    }
    results = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        meta_futs = {k: ex.submit(meta_insights, *v) for k, v in jobs.items()}
        sheet_fut = ex.submit(fetch_sheets)
        for k, fut in meta_futs.items():
            results[k] = shape_meta(fut.result())
        sheet = sheet_fut.result()

    data = {
        "dates": {"yesterday": day(1), "daybefore": day(2), "today": day(0), "tz": "IST"},
        "meta": {
            "yesterday_campaigns": results["yc"],
            "yesterday_adsets":    results["ya"],
            "yesterday_ads":       results["yd"],
            "last7_campaigns":     results["l7"],
            "last30_ads":          results["l30"],
        },
        "sheet": sheet,
    }
    with open(os.path.join(os.path.dirname(__file__), "data.json"), "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Wrote data.json — Meta insights + timed leads + Facebook/SVD tabs (concurrent fetch)")

# ---------- TELEGRAM ----------
def send_telegram_file(path="report.md"):
    token = os.environ.get("TELEGRAM_BOT_TOKEN", ""); chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not token or not chat_id:
        print("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID"); return False
    try:
        with open(os.path.join(os.path.dirname(__file__), path), encoding="utf-8") as f:
            msg = f.read()
    except FileNotFoundError:
        print(f"No {path} to send"); return False
    chunks = [msg[i:i+3800] for i in range(0, len(msg), 3800)] or [msg]
    ok = True
    for chunk in chunks:
        # NOTE: send as PLAIN TEXT (no parse_mode). Markdown tables/symbols in the report
        # break Telegram's parser and cause silent failures — plain text is reliable.
        body = urllib.parse.urlencode({
            "chat_id": chat_id, "text": chunk, "disable_web_page_preview": "true",
        }).encode()
        try:
            req = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=body)
            with urllib.request.urlopen(req, timeout=20) as r:
                if not json.load(r).get("ok"):
                    ok = False; print("Telegram returned not-ok")
        except Exception as e:
            ok = False; print("Telegram send failed:", e)
    print("Report sent to Telegram." if ok else "Telegram delivery had errors.")
    return ok

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--send":
        send_telegram_file("report.md")
    else:
        run_fetch()
