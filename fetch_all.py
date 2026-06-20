#!/usr/bin/env python3
"""
Divya Jyot — Daily data fetcher for the 7 PM cross-reference routine.
Pulls (A) Meta Ads performance and (B) the team's Google Sheet, writes both
to data.json for Claude Code to analyse and cross-reference.

ENV VARS REQUIRED:
  META_AD_ACCOUNT_ID   e.g. act_1078185463...
  META_ADS_TOKEN       long-lived token with ads_read
  GOOGLE_SHEET_ID      13T80cprP08eC2ap0i3x-lVInOSZPOmFBDbiNUlIPJvw
  GOOGLE_SA_JSON       path to service-account JSON with read access to the sheet
                       (share the sheet with the service account email)
"""
import json, os, urllib.request, urllib.parse
from datetime import date, timedelta

# ---------- META ----------
AD_ACCOUNT_ID = os.environ.get("META_AD_ACCOUNT_ID", "act_XXXXXXXXXX")
TOKEN = os.environ.get("META_ADS_TOKEN", "")
API = "v25.0"

def day(n): return (date.today() - timedelta(days=n)).isoformat()

def meta_insights(level, since, until):
    params = {
        "level": level,
        "fields": "campaign_name,adset_name,ad_name,spend,impressions,reach,clicks,ctr,cpm,frequency,actions",
        "time_range": json.dumps({"since": since, "until": until}),
        "limit": "200", "access_token": TOKEN,
    }
    url = f"https://graph.facebook.com/{API}/{AD_ACCOUNT_ID}/insights?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url) as r:
            return json.load(r).get("data", [])
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

# ---------- GOOGLE SHEET ----------
def fetch_sheet():
    """Reads Facebook + SVD tabs via Google Sheets API using a service account."""
    try:
        from google.oauth2.service_account import Credentials
        from googleapiclient.discovery import build
    except ImportError:
        return {"error": "pip install google-api-python-client google-auth"}

    sheet_id = os.environ.get("GOOGLE_SHEET_ID", "")
    # On Anthropic Cloud Routines the key is stored as a SECRET (env var),
    # not a file. GOOGLE_SA_JSON holds the full JSON content as a string.
    sa_json_str = os.environ.get("GOOGLE_SA_JSON", "")
    if not sa_json_str or not sheet_id:
        return {"error": "Missing GOOGLE_SA_JSON (paste full JSON) or GOOGLE_SHEET_ID"}

    sa_info = json.loads(sa_json_str)
    creds = Credentials.from_service_account_info(
        sa_info, scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"])
    svc = build("sheets", "v4", credentials=creds)

    def read(rng):
        try:
            res = svc.spreadsheets().values().get(spreadsheetId=sheet_id, range=rng).execute()
            return res.get("values", [])
        except Exception as e:
            return [["error", str(e)]]

    return {
        "facebook_tab": read("Facebook!A1:N300"),   # incoming leads + status/feedback
        "svd_tab":      read("SVD!A1:O200"),         # site visits
    }

# ---------- ASSEMBLE ----------
data = {
    "dates": {"yesterday": day(1), "daybefore": day(2), "today": day(0)},
    "meta": {
        "yesterday_campaigns": shape_meta(meta_insights("campaign", day(1), day(1))),
        "yesterday_adsets":    shape_meta(meta_insights("adset",    day(1), day(1))),
        "yesterday_ads":       shape_meta(meta_insights("ad",       day(1), day(1))),
        "last7_campaigns":     shape_meta(meta_insights("campaign", day(7), day(1))),
        "last30_ads":          shape_meta(meta_insights("ad",       day(30), day(1))),
    },
    "sheet": fetch_sheet(),
}

with open(os.path.join(os.path.dirname(__file__), "data.json"), "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("Wrote data.json — Meta + Google Sheet")
