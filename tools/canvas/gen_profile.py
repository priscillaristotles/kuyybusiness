"""Pinned posts and story highlights for @kuyy.business, added to the existing canvas.

Pinned posts use the 12 locked feed layouts. Highlights need a 1080x1920 story format the
feed system does not have, so the story frames below extend it with the same tokens,
paper objects, marks and logo.
"""
import json, os, sys
import gen
from gen import e, lines, logo_top, CHECK, ARROW, RING, UNDER, photo, page, LAYOUTS, LOGO_W, LOGO_B

INDEX = sys.argv[1]          # the live project/canvas.json, read just before
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "canvas2", "project")
os.makedirs(OUT, exist_ok=True)

SW, SH = 1080, 1920

# ---------------- story frames (extension of the feed system) ----------------
# Safe zone: Instagram covers the top ~250px (progress bar, handle) and the bottom ~250px
# (reply bar). Logo sits inside it, top-centre at y=280; nothing that matters below y=1670.

def s_logo(g):
    return f'<img alt="Kuyy! Business" src="{LOGO_W if g=="blue" else LOGO_B}" style="position:absolute;left:380px;top:280px;width:320px;height:58px;display:block">'

def s_head(g, label, title, top=470, size=96):
    acc = "c-yellow" if g == "blue" else "c-blue"
    lab = "c-yellow" if g == "blue" else "c-blue"
    t = [e(x) for x in title]
    t[1] = f'<span class="{acc}">{t[1]}</span>'
    return (f'<div class="abs t-label {lab}" style="left:96px;top:{top}px">{e(label)}</div>'
            f'<div class="abs t-title" style="left:96px;top:{top+58}px;width:900px;font-size:{size}px">{"<br>".join(t)}</div>')

def checks(rows, size=36):
    return "".join(f'<div style="display:flex;gap:18px;align-items:flex-start;margin-top:24px">{CHECK}'
                   f'<span class="t-body c-ink" style="font-size:{size}px">{e(r)}</span></div>' for r in rows)

def link_zone(top, left=96, w=888, h=150):
    return (f'<div class="abs" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px;border:4px dashed #4a5060;opacity:.6;'
            f'display:flex;align-items:center;justify-content:center"><span class="t-caption c-soft">LINK STICKER · business.kuyy.id</span></div>')

def link_zone_blue(top):
    return (f'<div class="abs" style="left:96px;top:{top}px;width:888px;height:150px;border:4px dashed #ffffff;opacity:.7;'
            f'display:flex;align-items:center;justify-content:center"><span class="t-caption c-paper">LINK STICKER · business.kuyy.id</span></div>')

def cover(mark):
    if mark == "arrow":
        svg = (f'<svg class="mark y" viewBox="0 0 160 160" aria-hidden="true" style="left:290px;top:710px;width:500px;height:500px;'
               f'stroke-width:16;transform:rotate(8deg)">{ARROW}</svg>')
    elif mark == "ring":
        svg = (f'<svg class="mark y" viewBox="0 0 300 150" aria-hidden="true" style="left:240px;top:810px;width:600px;height:300px;'
               f'stroke-width:22;transform:rotate(-4deg)">{RING}</svg>')
    else:
        svg = ('<svg class="mark y" viewBox="0 0 100 100" aria-hidden="true" style="left:310px;top:730px;width:460px;height:460px;'
               'stroke-width:13"><path d="M12 54 L40 82 L90 16"></path></svg>')
    return "blue", svg

def h_what_1():
    g = "blue"
    return g, f'''{s_logo(g)}
{s_head(g, "Start here", ["Studio software", "with the customers", "built in."])}
<div class="paper" style="left:120px;top:1010px;width:840px;height:520px;transform:rotate(-2deg);padding:64px 64px 0">
<div class="t-lead" style="font-size:46px">Kuyy! Business runs your<br>bookings, payments<br>and members.</div>
<div class="hr" style="margin:40px 0 32px"></div>
<div class="t-body c-soft" style="font-size:34px">And lists your classes on the Kuyy! app.</div>
</div>'''

def h_what_2():
    g = "blue"
    return g, f'''{s_logo(g)}
{s_head(g, "Two things in one", ["Run your studio.", "Get found."], size=88)}
<div class="paper" style="left:96px;top:800px;width:888px;height:400px;transform:rotate(-1.5deg);padding:52px 56px 0">
<div class="t-label c-blue">Run your studio</div>
{checks(["Bookings and payments", "Passes, packs and vouchers", "QR check-in"])}
</div>
<div class="paper" style="left:96px;top:1250px;width:888px;height:400px;transform:rotate(1.2deg);padding:52px 56px 0">
<div class="t-label c-blue">Get found</div>
{checks(["Listed on the Kuyy! app", "300,000+ registered users", "50+ cities"])}
</div>'''

def h_what_3():
    g = "blue"
    return g, f'''{s_logo(g)}
<div class="abs t-label c-yellow" style="left:0;right:0;top:560px;text-align:center">On Kuyy! today</div>
<div class="abs t-hero c-yellow" style="left:0;right:0;top:640px;text-align:center">300,000+</div>
<svg class="mark y" viewBox="0 0 400 30" preserveAspectRatio="none" aria-hidden="true" style="left:190px;top:840px;width:700px;height:40px;transform:rotate(-1deg)">{UNDER}</svg>
<div class="abs t-headline" style="left:0;right:0;top:930px;text-align:center;font-size:64px">people signed up to book<br>in 50+ cities.</div>
<div class="paper" style="left:170px;top:1200px;width:740px;height:300px;transform:rotate(-2deg);padding:52px 56px 0">
<div class="t-lead" style="font-size:42px">Your studio can be one<br>search away from them.</div>
<div class="t-caption c-soft" style="margin-top:30px">Kuyy! registered users and cities, Sep 2026</div>
</div>'''

def invoice_story(no, title, items, pill):
    g = "blue"
    rows = "".join(f'<div class="row t-figure" style="padding:22px 0;border-bottom:3px solid #d5dce8"><span class="c-soft">{e(a)}</span><span>{e(b)}</span></div>' for a, b in items)
    return g, f'''{s_logo(g)}
<div class="paper" style="left:130px;top:470px;width:820px;height:900px;transform:rotate(-1.5deg);padding:64px 64px 0">
<div class="row"><span class="t-label c-blue">Invoice</span><span class="t-caption c-soft">{e(no)}</span></div>
<div class="hr" style="margin:26px 0 44px;background:#0054db;height:4px"></div>
<div class="t-title" style="font-size:76px">{lines(title)}</div>
<div style="margin-top:48px">{rows}
<div class="row" style="padding:26px 0 0"><span class="t-label">Total due</span><span class="t-title c-blue" style="font-size:100px">Rp 0</span></div>
</div>
<div style="position:absolute;left:64px;bottom:64px"><span class="pill">{e(pill)} <span aria-hidden="true">&rarr;</span></span></div>
<svg class="mark b" viewBox="0 0 300 150" preserveAspectRatio="none" aria-hidden="true" style="left:500px;top:{452 + 96*(len(items)-1)}px;width:290px;height:140px;transform:rotate(-2deg)">{RING}</svg>
</div>
{link_zone_blue(1440)}'''

def h_who_1():
    g = "mist"
    chips = "".join(f'<span class="chip" style="font-size:30px;padding:14px 22px">{e(c)}</span>' for c in
                    ["Yoga", "Pilates", "Aerial", "Padel", "Gym", "Wellness"])
    return g, f'''{s_logo(g)}
{s_head(g, "Who it's for", ["Built for studios", "that take bookings."], size=88)}
<div class="paper" style="left:96px;top:820px;width:888px;height:620px;transform:rotate(-1.5deg);padding:60px 60px 0">
<div class="t-label c-soft">Studios on Kuyy! Business</div>
<div class="hr" style="margin:22px 0 36px"></div>
<div style="display:flex;flex-wrap:wrap;gap:18px">{chips}</div>
<div class="t-lead" style="font-size:44px;margin-top:56px">From one room<br>to many branches.</div>
</div>'''

def h_who_2():
    g = "mist"
    def sheet(left, top, rot, name, price, rows, business):
        p = f'<span class="hl">{e(price)}</span>' if business else e(price)
        rule = 'background:#0054db;height:4px' if business else ''
        lab = "c-blue" if business else "c-soft"
        return (f'<div class="paper" style="left:{left}px;top:{top}px;width:430px;height:700px;transform:rotate({rot}deg);padding:50px 44px 0">'
                f'<div class="t-label {lab}">{e(name)}</div><div class="t-title" style="font-size:80px;margin-top:26px">{p}</div>'
                f'<div class="t-body c-soft" style="font-size:28px;margin-top:8px">a month</div>'
                f'<div class="hr" style="margin:32px 0 10px;{rule}"></div>{checks(rows, 31)}</div>')
    return g, f'''{s_logo(g)}
{s_head(g, "Which plan", ["Two plans.", "Pick by size."], size=88)}
{sheet(96, 800, -1.5, "Premium", "Rp 150K", ["Solo instructors", "One-room studios", "Owner at the desk"], False)}
{sheet(556, 790, 1.2, "Business", "Rp 699K", ["Multi-branch studios", "Staff on payroll", "Your own website"], True)}
<div class="abs t-caption c-soft" style="left:96px;top:1560px;width:900px">Yearly: Rp 135K and Rp 599K a month. Prices as of Oct 2026.</div>'''

def h_who_3():
    g = "mist"
    return g, f'''{s_logo(g)}
{photo("Photo · Priscilla at Samasta", "left:96px;top:470px;width:470px;height:600px;transform:rotate(-2.5deg);box-shadow:0 18px 40px rgba(10,14,26,.14)")}
<div class="abs t-label c-blue" style="left:640px;top:540px;width:360px;line-height:1.5">Built by people<br>who run studios</div>
<svg class="mark b" viewBox="0 0 160 160" preserveAspectRatio="none" aria-hidden="true" style="left:600px;top:640px;width:130px;height:130px;transform:rotate(208deg)">{ARROW}</svg>
<div class="paper" style="left:400px;top:900px;width:600px;height:600px;transform:rotate(1.5deg);padding:56px 56px 0">
<div class="t-quote" style="font-size:46px">I run 7 aerial studio<br>branches. This is the<br>system I wanted<br>for them.</div>
<div class="hr" style="margin:40px 0 26px"></div>
<div class="t-label">Priscilla Aristotles</div>
<div class="t-caption c-soft" style="margin-top:10px">CBO, KUYY! · FOUNDER,<br>SAMASTA AERIAL STUDIO</div>
</div>'''

def h_who_4():
    g = "mist"
    return g, f'''{s_logo(g)}
<div class="abs drop" style="left:80px;top:470px;width:920px;height:800px;transform:rotate(-1deg)">
<div class="paper" style="left:0;top:0;width:920px;height:800px;-webkit-mask:radial-gradient(circle 28px at 630px 0,#0000 98%,#000),radial-gradient(circle 28px at 630px 100%,#0000 98%,#000);-webkit-mask-composite:source-in;mask-composite:intersect;padding:84px 0 0 64px">
<div class="t-label c-blue">30-minute demo</div>
<div class="t-title" style="font-size:80px;margin-top:30px">Not sure<br>it fits? Ask.</div>
<div class="t-body c-soft" style="margin-top:34px;width:520px">Bring your class list.<br>We set it up live.</div>
<div class="abs" style="left:64px;bottom:72px"><span class="pill">Book a demo <span aria-hidden="true">&rarr;</span></span></div>
<div class="abs" style="left:630px;top:44px;bottom:44px;border-left:4px dashed #d5dce8"></div>
<div class="abs t-caption c-soft" style="left:671px;top:330px;width:208px;text-align:center">TAP THE<br>LINK BELOW</div>
</div>
</div>
{link_zone(1380)}'''

def h_does_1():
    g = "blue"
    steps = ["Take bookings and payments online.", "Sell passes, packs and vouchers.",
             "Check members in by QR.", "Get listed on the Kuyy! app."]
    rows = "".join(f'<div style="display:flex;gap:28px;align-items:center"><span class="num">{i+1:02d}</span>'
                   f'<span class="t-body c-soft" style="font-size:36px">{e(s)}</span></div><div class="hr" style="margin-left:92px"></div>'
                   for i, s in enumerate(steps))
    return g, f'''{s_logo(g)}
<div class="paper" style="left:150px;top:470px;width:780px;height:1000px;transform:rotate(1.5deg);padding:96px 64px 0">
<div class="abs" style="left:0;right:0;top:40px;height:3px;background:#0054db;opacity:.5"></div>
<div class="abs" style="left:0;right:0;top:50px;height:3px;background:#0054db;opacity:.5"></div>
<div class="t-title" style="font-size:80px">What you<br>can do</div>
<div style="margin-top:64px;display:flex;flex-direction:column;gap:30px">{rows}</div>
</div>
<svg class="mark y" viewBox="0 0 160 160" preserveAspectRatio="none" aria-hidden="true" style="left:60px;top:1480px;width:130px;height:130px;transform:rotate(8deg)">{ARROW}</svg>'''

def phone_story(title, tags, screen):
    g = "blue"
    return g, f'''{s_logo(g)}
<div class="abs t-title" style="left:0;right:0;top:450px;text-align:center;font-size:84px">{e(title[0])}<br><span class="c-yellow">{e(title[1])}</span></div>
<div class="abs" style="left:355px;top:720px;width:370px;height:780px;border-radius:58px;background:#0a0e1a;padding:16px;box-shadow:0 26px 50px rgba(0,20,70,.35)">
<div style="width:100%;height:100%;border-radius:44px;overflow:hidden"><div class="photo"><span>{e(screen)}</span></div></div>
</div>
<svg class="mark y" viewBox="0 0 1080 1920" aria-hidden="true" style="left:0;top:0;width:1080px;height:1920px;stroke-width:5"><path d="M300 862 H360"></path><path d="M780 1052 H720"></path><path d="M318 1262 H360"></path></svg>
<div class="paper t-label c-blue" style="left:88px;top:830px;padding:18px 24px;transform:rotate(-2deg)">{e(tags[0])}</div>
<div class="paper t-label c-blue" style="left:780px;top:1020px;padding:18px 24px;transform:rotate(2deg)">{e(tags[1])}</div>
<div class="paper t-label c-blue" style="left:106px;top:1230px;padding:18px 24px;transform:rotate(-1deg)">{e(tags[2])}</div>'''

# ---------------- the set ----------------

PINNED = [
 {"id": "pin1", "ground": "blue", "name": "Pinned 1 · What Kuyy! Business is", "slides": [
   ("MathCover", {"label": "Start here · Kuyy! Business", "h": ["Booking software", "that also sends", "you customers?"],
      "header": "KUYY! BUSINESS · WHAT YOU GET", "rows": [("Bookings", "yes"), ("Payments", "yes"), ("App listing", "yes")],
      "total": "Rp 0", "total_label": "To start"}),
   ("LedgerCompare", {"title": ["Booking software,", "with demand built in."], "cols": ["Booking-only", "Kuyy!"],
      "rows": [("Takes bookings", "Yes", "Yes"), ("Takes payments", "Yes", "Yes"), ("App listing", "No", "Yes")],
      "total": ("Who can find you", "300,000+"),
      "source": ["Booking-only: studio software with no consumer app.", "Kuyy! registered users, Sep 2026."]}),
   ("ClipboardSteps", {"title": ["How to", "start"], "steps": [
      "Sign up at business.kuyy.id.", "Add your classes, passes and prices.",
      "Take bookings and payments for 30 days.", "Pick a plan on day 30, or leave."]}),
   ("InvoiceCta", {"no": "KUYY! BUSINESS · NO. 000", "title": ["Your first month", "is on us."],
      "items": [("30-day free trial", "Rp 0")], "total": "Rp 0", "pill": "Start free trial"}),
  ],
  "caption": "What Kuyy! Business is: studio software for bookings, payments and members, plus a listing on the Kuyy! app. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "Swap the QR for the trial page. 'Pick a plan on day 30, or leave' assumes no auto-billing after the trial: confirm."},
 {"id": "pin2", "ground": "mist", "name": "Pinned 2 · Who it's for", "slides": [
   ("PriceSheet", {"title": ["Built for", "studio owners."], "prices": ["Rp 150K", "Rp 699K"],
      "premium": ["Solo instructors", "One-room studios", "Owner at the desk"],
      "business": ["Multi-branch studios", "Staff on payroll", "Your own website"],
      "source": "Yearly: Rp 135K and Rp 599K a month. Prices as of Oct 2026."})],
  "caption": "For yoga, pilates, aerial, padel, gym and wellness studios, from one room to many branches. Start free trial at business.kuyy.id #kuyybusiness",
  "check": "Confirm list prices. This overlaps feed post 21 (same plan-fit rows): swap 21 for another price angle, or skip it."},
 {"id": "pin3", "ground": "blue", "name": "Pinned 3 · What you can do", "hold": True, "slides": [
   ("ProductScreen", {"title": ["Book. Get paid.", "Check them in."], "tags": ["Class bookings", "Auto-verified", "QR check-in"],
      "screen": "Real screenshot · studio dashboard"})],
  "caption": "Take bookings, get paid automatically, sell passes and check members in by QR, all in one app. Book a demo at business.kuyy.id #kuyybusiness",
  "check": "HOLD: needs a real app screenshot (member names blurred)."},
]

HIGHLIGHTS = [
 {"id": "h1", "name": "Highlight 1 · Start here (what it is)", "mark": "arrow",
  "frames": [h_what_1, h_what_2, h_what_3,
             lambda: invoice_story("NO. 001 · DUE DAY 30", ["Try it on your", "real classes."], [("30-day free trial", "Rp 0")], "Start free trial")],
  "note": "Highlight title: Start here\nCover: the arrow mark.\nStory 4: put an Instagram link sticker in the dashed box, linking to the trial page."},
 {"id": "h2", "name": "Highlight 2 · Who it's for", "mark": "ring",
  "frames": [h_who_1, h_who_2, h_who_3, h_who_4],
  "note": "Highlight title: Who it's for\nCover: the ring mark.\nStory 2: confirm prices on the day. Story 3: Priscilla approves her words and supplies the photo. Story 4: link sticker to the demo page."},
 {"id": "h3", "name": "Highlight 3 · What it does", "mark": "check", "hold": True,
  "frames": [h_does_1,
             lambda: phone_story(["Take bookings.", "Get paid."], ["Schedule", "Auto-verified", "Seating plan"], "Real screenshot · schedule"),
             lambda: phone_story(["Sell passes.", "See who's coming."], ["Class pack", "Voucher code", "QR check-in"], "Real screenshot · passes"),
             lambda: invoice_story("NO. 002 · DUE DAY 30", ["Your first month", "is on us."], [("30-day free trial", "Rp 0")], "Start free trial")],
  "note": "Highlight title: What it does\nCover: the check mark.\nHOLD: stories 2 and 3 need real app screenshots. Story 4: link sticker to the trial page."},
]

# ---------------- write files + merge into the live index ----------------

idx = json.load(open(INDEX))
PAGE = {"id": "p0", "name": "Profile · pinned + highlights"}
assert all(p["id"] != "p0" for p in idx["pages"]), "profile page already exists"
idx["pages"] = [PAGE] + idx["pages"]
idx["launch"] = {"view": "canvas", "page": "p0"}

written = []
def add(name, title, ground, body, x, y, w, h):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(page(title, ground, body, w, h))
    idx["boards"][name] = {"x": x, "y": y, "w": w, "h": h, "title": title, "page": "p0"}
    idx["order"].append(name)
    written.append(name)

GAP, TITLE = 80, 300
y = TITLE
idx["notes"]["pT"] = {"x": 0, "y": y - 250, "text": "Pinned posts · top row of the grid, left to right", "kind": "title1",
                      "maxW": 6 * 1080 + 5 * GAP, "page": "p0"}
x = 0
for pin in PINNED:
    for i, (layout, data) in enumerate(pin["slides"]):
        ground, body = LAYOUTS[layout](data)
        assert ground == pin["ground"]
        n = len(pin["slides"])
        title = f"{pin['name']} · slide {i+1}" if n > 1 else pin["name"]
        add(f"{pin['id']}-{i+1}-{layout.lower()}.dc.html", title, ground, body, x, y, 1080, 1350)
        x += 1080 + GAP
    idx["notes"][f"n{pin['id']}"] = {"x": x - 1080 - GAP, "y": y + 1350 + 40, "w": 1080, "maxH": 700, "page": "p0",
        "fill": "orange" if pin.get("hold") else "green", "size": "m",
        "text": f"{pin['name'].upper()}\nCAPTION\n{pin['caption']}\n\nBEFORE POSTING\n{pin['check']}"}
y += 1350 + 900 + TITLE
for h in HIGHLIGHTS:
    idx["notes"][f"t{h['id']}"] = {"x": 0, "y": y - 250, "text": h["name"], "kind": "title1",
                                   "maxW": 5 * SW + 4 * GAP, "page": "p0"}
    g, body = cover(h["mark"])
    add(f"{h['id']}-0-cover.dc.html", f"{h['name']} · cover", g, body, 0, y, SW, SH)
    for i, fn in enumerate(h["frames"]):
        g, body = fn()
        add(f"{h['id']}-{i+1}-story.dc.html", f"{h['name']} · story {i+1}", g, body, (i + 1) * (SW + GAP), y, SW, SH)
    idx["notes"][f"n{h['id']}"] = {"x": 5 * (SW + GAP), "y": y, "w": 760, "maxH": 1200, "page": "p0",
        "fill": "orange" if h.get("hold") else "green", "size": "l", "text": h["note"]}
    y += SH + 120 + TITLE

with open(os.path.join(OUT, "canvas.json"), "w") as f:
    json.dump(idx, f, ensure_ascii=False, indent=1)
print(json.dumps({f"project/{n}": f"project/{n}" for n in written}))
