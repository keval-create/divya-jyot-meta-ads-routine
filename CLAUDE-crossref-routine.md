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
Called hours later -> they've moved on. Speed-to-lead is the team's single biggest
controllable lever, and you measure it.

Data for this:
- `data.json > meta_leads.leads` — each Meta lead with `created_time_ist` (exact arrival,
  to the second), `phone10` (last 10 digits), and name.
- `data.json > sheet.facebook_tab` — where the team logs the lead + first follow-up notes.
- `data.json > sheet.revisions` — Google Drive revision timeline: a list of {id,
  modifiedTime} marking when batches of edits were saved to the sheet. COARSE — see
  `revisions_note`. Use it to bound when a row was first worked, to within a few minutes.

How to estimate response time per lead:
1. Take a fresh Meta lead: arrival = `created_time_ist`, phone = `phone10`.
2. Find that phone in the Facebook tab (match on last 10 digits).
3. Estimate when the team first WORKED that row. Two signals, use whichever is available:
   (a) Times the team wrote into their own notes ("called 13:52", dated follow-ups) —
       explicit, trust these first.
   (b) The revision `modifiedTime` closest to (but after) the lead's arrival, as a proxy
       for when the row was created / first edited.
4. Response lag = first-contact time minus arrival time.

Report it like a manager would:
- **Average first-response time** for yesterday's fresh leads.
- **Fastest and slowest** specific examples with actual clock times
  ("13:45 arrival -> 13:51 first call, 6 min OK" / "11:20 arrival -> next-day, BAD").
- **How many leads waited too long** (>30 min, >2 hours, next-day). These are the leads
  most likely lost to slow follow-up while the OTP-warm window was still open.
- If the team is consistently fast, SAY SO plainly — credit good work, don't manufacture
  problems. If consistently slow, name it and tie it to lost warm leads.
- Be honest about precision: if you're inferring contact time from coarse revisions rather
  than explicit notes, say the timing is approximate. Never invent a response time you
  can't support — mark it "unknown" instead.

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
