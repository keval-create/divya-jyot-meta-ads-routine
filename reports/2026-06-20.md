# Divya Jyot LYF — Daily Quality Audit: June 20, 2026

**₹267 cost-per-site-visit yesterday — 2 confirmed visits logged while team's Facebook lead log is 8 months out of date. Quality blind spot is the main problem today.**

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

**SVD visits logged on June 20:**
- **Manjulamahida** (9619289985) — 1 BHK, budget ₹90L
- **Sandeep shah** (8850364329) — 1 BHK, budget ₹1cr

**Lead quality from team sheet:** ⚠️ **CANNOT ASSESS** — the Facebook lead log (Google Sheet) stops at October 2025. All ~225 leads generated in the last 30 days, including yesterday's 15, have no feedback data. Match rate for June 2026 leads: **0%** — not because they're bad leads, but because the team hasn't logged them.

---

## 2. Quality by Source

Single active configuration: **"Studio" ad → "Open - DJR" adset → "Divya Jyot V3 June26"** campaign. No creative split to compare within the account.

**Luxury - DJ adset:** ₹7.76 spent over 30 days, 0 leads. Dormant — not pulling budget.

**What the SVD tab tells us about recent Facebook lead quality:**
- June 19: Swati wankhede — 1 BHK, **budget ₹60L** (too low, ₹87L studio won't fit)
- June 20: Manjulamahida — 1 BHK, budget ₹90L (borderline, studio is ₹87L)
- June 20: Sandeep shah — 1 BHK, budget ₹1cr (fits well)

**1 of 3 recent visitors is clearly budget-mismatched.** The other 2 are plausible buyers.

---

## 3. Real Cost Per Site Visit

| Window | Spend | SVD Visits (Facebook) | Cost/Visit |
|---|---|---|---|
| Yesterday (Jun 20) | ₹533.95 | 2 | **₹267** |
| 7-day (Jun 14–20) | ₹4,199.17 | 2 | ₹2,100 |
| 30-day (May 22–Jun 20) | ₹8,344 | 3 | ₹2,781 |

*Vanity CPL (30-day): ₹37.05 — cost-per-visit is 75× higher, as expected.*

The yesterday figure (₹267) is exceptional but should be read cautiously — those 2 visitors likely responded to ads from earlier days, not yesterday's exact ₹534 spend. The 30-day figure (₹2,781/visit) is more reliable as a structural cost.

**For a ₹87L product, ₹2,781 per site visit is defensible** if visit-to-booking conversion holds.

---

## 4. Trend

- **CTR:** 3.05% (30-day avg) → 2.26% (yesterday). Slight dip; still healthy for real estate.
- **CPL:** ₹37.05 (30-day) → ₹35.60 (yesterday). Slight improvement.
- **Frequency:** 2.46 over 30 days. Rising but still below 3 — audience not yet fatigued.
- **SVD visits:** 0 for most of May 2026, then 3 visits in 2 days (Jun 19–20). This kind of burst pattern is normal; no trend signal yet.
- **V3 OTP form quality verdict:** Cannot be measured. The team sheet doesn't have June 2026 lead data. The question of whether higher-intent forms are trading volume for quality is unanswerable right now.

Historical reference from 2025 data: the old leads showed ~20–25% warm/HOT rate by label, but most eventually went dead on budget mismatch or location mismatch. The ₹87L studio product has a narrow buyer profile.

---

## 5. Recommendations (Ranked)

**1. Fix the data gap — this is urgent.**
The Google Sheet's Facebook tab caps at row 300, last entry October 2025. Eight months of leads are invisible. Options:
- Extend the fetch range in `fetch_all.py` from `Facebook!A1:N300` to `Facebook!A1:N1000`
- Or confirm the team has stopped logging there and find where they're recording new leads.
Without this, the quality audit has no data to work with.

**2. Don't reduce spend — CPL looks fine and site visits are materialising.**
₹35.60 CPL with confirmed same-day SVD visits is performing. The knee-jerk of "CPL is low, cut budget" would be wrong. The Studio ad is delivering.

**3. Add a budget qualifier to the lead form if not already there.**
The OTP form was meant to filter quality — but Swati (₹60L) still got through. If the form doesn't ask "what's your budget?", add it. A ₹60L lead cannot buy this studio. Every such visit wastes the sales team's time.

**4. Get a revisit commitment from Sandeep shah (₹1cr) and Manjulamahida (₹90L).**
Both visited yesterday. Sandeep's budget fits. Manjula's is borderline (₹3L gap). Both should be called today for status — hot leads go cold in 48 hours.

---

*Single campaign active: Divya Jyot V3 June26 / Studio ad / Open - DJR adset. No other campaigns in spend window.*
*Sheet match rate for June 2026 leads: 0% due to data gap — quality numbers above are SVD-tab only, not cross-referenced from Facebook tab.*
