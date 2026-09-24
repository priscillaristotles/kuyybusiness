import json, html, os, datetime

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "canvas")
PROJ = os.path.join(ROOT, "project")
os.makedirs(PROJ, exist_ok=True)

LOGO_W = "/_blob/a5a22b6446ccbf923dfab0c1ecac0fe1"
LOGO_B = "/_blob/a85ddb95c889ea78c0df9c199a9defca"
DS = "ds/kuyybusinessfeed"

def e(s):
    return html.escape(s, quote=False)

def lines(xs):
    return "<br>".join(e(x) for x in xs)

CLIP = ('<svg viewBox="0 0 96 120" aria-hidden="true" style="width:96px;height:120px">'
        '<path d="M31 72 L22 10 Q48 -2 74 10 L65 72" fill="none" stroke="#B9C1CF" stroke-width="6" stroke-linejoin="round"></path>'
        '<path d="M8 66 H88 L80 118 H16 Z" fill="#0A0E1A"></path>'
        '<rect x="6" y="60" width="84" height="12" rx="3" fill="#262C3D"></rect></svg>')

def clip(x):
    return f'<div class="clip" style="left:{x}px;top:188px">{CLIP}</div>'

def rail():
    return '<div class="rail" style="top:250px"></div>'

def logo_top(g):
    return f'<img class="logo-top" alt="Kuyy! Business" src="{LOGO_W if g=="blue" else LOGO_B}">'

def logo_br(g):
    return f'<img class="logo-br" alt="Kuyy! Business" src="{LOGO_W if g=="blue" else LOGO_B}">'

RING = ('<path d="M170 16 C70 6 12 40 16 80 C22 126 150 138 244 120 C302 108 298 42 222 22 C190 14 150 14 116 22"></path>')
UNDER = '<path d="M6 22 C110 8 260 6 394 16"></path>'
ARROW = '<path d="M18 142 C28 76 66 42 132 30"></path><path d="M100 12 L134 30 L110 60"></path>'
CHECK = ('<svg viewBox="0 0 100 100" aria-hidden="true" style="width:30px;height:30px;flex:none;fill:none;stroke:#0054db;'
         'stroke-width:14;stroke-linecap:round;stroke-linejoin:round;transform:translateY(4px)"><path d="M12 54 L40 82 L90 16"></path></svg>')

def photo(label, style):
    return f'<div class="print" style="{style}"><div class="photo"><span>{e(label)}</span></div></div>'

# ---------------- layouts ----------------

def math_cover(p):
    teeth = ",".join(f"{i*12}px {14 if i%2==0 else 0}px" for i in range(51))
    rows = "".join(
        f'<div class="row t-figure" style="margin-top:{0 if i==0 else 26}px"><span>{e(a)}</span><span class="lead-dots"></span><span>{e(b)}</span></div>'
        for i,(a,b) in enumerate(p["rows"]))
    return "blue", f'''{logo_top("blue")}
<div class="abs t-label c-yellow" style="left:96px;top:238px">{e(p["label"])}</div>
<div class="abs t-headline" style="left:96px;top:290px;width:900px"><div>{e(p["h"][0])}</div><div class="c-yellow">{e(p["h"][1])}</div><div>{e(p["h"][2])}</div></div>
<div class="abs drop" style="left:240px;top:600px;width:600px;height:760px;transform:rotate(-3deg)">
<div class="paper" style="left:0;top:0;width:600px;height:760px;clip-path:polygon({teeth},600px 760px,0px 760px);padding:64px 56px 0">
<div class="t-caption c-soft" style="text-align:center">{e(p["header"])}</div>
<div class="hr-dash" style="margin:24px 0 30px"></div>
{rows}
<div class="hr-dash" style="margin:34px 0 30px"></div>
<div class="row"><span class="t-label">{e(p.get("total_label","You receive"))}</span><span class="t-headline" style="font-size:64px">{e(p["total"])}</span></div>
<svg class="mark b" viewBox="0 0 300 150" preserveAspectRatio="none" aria-hidden="true" style="left:348px;top:346px;width:240px;height:132px;transform:rotate(-2deg)">{RING}</svg>
</div>
</div>'''

def ledger(p):
    cells = ""
    for (lab,a,b) in p["rows"]:
        bd = "border-bottom:3px solid #d5dce8"
        cells += (f'<div class="t-body c-ink" style="padding:26px 0;{bd}">{e(lab)}</div>'
                  f'<div class="t-figure c-soft" style="font-size:30px;padding:28px 0 26px 20px;{bd}">{e(a)}</div>'
                  f'<div class="t-figure c-ink" style="font-size:30px;padding:28px 0 26px 20px;{bd}">{e(b)}</div>')
    return "blue", f'''{rail()}
<div class="paper" style="left:72px;top:272px;width:936px;height:900px;transform:rotate(-1deg);padding:72px 64px 0 96px">
<div class="abs" style="left:64px;top:0;bottom:0;width:3px;background:#0054db;opacity:.55"></div>
<div class="abs" style="left:72px;top:0;bottom:0;width:3px;background:#0054db;opacity:.55"></div>
<div class="t-title" style="font-size:64px;line-height:1.05">{lines(p["title"])}</div>
<div style="display:grid;grid-template-columns:1.5fr 1fr 1fr;margin-top:48px;column-gap:0">
<div class="t-label c-soft" style="padding:14px 0">&nbsp;</div>
<div class="t-label c-soft" style="padding:14px 0 14px 20px;background:#f2f5fa">{e(p["cols"][0])}</div>
<div class="t-label c-blue" style="padding:14px 0 14px 20px;background:#e6eefb">{e(p["cols"][1])}</div>
{cells}
<div class="t-body c-ink" style="padding:30px 0;font-weight:700">{e(p["total"][0])}</div>
<div class="t-figure" style="padding:32px 0 0 20px">&nbsp;</div>
<div class="t-figure c-ink" style="padding:32px 0 0 20px;font-weight:500"><span class="hl">{e(p["total"][1])}</span></div>
</div>
<div class="t-caption c-soft" style="position:absolute;left:96px;right:64px;bottom:56px">{lines(p["source"])}</div>
</div>
{clip(252)}{clip(732)}
{logo_br("blue")}'''

def steps(p):
    rows = ""
    for i,s in enumerate(p["steps"]):
        rows += (f'<div style="display:flex;gap:28px;align-items:center"><span class="num">{i+1:02d}</span>'
                 f'<span class="t-body c-soft" style="font-size:36px">{e(s)}</span></div><div class="hr" style="margin-left:92px"></div>')
    return "blue", f'''{rail()}
<div class="paper" style="left:150px;top:272px;width:780px;height:880px;transform:rotate(1.5deg);padding:96px 64px 0">
<div class="abs" style="left:0;right:0;top:40px;height:3px;background:#0054db;opacity:.5"></div>
<div class="abs" style="left:0;right:0;top:50px;height:3px;background:#0054db;opacity:.5"></div>
<div class="t-title" style="font-size:80px">{lines(p["title"])}</div>
<div style="margin-top:64px;display:flex;flex-direction:column;gap:30px">{rows}</div>
</div>
{clip(492)}
<svg class="mark y" viewBox="0 0 160 160" preserveAspectRatio="none" aria-hidden="true" style="left:60px;top:1150px;width:130px;height:130px;transform:rotate(8deg)">{ARROW}</svg>
{logo_br("blue")}'''

def invoice(p):
    items = "".join(
        f'<div class="row t-figure" style="padding:22px 0;border-bottom:3px solid #d5dce8"><span class="c-soft">{e(a)}</span><span>{e(b)}</span></div>'
        for a,b in p["items"])
    arrow = '<span aria-hidden="true">&rarr;</span>'
    return "blue", f'''{rail()}
<div class="paper" style="left:130px;top:272px;width:820px;height:900px;transform:rotate(-1.5deg);padding:64px 64px 0">
<div class="row"><span class="t-label c-blue">Invoice</span><span class="t-caption c-soft">{e(p["no"])}</span></div>
<div class="hr" style="margin:26px 0 44px;background:#0054db;height:4px"></div>
<div class="t-title" style="font-size:76px">{lines(p["title"])}</div>
<div style="margin-top:48px">{items}
<div class="row" style="padding:26px 0 0"><span class="t-label">Total due</span><span class="t-title c-blue" style="font-size:100px">{e(p["total"])}</span></div>
</div>
<div style="position:absolute;left:64px;right:64px;bottom:64px;display:flex;align-items:center;justify-content:space-between">
<span class="pill">{e(p["pill"])} {arrow}</span>
<div class="qr" style="width:170px;height:170px">QR</div>
</div>
<svg class="mark b" viewBox="0 0 300 150" preserveAspectRatio="none" aria-hidden="true" style="left:500px;top:{548 + 96*(len(p["items"])-2)}px;width:290px;height:140px;transform:rotate(-2deg)">{RING}</svg>
</div>
{clip(492)}
{logo_br("blue")}'''

def case_cover(p):
    facts = "".join(
        f'<div><div class="t-caption c-soft">{e(k)}</div><div class="t-body c-ink" style="font-weight:700;margin-top:6px;font-size:30px">{e(v)}</div></div>'
        for k,v in p["facts"])
    return "mist", f'''{logo_top("mist")}
<div class="abs t-label c-blue" style="left:96px;top:238px">{e(p["label"])}</div>
<div class="abs t-headline" style="left:96px;top:290px;width:900px"><div>{e(p["h"][0])}</div><div class="c-blue">{e(p["h"][1])}</div><div>{e(p["h"][2])}</div></div>
<div class="abs drop" style="left:120px;top:640px;width:840px;height:680px;transform:rotate(-1.5deg)">
<div class="paper" style="left:0;top:0;width:280px;height:70px;clip-path:polygon(0 100%,8% 0,92% 0,100% 100%);padding:18px 0 0 40px"><span class="t-label c-soft">Case file</span></div>
<div class="paper" style="left:0;top:64px;width:840px;height:616px;padding:40px 40px 0">
<div class="print" style="position:relative;width:760px;height:380px;padding:0"><div class="photo"><span>{e(p["photo"])}</span></div></div>
<div style="display:grid;grid-template-columns:1fr 1.25fr 1fr;gap:24px;margin-top:40px">{facts}</div>
</div>
</div>
<div class="pclip" style="left:868px;top:662px;transform:rotate(6deg)"><svg viewBox="0 0 44 120" aria-hidden="true" style="width:44px;height:120px"><path d="M14 36 V96 a10 10 0 0 0 20 0 V22 a14 14 0 0 0 -28 0 V88" fill="none" stroke="#9AA3B2" stroke-width="5" stroke-linecap="round"></path></svg></div>'''

def stat_cards(p):
    return "mist", f'''{rail()}
<div class="paper" style="left:90px;top:275px;width:430px;height:500px;transform:rotate(-2deg);padding:56px 48px 0">
<div class="t-label c-soft">Before</div>
<div class="hr" style="margin:22px 0 30px"></div>
<div class="t-hero c-soft" style="font-size:170px">{e(p["before"])}</div>
<div class="t-body c-ink" style="margin-top:26px">{e(p["unit"])}</div>
<div class="t-caption c-soft" style="margin-top:12px">{e(p["months"][0])}</div>
</div>
<div class="paper" style="left:560px;top:285px;width:430px;height:500px;transform:rotate(1.5deg);padding:56px 48px 0">
<div class="t-label c-blue">After</div>
<div class="hr" style="margin:22px 0 30px;background:#0054db;height:4px"></div>
<div class="t-hero c-blue" style="font-size:170px">{e(p["after"])}</div>
<div class="t-body c-ink" style="margin-top:26px">{e(p["unit"])}</div>
<div class="t-caption c-soft" style="margin-top:12px">{e(p["months"][1])}</div>
</div>
{clip(257)}{clip(727)}
<div class="abs t-lead" style="left:96px;top:880px;width:880px;font-size:46px">{lines(p["lead"])}</div>
<div class="abs t-caption c-soft" style="left:96px;top:1030px;width:800px">{lines(p["source"])}</div>
{logo_br("mist")}'''

def quote_note(p):
    return "mist", f'''{rail()}
<div class="paper" style="left:80px;top:272px;width:610px;height:780px;transform:rotate(-1.5deg);padding:48px 52px 0">
<div class="c-blue" style="font-weight:700;font-size:150px;line-height:.8;height:92px">&ldquo;</div>
<div class="t-quote">{lines(p["quote"])}</div>
<div class="hr" style="margin:44px 0 28px"></div>
<div class="t-label">{e(p["name"])}</div>
<div class="t-caption c-soft" style="margin-top:8px">{e(p["role"])}</div>
<div class="t-body c-soft" style="margin-top:24px;font-size:28px">{e(p["detail"])}</div>
<svg class="mark b" viewBox="0 0 400 30" preserveAspectRatio="none" aria-hidden="true" style="left:46px;top:372px;width:350px;height:28px">{UNDER}</svg>
</div>
{photo(p["photo"], "left:630px;top:500px;width:390px;height:500px;transform:rotate(3deg);box-shadow:0 18px 40px rgba(10,14,26,.14)")}
{clip(282)}
{logo_br("mist")}'''

def demo_ticket(p):
    arrow = '<span aria-hidden="true">&rarr;</span>'
    return "mist", f'''{rail()}
<div class="abs drop" style="left:80px;top:275px;width:920px;height:800px;transform:rotate(-1deg)">
<div class="paper" style="left:0;top:0;width:920px;height:800px;-webkit-mask:radial-gradient(circle 28px at 630px 0,#0000 98%,#000),radial-gradient(circle 28px at 630px 100%,#0000 98%,#000);-webkit-mask-composite:source-in;mask-composite:intersect;padding:84px 0 0 64px">
<div class="t-label c-blue">{e(p["label"])}</div>
<div class="t-title" style="font-size:80px;margin-top:30px">{lines(p["title"])}</div>
<div class="t-body c-soft" style="margin-top:34px;width:520px">{lines(p["body"])}</div>
<div class="abs" style="left:64px;bottom:72px"><span class="pill">Book a demo {arrow}</span></div>
<div class="abs" style="left:630px;top:44px;bottom:44px;border-left:4px dashed #d5dce8"></div>
<div class="abs" style="left:671px;top:250px;width:208px">
<div class="qr" style="width:208px;height:208px">QR</div>
<div class="t-caption c-soft" style="margin-top:20px;text-align:center">SCAN TO BOOK</div>
</div>
</div>
</div>
{clip(312)}
{logo_br("mist")}'''

def big_number(p):
    return "blue", f'''{logo_top("blue")}
<div class="abs t-label c-yellow" style="left:0;right:0;top:300px;text-align:center">{e(p["label"])}</div>
<div class="abs t-hero c-yellow" style="left:0;right:0;top:370px;text-align:center">{e(p["number"])}</div>
<svg class="mark y" viewBox="0 0 400 30" preserveAspectRatio="none" aria-hidden="true" style="left:190px;top:570px;width:700px;height:40px;transform:rotate(-1deg)">{UNDER}</svg>
<div class="abs t-headline" style="left:0;right:0;top:660px;text-align:center;font-size:64px">{lines(p["line"])}</div>
<div class="paper" style="left:170px;top:920px;width:740px;height:300px;transform:rotate(-2deg);padding:52px 56px 0">
<div class="t-lead" style="font-size:42px">{lines(p["lead"])}</div>
<div class="t-caption c-soft" style="margin-top:30px">{e(p["source"])}</div>
</div>'''

def product(p):
    t = p["tags"]
    return "blue", f'''{logo_top("blue")}
<div class="abs t-title" style="left:0;right:0;top:220px;text-align:center;font-size:84px">{e(p["title"][0])}<br><span class="c-yellow">{e(p["title"][1])}</span></div>
<div class="abs" style="left:355px;top:470px;width:370px;height:780px;border-radius:58px;background:#0a0e1a;padding:16px;box-shadow:0 26px 50px rgba(0,20,70,.35)">
<div style="width:100%;height:100%;border-radius:44px;overflow:hidden"><div class="photo"><span>{e(p["screen"])}</span></div></div>
</div>
<svg class="mark y" viewBox="0 0 1080 1350" aria-hidden="true" style="left:0;top:0;width:1080px;height:1350px;stroke-width:5"><path d="M300 612 H360"></path><path d="M780 802 H720"></path><path d="M318 1012 H360"></path></svg>
<div class="paper t-label c-blue" style="left:88px;top:580px;padding:18px 24px;transform:rotate(-2deg)">{e(t[0])}</div>
<div class="paper t-label c-blue" style="left:780px;top:770px;padding:18px 24px;transform:rotate(2deg)">{e(t[1])}</div>
<div class="paper t-label c-blue" style="left:106px;top:980px;padding:18px 24px;transform:rotate(-1deg)">{e(t[2])}</div>'''

def price_sheet(p):
    def rows(rs):
        return "".join(f'<div style="display:flex;gap:16px;align-items:flex-start;margin-top:22px">{CHECK}<span class="t-body c-ink" style="font-size:31px">{e(r)}</span></div>' for r in rs)
    return "mist", f'''{logo_top("mist")}
<div class="abs t-title" style="left:96px;top:236px;font-size:88px">{e(p["title"][0])}<br><span class="c-blue">{e(p["title"][1])}</span></div>
<div class="paper" style="left:96px;top:510px;width:430px;height:640px;transform:rotate(-1.5deg);padding:50px 44px 0">
<div class="t-label c-soft">Premium</div>
<div class="t-title" style="font-size:80px;margin-top:26px">{e(p["prices"][0])}</div>
<div class="t-body c-soft" style="font-size:28px;margin-top:8px">a month</div>
<div class="hr" style="margin:32px 0 10px"></div>{rows(p["premium"])}
</div>
<div class="paper" style="left:556px;top:500px;width:430px;height:640px;transform:rotate(1.2deg);padding:50px 44px 0">
<div class="t-label c-blue">Business</div>
<div class="t-title" style="font-size:80px;margin-top:26px"><span class="hl">{e(p["prices"][1])}</span></div>
<div class="t-body c-soft" style="font-size:28px;margin-top:8px">a month</div>
<div class="hr" style="margin:32px 0 10px;background:#0054db;height:4px"></div>{rows(p["business"])}
</div>
<div class="abs t-caption c-soft" style="left:96px;top:1215px;width:900px">{e(p["source"])}</div>'''

def founder(p):
    return "mist", f'''{logo_top("mist")}
{photo(p["photo"], "left:96px;top:236px;width:470px;height:600px;transform:rotate(-2.5deg);box-shadow:0 18px 40px rgba(10,14,26,.14)")}
<div class="abs t-label c-blue" style="left:640px;top:300px;width:360px;line-height:1.5">{lines(p["label"])}</div>
<svg class="mark b" viewBox="0 0 160 160" preserveAspectRatio="none" aria-hidden="true" style="left:600px;top:400px;width:130px;height:130px;transform:rotate(208deg)">{ARROW}</svg>
<div class="paper" style="left:400px;top:650px;width:600px;height:600px;transform:rotate(1.5deg);padding:56px 56px 0">
<div class="t-quote" style="font-size:46px">{lines(p["note"])}</div>
<div class="hr" style="margin:40px 0 26px"></div>
<div class="t-label">{e(p["name"])}</div>
<div class="t-caption c-soft" style="margin-top:10px">{lines(p["role"])}</div>
</div>'''

LAYOUTS = dict(MathCover=math_cover, LedgerCompare=ledger, ClipboardSteps=steps, InvoiceCta=invoice,
               CaseFileCover=case_cover, StatCards=stat_cards, QuoteNote=quote_note, DemoTicket=demo_ticket,
               BigNumber=big_number, ProductScreen=product, PriceSheet=price_sheet, FounderNote=founder)

VARS = (":root{--blue:#0054db;--blue-deep:#003fa8;--mist:#f2f5fa;--sky:#e6eefb;--paper:#ffffff;--yellow:#ffde59;"
        "--ink:#0a0e1a;--ink-soft:#4a5060;--rule:#d5dce8;--font-sans:\"DM Sans\",system-ui,sans-serif;"
        "--font-mono:\"DM Mono\",ui-monospace,monospace}")

def page(title, ground, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{e(title)}</title>
<script src="./support.js"></script>
<link rel="stylesheet" href="{DS}/components/bundle.css">
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&amp;family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&amp;display=swap">
<style>
body{{margin:0}}
{VARS}
</style>
</helmet>
<div class="kb-slide g-{ground}" style="width:1080px;height:1350px;font-family:'DM Sans',system-ui,sans-serif">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''

from posts import POSTS

W, H, GAP, ROWGAP, TITLE = 1080, 1350, 80, 120, 300
boards, order, notes = {}, [], {}
pages = [{"id": "p1", "name": "Posts 01–10"}, {"id": "p2", "name": "Posts 11–20"}, {"id": "p3", "name": "Posts 21–30"}]
count = 0
for post in POSTS:
    n = post["n"]
    pg = pages[(n - 1) // 10]["id"]
    row = (n - 1) % 10
    y = row * (H + ROWGAP + TITLE) + TITLE
    nslides = len(post["slides"])
    for i, (layout, data) in enumerate(post["slides"]):
        ground, body = LAYOUTS[layout](data)
        assert ground == post["ground"], (n, layout)
        name = "Main.dc.html" if (n == 1 and i == 0) else f"p{n:02d}-{i+1}-{layout.lower()}.dc.html"
        stitle = f"{n:02d} · slide {i+1} · {layout}" if nslides > 1 else f"{n:02d} · {layout}"
        with open(os.path.join(PROJ, name), "w") as f:
            f.write(page(stitle, ground, body))
        boards[name] = {"x": i * (W + GAP), "y": y, "w": W, "h": H, "title": stitle, "page": pg}
        order.append(name)
        count += 1
    kind = "carousel" if nslides > 1 else "single"
    hold = "  ·  HOLD" if post.get("hold") else ""
    notes[f"t{n:02d}"] = {"x": 0, "y": y - 250, "text": f"{n:02d} · {post['date']} · {post['name']} · {post['ground']} {kind}{hold}",
                          "kind": "title1", "maxW": 4 * W + 3 * GAP, "page": pg}
    sx = nslides * (W + GAP)
    notes[f"c{n:02d}"] = {"x": sx, "y": y, "w": 760, "maxH": 1300, "page": pg,
                          "fill": "orange" if post.get("hold") else "yellow" if False else "green",
                          "size": "l",
                          "text": "CAPTION\n" + post["caption"] + ("\n\nBEFORE POSTING\n" + post["check"] if post.get("check") else "")}

canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")},
          "title": "Kuyy Business — First 30 Posts", "launch": {"view": "canvas", "page": "p1"}, "pages": pages,
          "boards": boards, "order": order, "notes": notes,
          "designSystems": [{"title": "Kuyy! Business Feed", "namespace": "kuyybusinessfeed",
                             "artifact": "https://claude.ai/artifact/5BGcUdrHyrDg6PteKAdf3T",
                             "version": "1790234215-5819",
                             "copiedAt": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}]}
with open(os.path.join(PROJ, "canvas.json"), "w") as f:
    json.dump(canvas, f, ensure_ascii=False, indent=1)
print("artboards", count)
