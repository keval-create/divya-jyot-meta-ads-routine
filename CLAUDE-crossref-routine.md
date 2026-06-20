# Daily Cross-Reference Routine — Divya Jyot LYF Rewa (7 PM)

## What this routine does
Every evening you read `data.json` (Meta Ads spend + the team's Google Sheet),
CROSS-REFERENCE the two, and email Keval a detailed report on lead QUALITY and what
to change. This is not a spend dashboard — it's a quality audit that connects ad money
to real downstream outcomes.

## Critical business context
- Product: BARE SHELL studio, ₹87 lakh, Mulund West, 5 min from MG Road station.
- The REAL metric is **cost per site visit** and **warm-lead rate**, NOT CPL.
  A high CPL is fine if those leads are high intent and convert to visits.
  NEVER recommend pausing an ad on CPL alone.
- The core historical problem: ~1,200 past leads, only ~2.3% warm, ~4.5% did site
  visits. Most recorded "purchases" were in other locations entirely. The V3 strategy
  (OTP-verified higher-intent form) deliberately trades lead volume for lead quality.
  Your whole job is to measure whether that trade is working.

## The data you have
- `data.json > meta` — yesterday + 7-day + 30-day spend, leads, CPL, CTR, frequency by
  campaign / adset / ad.
- `data.json > sheet.facebook_tab` — incoming leads the team logs: Created, Name, Email,
  Phone, Status, Feedback, and multiple follow-up columns (free text like "Ringing",
  "Not interested", "Details share Visit Done 2/8/25", "Budget 1cr he want 439 sqft").
- `data.json > sheet.svd_tab` — confirmed site visits: Source, Name, Number, Visit Date,
  Req Flat, Remarks.

## How to cross-reference
1. **Match leads by phone number** between Meta's lead count and the Facebook tab.
   Phones may differ in formatting (+91, spaces, .0 suffixes) — normalise to last 10 digits.
2. **Read the free-text feedback with judgment.** Do NOT rely on rigid status labels.
   Infer intent: "Visit Done", "coming Sunday", "Prospective", "budget matches" = warm/hot.
   "Not interested", "fake no", "wrong number", "invalid", "out of service",
   "time pass" = dead. "Ringing", "busy", "switch off" repeatedly = unreachable.
3. **Find who reached the SVD tab** — those are the real conversions that matter.
4. **Compute the numbers that actually matter:**
   - Real cost per site visit = ad spend / number of leads that became SVD visits.
   - Warm-lead rate = warm leads / total leads.
   - Unreachable rate, fake/invalid rate.
   - Which CAMPAIGN / ADSET / AD the warm leads and visits came from (trace quality back
     to creative + audience, not just volume).

## The report (email body)
Keep it scannable, blunt, mobile-first. Structure:
1. **Headline** — the one thing that matters most today.
2. **Yesterday's spend vs quality** — spend, raw leads, CPL, BUT immediately followed by
   warm-lead count, unreachable/fake count, and any site visits logged. The contrast is
   the point.
3. **Quality by source** — which ad / adset produced the GOOD leads vs the junk. This is
   the most valuable section: "Studio video ad → 4 leads, 2 warm, 1 visit booked.
   Image 2 ad → 3 leads, all unreachable. Kill Image 2."
4. **Real cost per site visit** — the true efficiency number, vs the vanity CPL.
5. **Trend** — is quality improving since the OTP form went live, or just volume dropping?
6. **2-4 ranked recommendations** — concrete, framed as suggestions not auto-actions.
   Tie each to evidence from the cross-reference.

## Tone & rules
- Direct, data-grounded, "so what" framing. Keval knows the domain — use the vocabulary.
- No corporate filler, no "hope this finds you well." Lead with the answer.
- If the sheet data is stale (team hasn't updated), SAY SO — don't invent quality data.
- If phone matching is weak (few matches), report the match rate honestly so Keval knows
  how much to trust the quality read.
- Never fabricate. If you can't tell a lead's quality from the feedback, count it as
  "unclassified" rather than guessing.

## Delivery
Email to keval@divyajyotprojects.in via the configured email connector at 7 PM IST.
Subject: "Meta + CRM Daily — [headline in 5-7 words]"
