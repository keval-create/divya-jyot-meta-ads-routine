# Divya Jyot LYF Rewa — Daily Snapshot — Tue 1 Jul 2026

*First report in this series — no prior report to follow up on. `reports/_memory.md` started today.*

## 1. HEADLINE
Best CTR and lowest frequency of the last 30 days (3.22% CTR, 1.21 frequency) drove CPL down to
₹106 — but only 1 of the last 78 Meta leads is actually marked **Warm** in the sheet, and that
number is a sales-tracking problem, not an ad problem: 3 of the 4 leads that *did* visit the
site this month were still sitting in "Cold" status. The ad is working; the CRM hygiene isn't
keeping up with it.

## 2. THE FUNNEL — Tue 1 Jul 2026 (full day)
| Stage | Number |
|---|---|
| Spend | ₹636.96 |
| Impressions | 3,109 |
| Reach | 2,580 |
| Clicks (link clicks) | 100 (63) |
| Leads (canonical, verified vs `lead_actions_raw`) | 6 |
| CPL | ₹106.16 |
| Contacted by team (status/feedback logged) | 6 / 6 (100%) |
| Still untouched | 0 |
| Site visits logged yesterday | 0 (most recent SVD entry is 27 Jun) |

Lead split: 3 Facebook / 3 Instagram. Intent split: 3 within_3_months / 3 just_exploring.
`leads` matches the single canonical action (`onsite_conversion.lead_grouped` = `lead` = 6) —
no double-count, this ties to what Ads Manager shows.

**Today (2 Jul) so far, midnight–~7PM IST, still moving:** ₹400.40 spend, 1,860 impressions,
36 clicks, **3 leads**, CPL ₹133.47, CTR 1.94%. Partial day — don't read too much into it yet.

## 3. AD PERFORMANCE (agency hat)
One ad carrying 100% of spend: **"Studio"** in adset **"Open - DJR"**, campaign **"Divya Jyot V3
June26"**. (A second adset, "Luxury - DJ", has ₹7.76 lifetime spend and 0 leads — effectively
inactive, ignore it.)

| Window | Spend | Leads | CPL | CTR | CPC | CPM | Frequency |
|---|---|---|---|---|---|---|---|
| Yesterday (1 Jul) | ₹636.96 | 6 | ₹106.16 | 3.22% | ₹6.37 | ₹204.88 | 1.21 |
| Last 7 days | ₹4,255.01 | 22 | ₹193.41 | 2.43% | ₹8.77 | ₹212.77 | 1.76 |
| Last 30 days | ₹13,939.76 | 79 | ₹176.45 | 2.84% | — | — | 2.68 |

Yesterday beat both the 7-day and 30-day averages on every metric — CTR up, CPC down, frequency
down. **Frequency has been falling (2.68 → 1.76 → 1.21), not climbing — the creative is not
fatiguing.** No refresh needed on that basis.

Post-pause context: the campaign was paused 22 Jun for a Meta account-security flag. The V3
timed-lead log confirms **zero leads on 22 Jun** (the only zero day in the last 3 weeks), then
recovered from 23 Jun onward. Delivery is now healthy — yesterday was the best day since the
pause. Don't touch budget or creative on CPL grounds; the fundamentals are fine.

One risk: 100% of spend is on a single ad/creative. There's no hedge if this one fatigues later —
worth prepping a second creative variant now, before it's needed.

## 4. SPEED-TO-LEAD (sales-manager hat)
Matched 78 of 82 V3 timed leads (Jun 10 – Jul 2) to the Facebook tab by phone — **95.1% match
rate**. Of those, 49 had a dated follow-up note we could use to compute lag (the rest only have
undated notes like "Ringing" — day-level precision only, no times are written in the sheet).

**Overall (49 with dated follow-ups):** avg lag 2.6 days · same-day 5 · 1–3 days 30 · >3 days 14.

Yesterday's 6 leads all show a populated Cold/Dead status (i.e., contacted), but none have a
dated follow-up note yet to compute exact lag — too recent. Three leads from 30 Jun *do* show
first dated contact on 1 Jul (1-day lag): Nishant Kamdar, Vikas Bodwade, saumya.

**Fastest (same-day):**
| Name | Meta arrival (IST) | First dated contact | Lag | Intent |
|---|---|---|---|---|
| Jyothi Gowda | 2026-06-27 01:09 | 2026-06-27 | 0d | within_3_months |
| Parag Chavan | 2026-06-27 09:48 | 2026-06-27 | 0d | within_3_months |
| vikramjit kaushal | 2026-06-21 10:12 | 2026-06-21 | 0d | within_3_months |
| Dimple Dedhia | 2026-06-20 14:49 | 2026-06-20 | 0d | within_3_months |

**Slowest — and this is the real miss:**
| Name | Meta arrival (IST) | First dated contact | Lag | Intent |
|---|---|---|---|---|
| anant | 2026-06-11 00:45 | 2026-06-20 | **9d** | within_3_months |
| milind | 2026-06-10 11:26 | 2026-06-18 | 8d | within_3_months |
| Madhukar Bhavsar S. | 2026-06-10 11:58 | 2026-06-18 | 8d | within_3_months |
| theDaniel | 2026-06-10 18:50 | 2026-06-18 | 8d | within_3_months |
| Vipul Rakhasia | 2026-06-10 20:14 | 2026-06-18 | 8d | within_3_months |

All five slowest are **within_3_months** — the highest-intent bucket — and all five are from the
first two days of this V3 batch (10–11 Jun), meaning this was a launch-week backlog, not a
current problem. **12 of 78 within_3_months leads overall sat >1 day before first dated contact**,
but every one of them is from 10–29 Jun; nothing from the last 3 days shows a multi-day gap in
the dated data. Read this as: the team was slow at V3 launch and has since tightened up — worth
confirming that trend holds over the next few reports.

## 5. LEAD QUALITY (sales-manager hat)
Classified all 78 matched V3 leads from feedback text + status:

| Bucket | Count | % |
|---|---|---|
| Unreachable (busy/switch off/out of service/invalid) | 27 | 34.6% |
| Uncontacted / still just "Ringing" | 19 | 24.4% |
| Cold, in progress (details shared, not resolved) | 11 | 14.1% |
| BHK mismatch (wants 2BHK/3BHK; project is studio/1BHK) | 7 | 9.0% |
| Dead, other reason | 7 | 9.0% |
| Location mismatch (Thane, Kandivali, wants rent) | 3 | 3.8% |
| Budget mismatch | 2 | 2.6% |
| **Warm/Hot (status)** | **1** | **1.3%** |
| Dead, explicitly not interested | 1 | 1.3% |

**Warm-rate (by status label) is 1.3% — below the ~2.3% historical baseline.** But that number is
misleading: cross-referencing the SVD (site-visit) tab against these same 78 phone numbers finds
**4 confirmed site visits** from this V3 batch (Rewashankar Gomtiwal, Swati Wankhede, Sandeep
Shah, Manjula Mahida) — a **~5.1% site-visit rate, above the 4.5% historical baseline.** Only
Sandeep Shah is marked Warm/Hot in the Status column; the other three who *actually walked the
site* are still logged as Cold. **The Status field is not being updated when a lead converts to a
visit** — that's a tracking gap, not a lead-quality gap. Fix: update Status to Warm/Hot the moment
a visit is booked or completed, so the column is usable for triage.

**Real cost-per-site-visit vs vanity CPL:** trailing 30 days, ₹13,939.76 spend against 5 logged
site visits (4 traceable to this V3 batch by phone, 1 — Naveen Suvarna, visited 27 Jun — sourced
"Facebook" in the SVD tab but not found in the V3 timed-lead log, likely pre-dates the 10 Jun
V3 sheet start or was logged under a different number; flagged, not fabricated) = **~₹2,788 per
site visit** (₹3,485 if counting only the 4 directly-matched). That's ~16–20x the ₹176 vanity CPL
— exactly why CPL alone is the wrong metric here, and by the historical-baseline comparison, V3
is currently converting to visits *at or slightly above* its target rate.

## 6. DIAGNOSTIC STEPS
1. **Sales — fix Status hygiene, not speed.** 3 of 4 site-visit conversions are mislabeled Cold.
   Make "update Status to Warm the moment a visit is booked" a standing rule — right now nobody
   scanning the sheet for hot leads would find Sandeep Shah's peers.
2. **Sales — second/third-attempt cadence for the "Ringing" bucket.** 19 leads (24.4%) never got
   past a first unanswered call. That's the single biggest recoverable pool — bigger than the
   Unreachable bucket, which is mostly genuinely dead numbers.
3. **Sales — screen BHK on the first call.** 7 leads (9%) want 2BHK/3BHK this studio/1BHK project
   can't serve; a 30-second qualifying question on the first ring would let the team disqualify
   and move on instead of chasing "Ringing" for a week.
4. **Agency — no action on CPL/CTR/frequency.** All three are trending the right direction
   post-pause. Do not pause or refresh creative on cost grounds.
5. **Agency — prep a second creative** so there's a hedge ready once frequency does climb back up;
   right now 100% of spend rides on one ad.

## 7. ANYTHING ELSE
The V3 timed-lead sheet only goes back to 10 Jun, so speed-to-lead and quality stats above cover
that window, not the full historical Facebook tab (1,259 rows back to mid-2025). One SVD site
visit (Naveen Suvarna, 27 Jun) couldn't be traced to a V3 timed lead — worth a quick manual check
on whether that's a pre-V3 lead or a logging gap, since if it's the latter it means the phone-match
rate above (95.1%) may be slightly overstated for the sheet as a whole.

**Data note:** `fetch_all.py` had two bugs fixed as part of this run — (1) `action_attribution_windows`
was using a deprecated request format that 400'd every single Meta Insights call, and (2) the
Google Sheets client object was being shared across threads, which isn't safe and reliably
corrupted the run. Both are fixed in the script; today's numbers are live, verified data.
