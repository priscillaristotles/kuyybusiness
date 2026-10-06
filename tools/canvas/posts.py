DEMO = ("DemoTicket", {"label": "30-minute demo", "title": ["See it on your", "own schedule."],
                       "body": ["Bring your class list.", "We set it up live."]})

def demo(title, body):
    return ("DemoTicket", {"label": "30-minute demo", "title": title, "body": body})

def case(n, label_h, facts, photo, unit, lead, source, qrole, qdetail, qphoto, demo_slide):
    return [
        ("CaseFileCover", {"label": f"Studio case · {n:02d}", "h": label_h, "facts": facts, "photo": photo}),
        ("StatCards", {"before": "[n]", "after": "[n]", "unit": unit, "months": ["[MON YYYY]", "[MON YYYY]"],
                       "lead": lead, "source": source}),
        ("QuoteNote", {"quote": ["[Their words,", "lightly edited,", "approved by", "them.]"], "name": "[Name]",
                       "role": qrole, "detail": qdetail, "photo": qphoto}),
        demo_slide,
    ]

FOUNDER_ROLE = ["CBO, KUYY! · FOUNDER,", "SAMASTA AERIAL STUDIO"]
PRICE_SRC_SEP = "Yearly: Rp 135K and Rp 599K a month. Prices as of Sep 2026."
PRICE_SRC_OCT = "Yearly: Rp 135K and Rp 599K a month. Prices as of Oct 2026."

POSTS = [
 {"n": 1, "date": "Mon 28 Sep", "ground": "mist", "name": "FounderNote · why a studio owner helped build this",
  "slides": [("FounderNote", {"label": ["From the team", "that runs studios"],
     "note": ["I almost built my", "own studio software.", "Then I found Kuyy!", "and joined them."],
     "name": "Priscilla Aristotles", "role": FOUNDER_ROLE, "photo": "Photo · Priscilla at Samasta"})],
  "caption": "Why a studio owner ended up building studio software instead of buying it. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "Priscilla approves the words. Swap in a real photo."},

 {"n": 2, "date": "Tue 29 Sep", "ground": "blue", "name": "BigNumber · 300,000+ registered users",
  "slides": [("BigNumber", {"label": "On Kuyy! today", "number": "300,000+",
     "line": ["people signed up to book", "in 50+ cities."], "lead": ["Your studio can be one", "search away from them."],
     "source": "Kuyy! registered users and cities, Sep 2026"})],
  "caption": "300,000+ people already use the Kuyy! app to find their next class. Start free trial at business.kuyy.id #kuyybusiness"},

 {"n": 3, "date": "Wed 30 Sep", "ground": "mist", "name": "PriceSheet · two plans, prices in full",
  "slides": [("PriceSheet", {"title": ["Two plans.", "Prices in full."], "prices": ["Rp 150K", "Rp 699K"],
     "premium": ["Verified studio badge", "Unlimited memberships and vouchers", "Instant withdrawal"],
     "business": ["Everything in Premium", "Website builder", "Staffing and payroll"], "source": PRICE_SRC_SEP})],
  "caption": "Both plans, priced in full, with 30 days free to start. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "Confirm list prices on the day."},

 {"n": 4, "date": "Thu 01 Oct", "ground": "blue", "name": "The math · bank VA and e-wallet fees", "hold": True,
  "slides": [
   ("MathCover", {"label": "The math · payment fees", "h": ["50 bank transfers.", "How much goes", "to fees?"],
      "header": "YOUR STUDIO · OCT 2026", "rows": [("Payments", "50"), ("Fee each", "?"), ("Month total", "?")], "total": "Rp ?",
      "total_label": "You pay"}),
   ("LedgerCompare", {"title": ["50 payments a month,", "paid by bank transfer."], "cols": ["Public rate", "Kuyy!"],
      "rows": [("Per payment", "Rp 13,000", "Rp 2,500"), ("50 a month", "Rp 650,000", "Rp 125,000"), ("12 months", "Rp 7.8M", "Rp 1.5M")],
      "total": ("Kept a year", "+Rp 6.3M"),
      "source": ["Source: Xendit public bank VA rate, [month year].", "Kuyy! Business bank VA fee, Sep 2026."]}),
   ("LedgerCompare", {"title": ["Rp 300K class pack,", "paid by e-wallet."], "cols": ["Public rate", "Kuyy!"],
      "rows": [("Per payment", "Rp 11,500", "Rp 7,000"), ("50 a month", "Rp 575,000", "Rp 350,000"), ("12 months", "Rp 6.9M", "Rp 4.2M")],
      "total": ("Kept a year", "+Rp 2.7M"),
      "source": ["Source: Xendit public e-wallet rate, 2.5% + Rp 4,000,", "[month year]. Kuyy! e-wallet fee, Sep 2026."]}),
   ("InvoiceCta", {"no": "KUYY! BUSINESS · NO. 004", "title": ["Try it on your", "own payments."],
      "items": [("30-day free trial", "Rp 0")], "total": "Rp 0", "pill": "Start free trial"}),
  ],
  "caption": "Fees on 50 bank transfers and 50 e-wallet payments, worked out. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "HOLD: confirm whether the studio or the participant pays the Rp 2,500. Re-check Xendit's VA and e-wallet public rates and fill in [month year]. Swap the QR."},

 {"n": 5, "date": "Fri 02 Oct", "ground": "mist", "name": "Studio case 01 · Samasta Aerial", "hold": True,
  "slides": case(1, ["Samasta Aerial moved", "7 branches to one", "system in [X] weeks."],
     [("TYPE", "Aerial"), ("BRANCHES", "7"), ("CITIES", "4")], "Photo · a class at a Samasta branch",
     "[unit, e.g. hours a week on payment checks]", ["[Why it changed,", "in 2 short lines.]"],
     ["Samasta Aerial's own booking data, [months].", "Shared with permission."],
     "[ROLE] · SAMASTA AERIAL", "On Kuyy! Business since [Mon YYYY].", "Photo · the team member", DEMO),
  "caption": "How Samasta Aerial runs 7 branches on one system. Photos and data shared with permission by Samasta Aerial. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: one before/after metric from Samasta's data with written OK, a branch photo, a quote from a Samasta team member (ask: what stopped being your problem after the move?). Confirm all 7 branches are on Kuyy! Business."},

 {"n": 6, "date": "Sat 03 Oct", "ground": "blue", "name": "ProductScreen · dashboard overview", "hold": True,
  "slides": [("ProductScreen", {"title": ["Every booking,", "one screen."], "tags": ["Schedule", "Payments", "Passes"],
     "screen": "Real screenshot · dashboard day view"})],
  "caption": "Schedule, payments and passes on one dashboard. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: real screenshot of the dashboard day view, member names blurred."},

 {"n": 7, "date": "Sun 04 Oct", "ground": "mist", "name": "FounderNote · built for how Indonesian studios run",
  "slides": [("FounderNote", {"label": ["Built in Indonesia", "for Indonesian studios"],
     "note": ["Overseas tools didn't", "fit our studios. So", "we helped build one", "that does."],
     "name": "Priscilla Aristotles", "role": FOUNDER_ROLE, "photo": "Photo · Priscilla at a front desk"})],
  "caption": "Made for how Indonesian studios take bookings and payments. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "Priscilla approves the words. Use a different photo from post 01."},

 {"n": 8, "date": "Mon 05 Oct", "ground": "blue", "name": "BigNumber · 4,000+ communities",
  "slides": [("BigNumber", {"label": "Already on Kuyy!", "number": "4,000+",
     "line": ["communities host", "activities on Kuyy!"], "lead": ["Their members already", "know how to book here."],
     "source": "Kuyy! public numbers, communities, Sep 2026"})],
  "caption": "4,000+ communities already run their activities on the Kuyy! app. Start free trial at business.kuyy.id #kuyybusiness"},

 {"n": 9, "date": "Tue 06 Oct", "ground": "mist", "name": "PriceSheet · yearly prices",
  "slides": [("PriceSheet", {"title": ["Yearly costs", "less a month."], "prices": ["Rp 135K", "Rp 599K"],
     "premium": ["Billed once a year", "Advanced analytics", "Priority support"],
     "business": ["Billed once a year", "Everything in Premium", "Class scheduling"],
     "source": "Monthly: Rp 150K and Rp 699K. Yearly prices as of Sep 2026."})],
  "caption": "Pay yearly and each month costs less. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "Confirm list prices on the day."},

 {"n": 10, "date": "Wed 07 Oct", "ground": "blue", "name": "The math · how the free month works",
  "slides": [
   ("MathCover", {"label": "The math · free trial", "h": ["30 days free.", "What happens", "on day 31?"],
      "header": "YOUR STUDIO · TRIAL", "rows": [("Days 1 to 30", "Rp 0"), ("From day 31", "?"), ("Yearly plan", "?")],
      "total": "Rp ?", "total_label": "You pay"}),
   ("ClipboardSteps", {"title": ["How the free", "month works"], "steps": [
      "Sign up for Kuyy! Business and add classes.", "Take real bookings and payments for 30 days.",
      "Check your fees and hours saved.", "Pick Premium or Business on day 30."]}),
   ("InvoiceCta", {"no": "NO. 010 · DUE DAY 30", "title": ["Your first month", "is on us."],
      "items": [("Days 1 to 30", "Rp 0")], "total": "Rp 0", "pill": "Start free trial"}),
  ],
  "caption": "30 days free, then choose a plan. Go yearly within 30 days and you pay for 10 months and get 12. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "Confirm the 12-for-10 offer is live and which rate it bills at. Swap the QR."},

 {"n": 11, "date": "Thu 08 Oct", "ground": "mist", "name": "Studio case 02 · pilates studio", "hold": True,
  "slides": case(2, ["[Studio] [result]", "[result, cont.]", "in [time span]."],
     [("TYPE", "Reformer Pilates"), ("CITY", "[City]"), ("ON KUYY! SINCE", "[Mon YYYY]")], "Photo · the studio in use",
     "app bookings a month", ["[Why it changed,", "in 2 short lines.]"],
     ["[Studio]'s own booking data, [months].", "Shared with permission."],
     "OWNER · [STUDIO]", "On Kuyy! Business since [Mon YYYY].", "Photo · the owner",
     demo(["Fill the classes", "you already run."], ["We show you how members", "find you on the app."])),
  "caption": "[Studio], [city]: [result in one line]. Shared with permission by [Studio]. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: find a pilates studio with 3+ months on Kuyy! Business that will share one metric in writing. Ask the owner: where do your new members come from now?"},

 {"n": 12, "date": "Fri 09 Oct", "ground": "blue", "name": "ProductScreen · auto-verified payments", "hold": True,
  "slides": [("ProductScreen", {"title": ["No more checking", "transfer proofs."], "tags": ["Auto-verified", "Bank · e-wallet", "Withdraw now"],
     "screen": "Real screenshot · verified payment"})],
  "caption": "Payments confirm themselves, so the front desk stops matching screenshots. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: real screenshot of a verified payment. If the account is not on Premium, change the Withdraw now tag to QRIS."},

 {"n": 13, "date": "Sat 10 Oct", "ground": "mist", "name": "FounderNote · 7 branches, one system",
  "slides": [("FounderNote", {"label": ["From the team", "that runs studios"],
     "note": ["I run 7 aerial studio", "branches. This is the", "system I wanted", "for them."],
     "name": "Priscilla Aristotles", "role": FOUNDER_ROLE, "photo": "Photo · Priscilla at a third branch"})],
  "caption": "7 branches, 4 cities, one system. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "Use a photo from a different branch than posts 01 and 07."},

 {"n": 14, "date": "Sun 11 Oct", "ground": "blue", "name": "BigNumber · 400,000+ activities",
  "slides": [("BigNumber", {"label": "On Kuyy! so far", "number": "400,000+",
     "line": ["activities hosted", "on Kuyy!"], "lead": ["Your members book the", "same way they already do."],
     "source": "Kuyy! public numbers, activities, Sep 2026"})],
  "caption": "400,000+ activities hosted on the Kuyy! app so far. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "Confirm 'activities' means sessions hosted, not listings or bookings."},

 {"n": 15, "date": "Mon 12 Oct", "ground": "mist", "name": "PriceSheet · what each plan adds",
  "slides": [("PriceSheet", {"title": ["What each", "plan adds."], "prices": ["Rp 150K", "Rp 699K"],
     "premium": ["Seating plan", "Credits pass", "Recurring classes"],
     "business": ["Class scheduling", "Website builder", "Staffing and payroll"], "source": PRICE_SRC_OCT})],
  "caption": "Seating plans on Premium, payroll on Business. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "Confirm list prices on the day."},

 {"n": 16, "date": "Tue 13 Oct", "ground": "blue", "name": "The math · hours lost to transfer checks",
  "slides": [
   ("MathCover", {"label": "The math · admin time", "h": ["How many hours", "do transfer proofs", "cost you?"],
      "header": "FRONT DESK · LAST MONTH", "rows": [("Transfers", "?"), ("Minutes each", "?"), ("Hours a month", "?")],
      "total": "? hours", "total_label": "You lose"}),
   ("ClipboardSteps", {"title": ["Work out", "your hours"], "steps": [
      "Count last month's bank transfers.", "Time how long 1 check takes.",
      "Multiply them, then divide by 60.", "Kuyy! Business verifies each one for you."]}),
   ("InvoiceCta", {"no": "NO. 016 · DEMO", "title": ["Watch a payment", "confirm itself."],
      "items": [("30-minute demo", "Rp 0")], "total": "Rp 0", "pill": "Book a demo"}),
  ],
  "caption": "Work out how many hours you spend checking transfers by hand. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "Swap the QR for the demo booking page."},

 {"n": 17, "date": "Wed 14 Oct", "ground": "mist", "name": "Studio case 03 · yoga studio", "hold": True,
  "slides": case(3, ["[Studio] cut", "[admin task] by [X]", "in [time span]."],
     [("TYPE", "Yoga"), ("CITY", "[City]"), ("ROOMS", "[n]")], "Photo · the studio in use",
     "[hours a week on admin]", ["[Why it changed,", "in 2 short lines.]"],
     ["[Studio]'s own data, [months].", "Shared with permission."],
     "OWNER · [STUDIO]", "On Kuyy! Business since [Mon YYYY].", "Photo · the owner",
     demo(["See your week", "set up live."], ["Bring last month's", "schedule. We rebuild it."])),
  "caption": "[Studio], [city]: [result]. Shared with permission by [Studio]. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: a yoga studio with an operational metric (admin hours, or no-shows before and after QR check-in). Ask: what do you do with the time you got back?"},

 {"n": 18, "date": "Thu 15 Oct", "ground": "blue", "name": "ProductScreen · QR check-in", "hold": True,
  "slides": [("ProductScreen", {"title": ["Scan in.", "Class starts."], "tags": ["QR check-in", "E-ticket", "Live attendance"],
     "screen": "Real screenshot · QR check-in"})],
  "caption": "Members scan in with their e-ticket and attendance updates as they arrive. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: real screenshot of the QR scanner or an attendance list."},

 {"n": 19, "date": "Fri 16 Oct", "ground": "mist", "name": "FounderNote · co-founder note",
  "slides": [("FounderNote", {"label": ["From the team", "that builds it"],
     "note": ["Studio owners tell us", "what breaks. We ship", "the fix, then ask", "what's next."],
     "name": "[William full name]", "role": ["[ROLE], KUYY!", ""], "photo": "Photo · William"})],
  "caption": "Built with studio owners' feedback. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "Draft only: William rewrites or approves. Confirm his full name and role."},

 {"n": 20, "date": "Sat 17 Oct", "ground": "blue", "name": "BigNumber · 50+ cities",
  "slides": [("BigNumber", {"label": "Where Kuyy! is used", "number": "50+",
     "line": ["cities with people", "booking on Kuyy!"], "lead": ["Opening a new branch?", "The app is already there."],
     "source": "Kuyy! public numbers, cities, Sep 2026"})],
  "caption": "Kuyy! is already in 50+ Indonesian cities, including the one your next branch opens in. Start free trial at business.kuyy.id #kuyybusiness"},

 {"n": 21, "date": "Sun 18 Oct", "ground": "mist", "name": "PriceSheet · which plan fits you",
  "slides": [("PriceSheet", {"title": ["Which plan", "fits you."], "prices": ["Rp 150K", "Rp 699K"],
     "premium": ["Solo instructors", "One-room studios", "Owner at the desk"],
     "business": ["Multi-branch studios", "Staff on payroll", "Your own website"], "source": PRICE_SRC_OCT})],
  "caption": "Premium for one room, Business for a team. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "Confirm list prices. Check the fit rows with sales."},

 {"n": 22, "date": "Mon 19 Oct", "ground": "blue", "name": "The math · flash sale for empty spots", "hold": True,
  "slides": [
   ("MathCover", {"label": "The math · empty spots", "h": ["4 empty spots", "at 7 AM earn", "nothing."],
      "header": "7 AM CLASS · 8 SPOTS", "rows": [("Booked", "4"), ("Empty", "4"), ("Empty earns", "Rp 0")], "total": "Rp ?"}),
   ("ClipboardSteps", {"title": ["How flash", "sale works"], "steps": [
      "Pick the class and the spots to release.", "Set your own discount.",
      "Set when the sale opens and closes.", "Every other spot keeps its full price."]}),
   ("InvoiceCta", {"no": "KUYY! BUSINESS · NO. 022", "title": ["Sell the spot", "you'd lose."],
      "items": [("Regular price", "unchanged"), ("30-minute demo", "Rp 0")], "total": "Rp 0", "pill": "Book a demo"}),
  ],
  "caption": "Release only the spots that would go empty, at a discount you set. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: confirm flash sale is live in production and the 4 steps match the shipped feature. Needs Priscilla's sign-off (not in the feed guideline)."},

 {"n": 23, "date": "Tue 20 Oct", "ground": "mist", "name": "Studio case 04 · padel or gym", "hold": True,
  "slides": case(4, ["[Studio] [result]", "[result, cont.]", "in [time span]."],
     [("TYPE", "Padel"), ("CITY", "[City]"), ("COURTS", "[n]")], "Photo · a match or the front desk",
     "[court bookings a month]", ["[Why it changed,", "in 2 short lines.]"],
     ["[Studio]'s own booking data, [months].", "Shared with permission."],
     "OWNER · [STUDIO]", "On Kuyy! Business since [Mon YYYY].", "Photo · the owner",
     demo(["Courts, classes,", "one schedule."], ["Bring your booking list.", "We set it up live."])),
  "caption": "[Studio], [city]: [result]. Shared with permission by [Studio]. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: a padel club or boutique gym willing to share one metric. Ask: what did you use before, and what changed at the desk?"},

 {"n": 24, "date": "Wed 21 Oct", "ground": "blue", "name": "ProductScreen · memberships, packs, vouchers", "hold": True,
  "slides": [("ProductScreen", {"title": ["Passes, packs", "and vouchers."], "tags": ["Membership", "Class pack", "Voucher code"],
     "screen": "Real screenshot · pass setup"})],
  "caption": "Set up memberships, class packs and voucher codes in minutes. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: real screenshot of the pass setup. Time the setup; cut 'in minutes' if it takes longer."},

 {"n": 25, "date": "Thu 22 Oct", "ground": "mist", "name": "FounderNote · who answers when you message us",
  "slides": [("FounderNote", {"label": ["Who answers when", "you message us"],
     "note": ["Most questions come", "in before the first", "class. So we start", "early too."],
     "name": "[Name]", "role": ["STUDIO SUPPORT, KUYY!", "[CITY]"], "photo": "Photo · the support person"})],
  "caption": "The team that picks up when your studio messages us. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "Draft only: the support person rewrites it. Keep 'we start early' only if support hours start before morning classes."},

 {"n": 26, "date": "Fri 23 Oct", "ground": "blue", "name": "BigNumber · 30-day free trial",
  "slides": [("BigNumber", {"label": "Free trial", "number": "30 days",
     "line": ["to run your studio", "on Kuyy! first."], "lead": ["Real bookings, real", "payments, before you pay."],
     "source": "Kuyy! Business trial terms, Sep 2026"})],
  "caption": "Run your real classes on Kuyy! for 30 days before you pay anything. Start free trial at business.kuyy.id #kuyybusiness"},

 {"n": 27, "date": "Sat 24 Oct", "ground": "mist", "name": "PriceSheet · prices in full, no commission", "hold": True,
  "slides": [("PriceSheet", {"title": ["Prices in full.", "No commission."], "prices": ["Rp 150K", "Rp 699K"],
     "premium": ["0% booking commission", "Unlimited memberships and vouchers", "Instant withdrawal"],
     "business": ["0% booking commission", "Everything in Premium", "Staffing and payroll"], "source": PRICE_SRC_OCT})],
  "caption": "A flat monthly price with no cut of your bookings. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "HOLD: confirm zero booking commission on both plans. Confirm list prices."},

 {"n": 28, "date": "Sun 25 Oct", "ground": "blue", "name": "The math · what Premium needs to pay for itself",
  "slides": [
   ("MathCover", {"label": "The math · Premium", "h": ["Rp 150K a month.", "How many bookings", "pay for it?"],
      "header": "PREMIUM · MONTHLY", "rows": [("Plan", "Rp 150,000"), ("Class price", "?"), ("Bookings needed", "?")],
      "total": "? bookings", "total_label": "You need"}),
   ("ClipboardSteps", {"title": ["Work out", "your number"], "steps": [
      "Start with Rp 150,000, the Premium price.", "Divide by your drop-in price.",
      "Round up. That's your break-even.", "Compare it to 1 week of bookings."]}),
   ("InvoiceCta", {"no": "KUYY! BUSINESS · NO. 028", "title": ["Test it before", "you pay Rp 150K."],
      "items": [("Days 1 to 30", "Rp 0"), ("From day 31", "Rp 150,000")], "total": "Rp 0", "pill": "Start free trial"}),
  ],
  "caption": "Work out how many bookings cover Premium. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "Confirm the Premium price. Swap the QR."},

 {"n": 29, "date": "Mon 26 Oct", "ground": "mist", "name": "Studio case 05 · second-city studio", "hold": True,
  "slides": case(5, ["[Studio] [result]", "[result, cont.]", "in [time span]."],
     [("TYPE", "[Vertical]"), ("CITY", "[City]"), ("ON KUYY! SINCE", "[Mon YYYY]")], "Photo · the studio in use",
     "[new members from the app]", ["[Why it changed,", "in 2 short lines.]"],
     ["[Studio]'s own booking data, [months].", "Shared with permission."],
     "OWNER · [STUDIO]", "On Kuyy! Business since [Mon YYYY].", "Photo · the owner",
     demo(["Wherever your", "studio is."], ["Demos run online.", "Bring your class list."])),
  "caption": "[Studio], [city]: [result]. Shared with permission by [Studio]. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: a studio outside Jakarta. Ask: what was hard about running a studio in [city] before? Confirm demos run online."},

 {"n": 30, "date": "Tue 27 Oct", "ground": "blue", "name": "ProductScreen · seating plan", "hold": True,
  "slides": [("ProductScreen", {"title": ["Members pick", "their own spot."], "tags": ["Seating plan", "Spot picker", "No double-booking"],
     "screen": "Real screenshot · seating plan"})],
  "caption": "Members choose their reformer or bike when they book. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: real screenshot of the seating plan. Keep 'No double-booking' only if the screen shows it; else use 'Recurring class'."},
]


# ---- Revision, Oct 2026: Priscilla's story moves to pinned post 2 (the brand story).
# The feed's founder notes now feature other studio founders, and case 01 is no longer Samasta.

def other_founder(n, date, angle, label, ask, caption_topic):
    return {"n": n, "date": date, "ground": "mist", "name": f"FounderNote · studio founder · {angle}", "hold": True,
            "slides": [("FounderNote", {"label": label,
                "note": ["[Their words,", "2 sentences or", "fewer, approved", "by them.]"],
                "name": "[Founder name]", "role": ["FOUNDER,", "[STUDIO], [CITY]"],
                "photo": "Photo · the founder at their studio"})],
            "caption": f"[Founder] of [Studio], [city], on {caption_topic}. Shared with permission. Book a demo at business.kuyy.id #kuyybusiness",
            "check": f"HOLD: a studio founder on Kuyy! Business, their photo and their written OK. Ask: {ask}"}

_REVISED = {
 1: other_founder(1, "Mon 28 Sep", "why they started", ["From a studio", "founder on Kuyy!"],
                  "why did you start your studio?", "why they started their studio"),
 5: {"n": 5, "date": "Fri 02 Oct", "ground": "mist", "name": "Studio case 01 · [studio]", "hold": True,
     "slides": case(1, ["[Studio] [result]", "[result, cont.]", "in [time span]."],
        [("TYPE", "[Vertical]"), ("CITY", "[City]"), ("ON KUYY! SINCE", "[Mon YYYY]")], "Photo · the studio in use",
        "[unit, same on both cards]", ["[Why it changed,", "in 2 short lines.]"],
        ["[Studio]'s own booking data, [months].", "Shared with permission."],
        "FOUNDER · [STUDIO]", "On Kuyy! Business since [Mon YYYY].", "Photo · the founder", DEMO),
     "caption": "[Studio], [city]: [result in one line]. Shared with permission by [Studio]. Book a demo at business.kuyy.id #kuyybusiness",
     "check": "HOLD: a studio other than Samasta (Samasta's story is pinned post 2). One metric with written OK, a photo, a founder quote."},
 7: other_founder(7, "Sun 04 Oct", "the hard part", ["From a studio", "founder on Kuyy!"],
                  "what is the hardest part of running your studio week to week?", "the hardest part of running a studio"),
 13: other_founder(13, "Sat 10 Oct", "advice", ["From a studio", "founder on Kuyy!"],
                   "what would you tell someone opening their first studio?", "what they'd tell a first-time owner"),
}
POSTS = [_REVISED.get(p["n"], p) for p in POSTS]
