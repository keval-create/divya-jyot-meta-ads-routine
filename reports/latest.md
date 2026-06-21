# Routine Failed — Both Data Sources Unavailable (2026-06-20)

**No quality analysis could be produced today. Both Meta Ads and the Google Sheet returned errors.**

---

## What failed

### 1. Meta Ads API — 403 Forbidden
All five Meta API calls (yesterday campaigns, adsets, ads; last-7 campaigns; last-30 ads) returned `HTTP Error 403: Forbidden`.

**Likely cause:** The `META_ADS_TOKEN` is expired. Meta long-lived user tokens last ~60 days; system user tokens are permanent but can be revoked. The account ID (`act_1078185463738176`) looks correct.

**Fix:** Generate a new long-lived token at [Meta Business Suite → System Users] or re-authenticate via the Graph API Explorer and update the `META_ADS_TOKEN` secret in the Claude Code routine settings.

### 2. Google Sheet — `GOOGLE_SA_JSON` secret is truncated
The `GOOGLE_SA_JSON` environment variable contains only `{` — a single opening brace. The full service-account JSON was not saved correctly when the secret was configured.

**Fix:** Open the service account key file (a JSON file downloaded from Google Cloud → IAM → Service Accounts) and paste the **entire** contents into the `GOOGLE_SA_JSON` secret. It should be ~2,400 characters and start with `{"type": "service_account", ...}`.

---

## What this means

- **No spend data.** Can't report yesterday's ₹ spend, leads, or CPL.
- **No sheet cross-reference.** Can't assess lead quality, warm-lead rate, or site visits.
- **No recommendations possible** without data.

---

## What to do now

1. **Fix `META_ADS_TOKEN`** — refresh the token, update the secret, re-run.
2. **Fix `GOOGLE_SA_JSON`** — paste the full service-account JSON into the secret, re-run.
3. Once both secrets are corrected, re-trigger this routine manually to get today's quality read.

---

*Routine run: 2026-06-21 | Report date: 2026-06-20*
