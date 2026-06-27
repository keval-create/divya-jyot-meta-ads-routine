# CLAUDE.md — divya-jyot-meta-ads-routine

Daily analytics routine for **Divya Jyot LYF Rewa** (real-estate, Mumbai). Each day it pulls
Meta Ads performance + the sales team's Google Sheets + the timed CRM leads, then produces a
single blunt, mobile-first Telegram report covering ad performance AND how the sales team
handled the leads (speed-to-lead, quality, diagnostics).

## Repo layout
- `fetch_all.py` — the data fetcher. Pulls Meta Ads insights, the team Google Sheet
  (Facebook + SVD tabs), and the V3 CRM Event sheet (timed leads). Writes `data.json`.
  Also handles Telegram delivery via `python3 fetch_all.py --send`.
- `CLAUDE-crossref-routine.md` — **the routine spec.** Read it in full before producing a
  report: it defines the exact flow, the required report sections, tone, and the
  "improve over time" memory discipline. This file is the source of truth for *what to do*;
  the section below is just orientation.
- `data.json` — generated each run (gitignored conceptually; it's the fetcher's output).
- `reports/` — `YYYY-MM-DD.md` per day, plus `latest.md` and `_memory.md` (cross-day memory).

## The daily flow (per CLAUDE-crossref-routine.md)
1. `python3 fetch_all.py` → writes `data.json`.
2. Read `data.json`. Analyse as BOTH ad agency + sales manager.
3. Read the last few `reports/` (esp. `latest.md`, `_memory.md`) to follow up on prior calls.
4. Write `report.md` + `reports/YYYY-MM-DD.md` + `reports/latest.md`, update `reports/_memory.md`.
5. Commit everything.
6. `python3 fetch_all.py --send` → delivers `report.md` to Telegram.

## Environment / config
`fetch_all.py` is driven entirely by env vars (no config file):
- `META_AD_ACCOUNT_ID` (the `act_` prefix is auto-added), `META_ADS_TOKEN` (needs `ads_read`)
- `GOOGLE_SHEET_ID`, `LEADS_SHEET_ID` (has a default), `GOOGLE_SA_B64` / `GOOGLE_SA_JSON`
  (service-account creds; base64 or raw JSON, auto-detected)
- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` (for `--send`)
- Meta API version is pinned (`API = "v25.0"`); timezone is IST throughout.
- Python deps used: `google-auth`, `google-api-python-client`, `google-auth-httplib2`,
  `httplib2` (stdlib for everything else — `urllib`, `ssl`, `concurrent.futures`).

## Gotchas baked into the code — do NOT regress these
- **Lead counting is canonical, never summed.** Meta returns the same leads under several
  overlapping action types (`onsite_conversion.lead_grouped`, `leadgen_grouped`, `onsite_lead`,
  `lead`). `leads_from()` returns ONE canonical type by priority — summing them multi-counts
  (~5×) and crushes CPL. `lead_actions_raw` is kept in every row as an audit trail; report
  numbers MUST reconcile with Ads Manager.
- **Attribution is pinned** to 7-day click + 1-day view to match Ads Manager's default.
- **TLS verification is intentionally disabled** for Meta + Google calls because the runtime
  env uses a self-signed proxy cert. This is deliberate, not a bug to "fix."
- **Telegram is sent as plain text**, no `parse_mode` — markdown tables/symbols break
  Telegram's parser and cause silent delivery failures.
- The fetcher runs all Meta calls + Sheet reads **concurrently** (ThreadPoolExecutor) to keep
  runtime down; keep new fetches inside that pattern.

## Analysis principles (business context — see routine doc for full detail)
- Product: bare-shell studio, ₹87L, Mulund West. The real metric is **cost per site visit**
  and **warm-lead rate**, not CPL. **Never recommend pausing an ad on CPL alone.**
- Speed-to-lead (how fast the team called an OTP-verified lead) is the most important section.
- Always be honest about match rate / stale data — never fabricate a number; mark unknowns.

## Git
- Work on the branch you were assigned; commit reports + code together with clear messages.
- Don't commit secrets — all credentials come from env vars, never hard-code them.
