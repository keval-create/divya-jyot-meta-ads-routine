# Daily Snapshot — Divya Jyot LYF Rewa
**Date:** 24 June 2026 (report run: 25 June ~7PM IST)
**Campaign:** Divya Jyot V3 June26 | Ad: Studio | Adset: Open - DJR

---

## 1. HEADLINE

Meta API is fully dark — 400 errors across every endpoint, zero spend/CPL/CTR data available — but the campaign is alive: 14 leads since June 23 resume, V3 site-visit rate at **6.7% (beats the 4.5% baseline)**, and a confirmed warm lead (Sandeep Shah, ₹87L budget) who may be visiting TODAY (Thursday June 26).

---

## 2. THE FUNNEL (today June 25, midnight–~7PM IST)

**Meta ad metrics: UNAVAILABLE** — HTTP 400 Bad Request on all API calls (today, yesterday, last-7, last-30). Likely a token expiry or account permission issue stemming from the June 22 security-flag pause. Fix this before anything else.

**Leads today (3 confirmed):**
- 00:12 IST — Mitesh Shah (FB, 3–6 months) — Voicemail, no follow-up yet
- 02:59 IST — Rajesh Kothari (FB, within_3_months) — Out of service
- 07:43 IST — Vivek Dwivedi (IG, within_3_months) — 1RK ₹60L (dead, budget too low)

**Team contact today:** All 3 have a first-call attempt logged. The midnight/3AM leads are understandably hard to reach — acceptable for now, but Mitesh Shah (3–6 months) needs a callback this evening.

**Site visits today:** 0 new. Rewashankar Gomtiwal visited June 24 (same day as lead — excellent).

**V3 campaign window (June 10–25, for context):**
- Total leads: 60
- Matched in Facebook sheet: 57/60 (95%)
- Confirmed site visits: 4 (see section 5)

---

## 3. AD PERFORMANCE (agency hat)

**META API: DOWN.** HTTP 400 Bad Request on all endpoints — today, yesterday, last-7 days, last-30 days. Cannot report spend, impressions, CTR, CPM, CPC, frequency, or CPL for any window.

**What we know from context:**
- Campaign "Divya Jyot V3 June26" was PAUSED June 22 due to a Meta account-security flag
- It RESUMED after a budget-threshold protection was set
- Leads continue arriving (June 23: 4, June 24: 7, June 25: 3 so far) — delivery is confirmed
- The API issue may be a token expiry coinciding with the security-flag incident, or a permissions change on the ad account

**Action required:** Check META_ADS_TOKEN expiry. If the token was refreshed or revoked during the June 22 security review, generate a new one and update the environment variable. Without this, every future report will be data-blind on the ad side.

---

## 4. SPEED-TO-LEAD (sales-manager hat)

**V3 campaign June 10–25 (57 matched leads):**
- Same-day contact: ~40 (70%) ✓
- 1–3 day lag: 4 (7%)
- >3 day lag: 11 (19%) ⚠
- No date data: 2

**The 70% same-day rate is GOOD.** The team is picking up new leads quickly.

**The 19% >3 day lag needs attention.** Several June 10–12 leads (milind, Madhukar Bhavsar, theDaniel, Vipul Rakhasia) show first follow-up dates of June 17–18, a 7-day gap. These were within_3_months leads. Each day of delay on an OTP-verified lead drops contact probability sharply.

**Recent leads (June 23–25): team is dialling next-day** — follow-ups on June 24 for June 23 leads, June 25 for June 24 leads. Good rhythm.

**Today's leads (June 25):**
- Mitesh Shah (00:12 IST, 3–6 months): voicemail so far — call again this evening
- Rajesh Kothari (02:59 IST, within_3_months): out of service — retry 2–3 more times over next 2 days before writing off
- Vivek Dwivedi (07:43 IST): dead (1RK, ₹60L) — no further effort needed

**Named priority miss:**
- **Uday Masurkar (9833676559, June 10, 3–6 months):** Feedback says "Req 1 bhk, Coming Saturday." Follow-up notes say "13/06/26 Coming Sunday." He made TWO visit commitments and is still marked Cold. Did he actually visit? This needs a direct check today.
- **Sandeep Shah (9223200118, June 14, just_exploring → Warm):** Only warm lead in 60. Budget ₹87L exact. Feedback: "coming next thursday." If that was June 19 (missed) or June 26 (tomorrow), either way needs a call TODAY.

---

## 5. LEAD QUALITY (sales-manager hat)

**60 V3 leads, June 10–25:**

| Status | Count | % |
|--------|-------|---|
| Cold   | 49    | 82% |
| Dead   | 7     | 12% |
| Warm   | 1     | 2%  |
| Unmatched | 3  | 5%  |

**Warm rate: 1.7% — below the 2.3% V3 baseline.** But see site-visit rate below.

**Dead breakdown (7 leads):**
- Budget too low: Shraddha Narvekar (₹55L), Vivek Dwivedi (1RK ₹60L)
- 2BHK at wrong budget: Tilak Deorukhakar (2BHK ₹90L — product mismatch)
- Rental seeker: Suman Yadav
- Invalid number: norwin saloman
- Silent dead: Noorjaha Shaikh (no answer ever)
- By mistake: Naresh Sachade

**Quality leaks in "Cold" pool:**
- Dhiraj Dand (June 23): asking ₹20,000/sqft → ~₹80L for the studio — pre-screen budget immediately
- Gaykawad Sushant (June 24): 1BHK ₹85L — 2L below ask, borderline
- Chandrashekhar (June 24): 1BHK ₹85L — same
- Sudarshan Gaikwad (June 10): 1RK ₹50L — dead on budget, still Cold

**V3 SITE VISITS (4 confirmed from this campaign):**

| Lead | Arrived | Visited | Intent | Budget | Notes |
|------|---------|---------|--------|--------|-------|
| Swati Wankhede | June 13 | June 19 | within_3_months | ₹60L | Low budget, but visited |
| Manjula Mahida | June 19 | June 20 | 3–6 months | ₹90L | Borderline budget |
| Sandeep Shah | June 20 | June 20 | just_exploring | ₹1cr | Strong budget, same-day visit |
| Rewashankar Gomtiwal | June 24 | June 24 | just_exploring | undisclosed | Same-day visit |

**Site-visit rate: 4/60 = 6.7% — ABOVE the 4.5% historical baseline.** V3 is working on this metric. The warm-lead rate (1.7%) lags the 2.3% baseline, but visit conversion compensates.

**Cost per site visit: CANNOT COMPUTE** — no spend data (Meta API down).

**Unmatched leads (3 not in Facebook sheet):**
- Ravi DU (9321110668, June 10, within_3_months)
- ANDRE BRIAN EDWARD ROZARIO (9821266080, June 14, 3–6 months)
- Atul Thorat (9819877789, June 24, within_3_months) — **add these to the sheet today**

---

## 6. DIAGNOSTIC STEPS (both hats, ranked)

**1. FIX THE META API TOKEN — TODAY (agency hat)**
All 7 Meta API endpoints returning HTTP 400. This is either a token expiry or a permissions change from the June 22 security incident. Action: log into Meta Business Suite, check the token under System Users or App settings, regenerate if expired, and update META_ADS_TOKEN. Every day this is broken is another day you can't see spend or CPL.

**2. CALL SANDEEP SHAH NOW (sales-manager hat)**
Phone 9223200118. Only Warm lead in 60. Budget ₹87L, said "coming next Thursday." That Thursday could be today or tomorrow (June 25/26). He's not in the SVD tab — no visit logged yet. If he doesn't answer, leave a specific voicemail: "We have a slot for you this evening/tomorrow morning."

**3. ADD ATUL THORAT + RAVI DU + ANDRE ROZARIO TO FACEBOOK SHEET (sales-manager hat)**
Three leads (including one within_3_months from today, June 24) have no record in the team sheet. They're receiving zero follow-up. Add them and call today.

**4. ADD BUDGET SCREENING SCRIPT TO FIRST CALL (sales-manager hat)**
Multiple leads slipping through at ₹60–85L for an ₹87L product. Every call should open with: "Our studio is priced at ₹87 lakh — does that fit your budget?" If no, exit gracefully in 60 seconds. This trims wasted follow-up on Sudarshan Gaikwad (₹50L, 6 follow-ups), Shraddha Narvekar (₹55L, zero follow-up but correctly dead), Dhiraj Dand.

**5. UDAY MASURKAR RESOLUTION (sales-manager hat)**
Phone 9833676559. Two separate visit promises (June 10 and June 13). Still Cold. Call to find out: did he visit (SVD lookup shows no match), or is this stalling? If he genuinely hasn't come, a firm close — "I can book you a private slot tomorrow morning" — may convert him.

---

## 7. ANYTHING ELSE

**Purchases in the pipeline (older leads converting):**
The SVD tab records 4 purchases from this campaign's lead pool:
- Pankaj Thakkar — purchased April 14, 2026 (July 2025 lead, took 9 months)
- Aasha Jain — purchased April 5, 2026
- Rinkesh Shah — purchased May 8, 2026
- Umesh Kadam — purchased May 20, 2026 (in Vikhroli — another project, lost sale)

This matters because it confirms the funnel does convert over a 6–12 month tail. "Cold" doesn't mean "dead" — it means the follow-up cadence needs to stay alive.

**The campaign is delivering after the June 22 resume.** 14 leads in June 23–25, including a same-day site visit on June 24 from a just_exploring lead (Rewashankar Gomtiwal). The ads are working. The Meta API issue is a reporting problem, not a delivery problem — but it needs to be fixed so you can see CPL, frequency, and whether the creative is starting to fatigue.

**Intent signal looks reasonable:**
- within_3_months: 33/60 (55%) — above half the funnel is actively buying
- 3–6 months: 14/60 (23%)
- just_exploring: 13/60 (22%)

The "just_exploring" leads delivered 2 of the 4 site visits (Sandeep Shah and Rewashankar Gomtiwal) — don't discount them. Intent declared on a form isn't always what shows up at the site.
