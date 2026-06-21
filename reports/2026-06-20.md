# Divya Jyot LYF — Daily Quality Audit: June 20, 2026

**22% warm-lead rate over last 30 days — significantly above the historical 2.3% baseline. V3 form is working. The problem is 47% unreachable leads and slow team follow-up. Speed-to-lead timestamps blocked: Meta token needs `leads_retrieval` permission.**

---

## 1. Yesterday's Spend vs Quality (June 20)

| Metric | Value |
|---|---|
| Spend | ₹533.95 |
| Meta leads | 15 |
| CPL | ₹35.60 |
| Reach | 1,941 |
| CTR | 2.26% |
| Frequency | 1.16 |

**Of 15 leads, 4 logged in sheet so far (27%)** — team is still catching up. What's been logged:

| Lead | Status | Notes |
|---|---|---|
| Sandeep shah (8850364329) | ✅ Site visit done | 1 BHK, ₹1cr budget — **good fit** |
| Suman yadav (8108958550) | ❌ Dead | Looking for rent |
| Dimple dedhia (9819292880) | Unreachable | Busy, ringing |
| Vikramjit kaushal (9876455912) | Unreachable | Busy |

11 of yesterday's 15 leads are not yet in the sheet. Quality on those is unknown.

**SVD visits confirmed on June 20:** 2 — Manjulamahida (₹90L, 1 BHK) + Sandeep shah (₹1cr, 1 BHK). Cost per visit: **₹267**. Both are Facebook leads from June 19–20.

---

## 2. Quality by Source — Last 30 Days (Jun 10–20, 45 leads tracked)

Single active configuration: Studio ad → Open-DJR adset → Divya Jyot V3 June26.

| Classification | Count | % |
|---|---|---|
| HOT (site visit done) | 3 | 6.7% |
| WARM (clear intent, budget fit) | 7 | 15.6% |
| DEAD (location/budget/fake) | 11 | 24.4% |
| UNREACHABLE (ringing/busy/voicemail) | 21 | 46.7% |
| Cold/unclear | 3 | 6.7% |

**Warm + HOT rate: 22.2%** — nearly 10× better than the historical 2.3% baseline. The OTP form is filtering meaningfully.

**Budget mismatches pulling quality down:**
- Sudarshan Gaikwad — ₹50L (way too low)
- Andre Rozario — ₹55L max
- Swati Wankhede — ₹60L (still visited! Lost cause on budget)
- Shweta Singh — max ₹80L
- Bhakti Bhanushali — ₹85L (borderline)

**Location mismatches:**
- Reema Desai — wants Kandivali/Borivali
- Anant — wants Thane
- Manal — lives in Dombivali, looking for 1RK there

**Best missed conversion — Sandeep Shah (Jun 14):** Budget ₹87L for 1RK — an exact match for this studio. Said "coming next Thursday" (Jun 19). Team called 18/6, 19/6, 20/6 — ringing each time. Never came in. This is a genuine warm lead who went cold. Budget fits to the rupee.

---

## 3. Real Cost Per Site Visit

| Window | Spend | Facebook SVD visits | Cost/visit |
|---|---|---|---|
| Yesterday | ₹533.95 | 2 | **₹267** |
| 7-day | ₹4,199 | 3 | ₹1,400 |
| 30-day | ₹8,344 | 3 | **₹2,781** |

Vanity CPL: ₹35.60–₹44.20. Real cost per visit is 75× the CPL — expected, and at ₹2,781 per visit this is defensible for an ₹87L product where a single booking covers the full campaign spend many times over.

**Visit quality concern:** 1 of the 3 recent visits (Swati, Jun 19) has a ₹60L budget — she'll never close. So 2 of 3 visits are viable buyers. Viable-buyer cost/visit = ₹4,172 over 30 days.

---

## 4. Speed-to-Lead (New Feature — Partially Blocked)

The new `fetch_all.py` attempts to pull individual Meta leads with exact `created_time` timestamps for speed-to-lead measurement. **Currently blocked by two permission gaps:**

**Gap 1 — Meta token missing `leads_retrieval`:**
> `(#100) Tried accessing nonexisting field (leadgen_forms)`

The current token has `ads_read` but not `leads_retrieval`. Without it, individual lead timestamps and phone numbers can't be fetched from Meta. Action: generate a new token with `ads_read` + `leads_retrieval` permissions (requires Facebook app with `leads_retrieval` in Advanced Access).

**Gap 2 — Google Drive revisions returned 0:**
The service account fetches Sheets data fine but returns no revision history. The Drive API either isn't enabled in the GCP project or the SA doesn't have the Sheet in its Drive scope. Action: enable Google Drive API in the project console, or share the sheet with the SA at the Drive level (not just Sheets).

**What the sheet notes suggest (approximate):**
From the dated follow-up entries, Jun 10 leads are being called on 13/6, 18/6, 19/6, 20/6 — meaning first contact is happening 3–8 days after lead arrival for many. If the OTP-warm window is 30–60 minutes, this is a significant gap. But this is inferred from follow-up dates, not actual call timestamps — it could be that a same-day call happened that isn't logged.

Once the token and Drive permissions are fixed, speed-to-lead will be available per-lead in future runs.

---

## 5. Trend

- **Warm-lead rate:** 22.2% (last 30 days) vs 2.3% historical — V3 OTP form is working, this is the headline win
- **Unreachable rate:** 46.7% — this is the dominant problem. Nearly half of all leads can't be reached. Whether that's because of slow follow-up, bad numbers, or genuinely unavailable people, the sheet notes don't distinguish
- **CPL:** ₹35.60 (yesterday) to ₹44.20 (7-day) — mild fluctuation, acceptable range
- **Frequency:** 2.46 (30-day) — still below 3, audience not fatigued
- **CTR:** 3.05% (30-day) → 2.26% (yesterday) — slight dip, watch but not alarming

---

## 6. Recommendations (Ranked)

**1. Fix speed-to-lead permissions — this is the point of today's feature.**
- Meta: regenerate token with `leads_retrieval` permission
- Google: enable Drive API in Cloud Console, confirm SA has Drive-level access to the sheet
- Once fixed, this routine will report per-lead response times automatically

**2. Attack the unreachable pile — it's nearly half your leads.**
46.7% unreachable is not acceptable for an OTP-verified form. These people completed OTP, so their numbers are real and they were engaged. Calling within 30 minutes of form submission catches them before they forget. Schedule a morning blitz: call every lead from the previous evening within the first hour of business.

**3. Recover Sandeep Shah (₹87L, 1RK, exact fit).**
Lead from Jun 14, perfect budget match, said he'd visit Jun 19. Didn't show. Team has rung 3 times — try WhatsApp message today with a site photo and a specific time slot offer.

**4. Add a budget question to the form.**
5 leads in the last 30 days have budgets of ₹50–80L — well below the studio's ₹87L floor. Each is a wasted call. A single "What's your approx. budget?" field on the form would filter these out before they enter the pipeline.

**5. Get yesterday's 11 unlogged leads into the sheet today.**
Only 4 of 15 Jun 20 leads are logged. The others are aging — every hour without a call reduces the chance of an answer. Log and call before end of day.

---

*One active campaign: Divya Jyot V3 June26 / Studio ad / Open-DJR adset.*
*Speed-to-lead: blocked — Meta `leads_retrieval` + Drive revision permissions needed.*
*Sheet match rate (30-day): 45/225 = 20% logged. More complete for recent dates; older leads have full follow-up history.*
