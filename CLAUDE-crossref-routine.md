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
- `data.json > sheet.facebook_tab` — the team's full lead log, diligently maintained.
  IMPORTANT STRUCTURE: this sheet has MULTIPLE campaign sections stacked vertically,
  separated by banner rows like "20/01/2026 New Advertisement". Leads run from mid-2025
  through the current week. Columns: row#, Created date, Name (often with BHK/req noted),
  Email, Phone, Status (Cold/Warm/Hot/Dead/etc.), then Feedback + up to 8 dated follow-up
  columns containing free-text call notes. Date formats are inconsistent (DD/MM/YYYY,
  M/D/YYYY, typos like "02/09/2525") — parse defensively.
- `data.json > sheet.svd_tab` — confirmed site visits: Source, Name, Number, Visit Date,
  Req Flat, Remarks.

## How to cross-reference
1. **Match leads by phone number** between Meta's lead count and the Facebook tab.
   Phones vary in formatting (+91, spaces, leading digits, ".0", concatenated like
   "9321110668 / 8369593191", country-code prefixes) — normalise to last 10 digits.
2. **Read the free-text feedback with judgment** — the team writes natural notes, not
   rigid labels. The Status column is their own call (Cold/Warm/Hot/Dead) but the real
   signal is in the follow-up text. Infer intent:
   - WARM/HOT signals: "Visit Done", "coming Sunday/tomorrow", "site visit planning",
     budget that fits ₹87L (e.g. "budget 1cr", "90 lakhs", "85 lakhs"), "Details shared"
     followed by engagement, revisit.
   - DEAD signals: "Not interested", "wrong no/invalid", "out of service", "Looking for
     [other location]" (Ghatkopar, Navi Mumbai, Dadar, rental, MP/Bihar/other states),
     "low budget" (anything well under ₹80L for the studio), "rental enquiry", "broker",
     "Muslim client" (note: team uses this as a dead-tag — treat as dead, do not comment).
   - UNREACHABLE: repeated "Ringing", "Busy", "Voicemail", "switch off".
3. **Recognise the budget-mismatch pattern** — a huge share of dead leads are people
   wanting OTHER locations or with budgets far below ₹87L, OR wanting 2BHK at 1.4cr+ that
   this project can't serve. This is the dominant quality problem. Quantify it.
4. **Find who reached the SVD tab** — those are the real conversions that matter.
5. **Compute the numbers that actually matter:**
   - Real cost per site visit = ad spend / number of leads that became SVD visits.
   - Warm-lead rate = warm leads / total leads (for the recent window, e.g. last 30 days).
   - Unreachable rate, dead-on-location rate, low-budget rate.
   - Which CAMPAIGN / ADSET / AD the warm leads and visits trace back to.

## NEW — Speed-to-lead (you are now the team's manager, not just an ad auditor)
You also monitor how fast the sales team responds to fresh leads. The premise: a lead who
just did OTP verification has their phone in hand. Called within minutes -> they answer.
Called hours/days later -> they've moved on. Speed-to-lead is the team's single biggest
controllable lever, and you measure it.

Data for this:
- `data.json > sheet.meta_leads_timed` — every Meta lead with EXACT arrival time already
  converted to IST (`created_time_ist`), plus `phone10` (last 10 digits), `name`,
  `platform` (fb/ig), `intent` (the form answer: within_3_months / 3-6_months /
  just_exploring — a direct intent signal), and the ad/adset/campaign it came from.
  (This comes from the V3 CRM Event sheet that Pabbly populates — exact, reliable.)
- `data.json > sheet.facebook_tab` — where the team logs the lead + dated follow-up notes.

How to estimate response time per lead:
1. Take a lead from `meta_leads_timed`: arrival = `created_time_ist`, phone = `phone10`.
2. Find that phone in the Facebook tab (match on last 10 digits).
3. Estimate when the team FIRST contacted it, from the team's dated follow-up notes
   (e.g. "13/06/26", "called 13:52", first dated entry in the follow-up columns). The team
   writes dates, sometimes times — use the earliest contact evidence you can find.
4. Response lag = first-contact − arrival. Day-level if only dates are logged; finer if
   times are written. Be explicit about which precision you have.

What the data already suggests (verify each run): leads arriving early June were often not
first-contacted for 3-8 days. If real, that's warm leads going cold while the OTP window
(minutes-to-hours) is wide open. This is the highest-value thing you monitor.

Report it like a manager would:
- **Average first-response time** for the recent leads you can match.
- **Fastest and slowest** named examples with actual dates/times.
- **How many leads waited too long** (>1 day, >3 days). Tie slow response to lost warm leads.
- **Cross intent with speed**: a `within_3_months` lead left for 5 days is a worse miss than
  a `just_exploring` one. Flag high-intent leads that got slow follow-up specifically.
- If the team is fast, SAY SO and credit it. If slow, name it directly. Never invent a
  response time you can't support from the data — mark it "unknown".

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
After you finish writing the report, save it as a Markdown file in the `reports/`
folder of this repo, named by date: `reports/YYYY-MM-DD.md` (use yesterday's date).
Then commit it back to the repository so Keval can read it anytime.
Format in clean Markdown — bold headers, short bullets, scannable on mobile.
Start with a one-line headline. Keep it tight — quality over length.
Also overwrite `reports/latest.md` with the same content so the most recent
report is always at a predictable path.
