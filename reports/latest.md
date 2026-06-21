# Divya Jyot LYF — Daily Quality Audit: June 20, 2026

**2 site visits yesterday at ₹267 each. Drive revision history now live. Unreachable rate hit 52% — half your leads can't be reached. Meta `leads_retrieval` token still needed for exact speed-to-lead times.**

---

## 1. Yesterday's Spend vs Quality (June 20)

| Metric | Value |
|---|---|
| Spend | ₹533.95 |
| Meta leads | 15 |
| CPL | ₹35.60 |
| Reach | 1,941 |
| 7-day frequency | 1.91 |

**4 of 15 leads logged so far (27%)** — 11 still missing from the sheet:

| Lead | Status | Notes |
|---|---|---|
| Sandeep shah (8850364329) | ✅ Site visit done | 1 BHK, ₹1cr budget — **exact fit** |
| Suman yadav (8108958550) | ❌ Dead | Looking for rent |
| Dimple dedhia (9819292880) | Unreachable | Busy, ringing |
| Vikramjit kaushal (9876455912) | Unreachable | Busy |

**SVD visits Jun 20:** 2 — Manjulamahida (₹1cr, 1 BHK) + Sandeep shah (₹1cr, 1 BHK). Cost per visit: **₹267**. Both are Facebook leads from Jun 19–20.

---

## 2. Quality by Source — Jun 10–21 (48 leads tracked)

Single active configuration: Studio ad → Open-DJR adset → Divya Jyot V3 June26.

| Classification | Count | % |
|---|---|---|
| WARM/HOT (intent + budget fit) | 7 | 14.6% |
| DEAD (location/budget/fake/rental) | 13 | 27.1% |
| UNREACHABLE (ringing/busy/switched off) | 25 | 52.1% |
| Cold/unclear | 3 | 6.2% |

**Warm + HOT rate: 14.6%** — still 6× the historical 2.3% baseline. OTP form continues to filter.

**Active warm pipeline (need follow-up today):**
- **Uday Masurkar (10/06)** — req 1 BHK, said "Coming Saturday" Jun 13, then "Coming Sunday" Jun 14. Ringing 18/6, 19/6, 20/6, 21/6 — 4 consecutive days unreachable. Was genuinely warm, now going cold.
- **Nehal Mota (12/06)** — budget ₹1cr, 1 BHK. Busy 13/6, busy 18/6, busy 19/6. Location concern: lives in Dombivali — confirm they'll travel to Mulund.
- **Bhakti Bhanushali (11/06)** — req 1 BHK 400+ sqft, budget ₹85L. Borderline budget (₹87L ask) but close enough to pursue.
- **Sandeep Shah (14/06)** — budget ₹87L, 1RK exact fit. Said "coming next Thursday" (Jun 19). Called 18/6, 19/6, 20/6 — ringing each time. **Best missed conversion in the pipeline. Try WhatsApp today.**

**Budget mismatches pulling quality down:**
- Sudarshan Gaikwad — ₹50L (too low)
- Andre Rozario — max ₹55L (too low)
- Shweta Singh — max ₹80L (₹7L short, borderline)

**Location mismatches (dead):**
- Anant — wants Thane
- Manal — wants 1RK in Dombivali
- Reema Desai — wants Kandivali/Borivali

---

## 3. Real Cost Per Site Visit

| Window | Spend | SVD visits (Facebook) | Cost/visit |
|---|---|---|---|
| Yesterday (Jun 20) | ₹533.95 | 2 | **₹267** |
| 7-day | ₹4,199 | 3 | ₹1,400 |
| 30-day | ₹8,344 | 3 | **₹2,781** |

Vanity CPL: ₹35.60. Real cost per visit: 75× the CPL — expected at this funnel depth. ₹2,781 per visit is fully defensible for an ₹87L product.

---

## 4. Speed-to-Lead (Partially Unblocked)

**Drive revision history now working** — service account upgraded to Editor access. 47 revisions returned spanning May 27 – Jun 21.

**Sheet activity on June 20 (when the team worked the sheet):**

| Batch | IST time |
|---|---|
| 1st edit | 11:04 AM |
| 2nd edit | 12:30 PM |
| 3rd edit | 3:27 PM |
| 4th edit | 4:56 PM |

**Today (Jun 21) activity:** Sheet edited at 10:54 AM and 11:35 AM — team is working leads this morning.

**The gap:** The team's first sheet entry on Jun 20 was 11:04 AM. If leads were arriving through the morning (typical for Facebook), some waited hours before first contact. We can't confirm the exact lag because Meta lead `created_time` is still blocked.

**Still blocked:** `HTTP Error 400` on Meta leadgen_forms — token missing `leads_retrieval` permission. Once regenerated, speed-to-lead is reported per lead automatically.

---

## 5. Trend

- **Warm-lead rate:** 14.6% (Jun 10–21) vs 2.3% historical — still 6× above baseline
- **Unreachable rate:** 52.1% — now the dominant problem. More than half of all leads can't be reached despite OTP-verified numbers
- **CPL:** ₹35.60 — stable
- **Frequency:** 1.91 (7-day) — audience not fatigued, headroom to scale
- **Site visits:** 2 in one day yesterday (₹267/visit) — strongest single-day result in the tracked period

---

## 6. Recommendations (Ranked)

**1. WhatsApp Sandeep Shah (₹87L, 1RK, exact fit) — today.**
Three consecutive calls went unanswered. Send a WhatsApp with a site photo and a specific slot: "Are you free Thursday 11 AM for a site visit? I've set aside time." This lead is still warm — don't let it die from call fatigue.

**2. Same for Uday Masurkar — 4 days ringing is too long.**
He said he was coming twice (Jun 13, Jun 14). Four unanswered calls since. Try WhatsApp or a different number. If no response by tomorrow, move to dead.

**3. Attack the unreachable pile with an evening blitz.**
52% unreachable is not acceptable for OTP-verified leads. People who submitted at 9 AM won't answer until 7–8 PM. Run a dedicated callback round every evening for the day's unanswered leads.

**4. Fix the Meta `leads_retrieval` token.**
Regenerate the Facebook token with `ads_read` + `leads_retrieval` permissions (requires Advanced Access in the Facebook app settings). This unlocks per-lead arrival timestamps and closes the speed-to-lead measurement loop.

**5. Log yesterday's 11 unlogged leads today.**
Only 4 of 15 Jun 20 leads are in the sheet. The others are now 24+ hours old. Log and call before end of day — answer rates drop sharply after 48 hours.

---

*One active campaign: Divya Jyot V3 June26 / Studio ad / Open-DJR adset.*
*Speed-to-lead: Drive revisions ✅ (47 entries). Meta `leads_retrieval` ❌ (token permission needed).*
*Sheet match rate (Jun 10–21): 48 leads tracked of ~95 7-day Meta leads = ~50% logged.*
