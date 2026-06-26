# Divya Jyot LYF Rewa — Daily Snapshot
**Report date: 26 Jun 2026 (~7 PM IST) | Primary window: today (midnight–~7 PM IST)**
*First run — no prior reports to compare against. _memory.md created fresh below.*

---

## ⚠️ CRITICAL: META ADS API RETURNING 400 ERRORS

All Meta API calls (today, yesterday, last-7, last-30 — every level: campaign/adset/ad) returned HTTP 400 Bad Request. **No spend, impressions, CTR, CPC, CPM, frequency, or CPL data is available for this report.**

This is likely a revoked or expired API access token. The Meta ad account token needs to be refreshed in the repo secrets (META_ADS_TOKEN env var) before the next run will show ad performance data.

**Impact:** Cannot compute CPL, cost-per-site-visit, CTR trends, or frequency for this report. All funnel numbers below are drawn from the Google Sheet only.

---

## 1. HEADLINE

2 IG leads today, both already contacted — and **Priya says she's coming Saturday.** That's the one bright spot. The Meta Ads API is completely dark (400 error, token likely expired), and all 4 confirmed site visitors from this campaign want 1BHK/2BHK — not the studio. The product mismatch is the #1 issue, not speed-to-lead.

---

## 2. THE FUNNEL (today so far, midnight–~7 PM IST)

**Meta Ads data: UNAVAILABLE (API 400)**
Spend, impressions, reach, clicks, CPL: unknown.

**From the V3 CRM Event sheet (what we can see):**

| Stage | Today (26 Jun) | Yesterday (25 Jun) | Last 7 days (20–26 Jun) |
|---|---|---|---|
| Leads in | 2 | 3 | 14 |
| Platform | 2 IG | 2 FB, 1 IG | Mix |
| Contacted same-day | 2 / 2 ✅ | 3 / 3 ✅ | Yes |
| Site visits logged | 0 | 0 | 4 (all on 24 Jun) |

**Today's 2 leads (both IG, both 3–6 months intent):**
- **Rashmi** (9820723248) — 10:00 AM IST. Feedback: "Looking for 1bhk, budget not disclosed, details shared." Status: Cold.
- **Priya** (7208141086) — 2:17 PM IST. Feedback: "Looking for 2bhk, budget not disclosed. **She will come Saturday.**" Status: Cold.

Both contacted within hours of arriving. Speed is good. But both said 1BHK/2BHK — product mismatch on first call.

**Campaign total since June 10 launch:**
- Total leads: **62** (from V3 CRM Event sheet)
- Campaign: Divya Jyot V3 June26
- Paused: June 22 (Meta account-security flag) — 0 leads that day ✅ confirmed
- Resumed: June 23 — 4 leads June 23, 7 on June 24 (post-resume spike)
- Platform: 34 FB (55%), 28 IG (45%)
- Intent: 33 within_3_months (53%), 16 three-to-6-months (26%), 13 just_exploring (21%)

---

## 3. AD PERFORMANCE (agency hat)

**Data unavailable — Meta API 400 error.**

What is known contextually:
- Campaign was paused June 22 for a Meta account-security flag. The budget-threshold protection was set and delivery resumed June 23.
- Post-resume delivery looks healthy from the lead volume (7 leads on June 24, strongest single day since launch).
- Pre-pause: June 10 produced 13 leads (launch day spike), then 2–7/day through June 21.
- No CTR, CPM, frequency, or creative fatigue data available without API access.

**Action required immediately:** Refresh META_ADS_TOKEN so the next run can pull actual ad metrics.

---

## 4. SPEED-TO-LEAD (sales-manager hat)

**Verdict: EXCELLENT on first contact. Gap problem on follow-up cadence for June 10–14 leads.**

**Today's leads:** Both contacted same-day within hours of arriving. Rashmi (10 AM) and Priya (2:17 PM) both have feedback logged in the sheet already. This is the right behavior for OTP-verified leads. Credit to the team.

**Yesterday's leads (3 leads):**
- Mitesh Shah (midnight, 3–6 months): Voicemail June 25 → Ringing June 26. Being worked.
- Rajesh Kothari (3 AM, within_3_months): Out of service June 25 → Out of service June 26. High-intent lead with dead number. Flag it.
- Vivek Dwivedi (7:43 AM, within_3_months): Called June 25, disclosed "1RK budget 60L" → Dead. Resolved same-day. Fine.

**Within-3-months leads contacted same-day but never reconnected (CRITICAL MISSES):**
These OTP-verified high-intent leads had an initial call attempt but then faced a 7-8 day gap before follow-up:
- **milind** (June 10, 11:25 AM) — Called June 10 (busy), June 10-11 (no answer), then nothing until June 18. Now 16 days old, still just ringing. Window almost certainly closed.
- **Madhukar Bhavsar** (June 10, 11:58 AM) — Same pattern: June 10 attempts, then June 18 restart. 16 days, out of service.
- **Daniel Sapurkar** (June 10, 6:45 PM) — Ringing since June 10. 16 days. No conversation ever.
- **Vipul Rakhasia** (June 10, 6:50 PM) — Said "coming today evening" on June 10. Then disappeared. Has been ringing since June 18. Classic ghost.
- **Pravin Bhuingal** (June 17, 12:02 PM) — 9 days, ringing throughout. No conversation.
- **Jaideep Salunke** (June 17, 1:26 PM) — 9 days, out of service / ringing. No conversation.
- **Vishram Kudalkar** (June 19, 11:08 PM) — 7 days, ringing. No conversation.
- **Himalaya Agrawal** (June 19, 11:25 PM) — 7 days, ringing. No conversation.

**The gap: June 10 leads were called June 10–11, then not again until June 18 (7-day blackout).** For "within_3_months" OTP-verified leads, that gap is too long. These 4 June-10 leads with high intent are now likely gone.

**Cross-intent speed check:** The worst miss is **Vipul Rakhasia** — within_3_months, explicitly said "coming today evening" on June 10, then vanished. If the team had followed up within 24–48 hours instead of waiting until June 18, there was a real chance of rescuing a same-day site visit.

**Sandeep Shah (9223200118, June 14, just_exploring)** is marked WARM — "1RK budget 87L, coming next Thursday." That "Thursday" was June 19–21. His last 4 follow-ups (June 18, 19, 20, 21) are all "Ringing." He has gone silent. Most likely got cold or picked another project. This is the only WARM lead in the system. Need to escalate with a WhatsApp message — not just calls.

---

## 5. LEAD QUALITY (sales-manager hat)

**62 total leads, 57 matched to Facebook tab. Quality breakdown:**

**Dead / Clearly unqualified (won't convert):** ~18 leads (29%)
- Wrong location: Reema P. Desai (wants Kandivali/Borivali), Anant (CP Thane), nehal mota (Dombivali), Manal/unmatched (Dombivali)
- Wrong type + way below budget: Shraddha (1BHK ₹55L), Atul (1RK ₹30L), Aparna (1RK ₹55L), Sudarshan (1RK ₹50L), Vivek Dwivedi (1RK ₹60L)
- Rental seeker: Suman Yadav
- Invalid/accidental: Norwin Saloman (invalid), Naresh Sachade (by mistake)
- Not interested: Sailee Joag, Neeraj, Kiran Dharamshi (spoke to Keval, not interested)
- Unreachable dead: Noorjaha Shaikh

**Product mismatch but budget OK (will visit wrong project):** ~20 leads (32%)
These leads want 1BHK or 2BHK with decent budgets (80L–1.4CR) — the campaign is bringing in buyers for a different product category. They're visiting but can't buy what's being sold.
Notable: Shweta Singh (1BHK ₹80L), Bhakti Bhanushali (1BHK ₹85L), Christina Dias (2BHK ₹1.5CR), Soni Karan (2BHK), NIKHIl (1BHK), Ashok Patel (2BHK/broker), Dhiraj Dand (wants ₹20k/sqft), Chandrashekhar (1BHK ₹85L), Gaykawad Sushant (1BHK ₹85L), Shradha Mhamunkar (2BHK ₹1.4CR)

**Still being worked / no disqualifier confirmed yet:** ~15 leads (24%)
The team is calling but hasn't reached them. Include: Milind, Madhukar, Daniel, Deepali, Vipul Rakhasia, Pravin, Jaideep, Vishram, Himalaya, Shersingh, Vikas Kamble, Akshay Wagh, Mitesh Shah, Rajesh Kothari, Vanita Gala, Vishram, Himalaya

**Warm / visit-ready:** 2 leads (3%)
- **Sandeep Shah** (9223200118, June 14): 1RK ₹87L, WARM status — perfect match but has gone silent
- **Priya** (7208141086, June 26, today): Says "coming Saturday" — follow up at 9 AM tomorrow to confirm

**Site visits confirmed:** 4 (6.5% of 62 leads)
- Swati Wankhede: Visited June 19. Budget ₹60L max, wants 1BHK. Mismatch — confirmed.
- Manjula Mahida: Visited June 20. Budget ₹1CR, wants 1BHK (439 sqft). Budget is right, product is wrong.
- Sandeep Shah (8850364329): Visited June 20. Budget ₹1CR, wants 1BHK. Budget fine, product wrong.
- Rewashankar Gomtiwal: Visited June 24 (same-day lead!). Budget undisclosed, wants 2BHK. Wrong product.

**Site visit rate: 6.5% vs historical baseline 4.5% — V3 IS beating baseline on volume.**
**But zero of 4 visitors are matched to the studio product.** Real cost-per-quality-visit is unknown (no spend data), but the visits aren't converting to serious buyers for an 87L studio.

**Dominant quality leak:** The creative/targeting is attracting 1BHK and 2BHK seekers. The studio (bare shell, ₹87L) is attracting curious viewers but the intent-to-buy this specific product is low.

---

## 6. DIAGNOSTIC STEPS (ranked)

**1. Fix Meta API token NOW — agency critical**
Without spend data, we're flying blind. Token refresh needed in repo secrets. Every day without it means no CTR, no frequency, no budget optimization signal. Priority: tonight.

**2. WhatsApp the WARM lead Sandeep Shah (9223200118) — sales, today**
He said 1RK ₹87L and "coming next Thursday" (June 18–21). Four call attempts since then, all ringing. He hasn't picked up but he hasn't blocked either. A WhatsApp message — "Hi Sandeep, just a reminder the studio at Mulund West is still available at ₹87L. Would love to show you this week" — has better odds than another unanswered call.

**3. Confirm Priya's Saturday visit (7208141086) — sales, tomorrow morning**
She said "coming Saturday" (June 27) but wants 2BHK. Budget not disclosed. A call or WhatsApp by 9 AM Saturday to confirm + do pre-qualification (budget, timeline) will determine if it's worth preparing the site. If budget is strong (90L+), she may be persuadable on studio vs 1BHK.

**4. Stop calling the June 10 ghost leads after 7+ attempts — sales, cleanup**
Milind, Madhukar, Daniel Sapurkar, Vipul Rakhasia — 16 days, 6–8 attempts each, no contact. These are done. One final WhatsApp message to each and then archive. Freeing up the team's time for June 23–26 leads which still have a window.

**5. Creative brief: add "studio / 1RK" language explicitly — agency**
The dominant quality leak (1BHK/2BHK seekers) suggests the creative says "flat in Mulund" without being specific about studio/1RK. When the API is back, check if FB vs IG has different mismatch rates. Consider testing an ad with "India's most affordable studio — ₹87L, Mulund West" in the headline to pre-filter 1BHK/2BHK seekers. V3 form gives intent, but better to screen at the creative stage.

---

## 7. ANYTHING ELSE

**The Rewashankar miracle:** Rewashankar Gomtiwal came in as a lead at 12:37 PM on June 24 and visited the site the SAME AFTERNOON. That's the fastest possible conversion — lead to visit in hours. He wants a 2BHK and the project can't serve him, but the team's response speed on June 24 was exceptional. This should be the model: new lead in, call within the hour, push for same-week visit.

**Parnav Shah (old lead, SVD visit June 24):** An old September 2025 Facebook lead (2BHK, ₹1.7CR) who showed up for a site visit on June 24. No information on whether this visit progressed. Worth a follow-up call — someone who remembers an ad from 9 months ago and walks in is a serious buyer. But the 2BHK requirement can't be served.

**Swati Wankhede's SVD note (26/6 follow-up):** "Not interested." She visited June 19, budget ₹60L max. Now confirmed dead. Clean close.

**Manjula Mahida (SVD, 26/6 follow-up):** "Final budget 90 lakhs and he want 439." The studio is ₹87L — this is 3L above his stated max. This is the closest any visitor has come to matching. Worth one more pitch: "At ₹87L, you get a bare-shell studio where you design your own interior — here's what the 439 sqft layout looks like."

---

*Next run: pull this report to track whether Priya visited Saturday and whether Sandeep Shah responded to WhatsApp. Fix Meta API token before next run.*
