"""Launch announcement: a collab post published from @kuyy.business with @kuyy.app as collaborator,
so it shows on both grids. Built from the locked "The math" carousel (blue)."""
import json, os, sys
from gen import page, LAYOUTS

INDEX = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "canvas3", "project")
os.makedirs(OUT, exist_ok=True)

SLIDES = [
 ("MathCover", {"label": "New · Kuyy! Business", "h": ["Clubs host on Kuyy!", "Now studios can", "run on it too."],
    "header": "KUYY! · WHAT IT DOES", "rows": [("Host activities", "yes"), ("Book classes", "yes"), ("Run a studio", "new")],
    "total": "Oct 2026", "total_label": "Launch"}),
 ("LedgerCompare", {"title": ["4,000+ communities", "host here. Now studios."], "cols": ["Kuyy! app", "Business"],
    "rows": [("Who hosts", "Clubs", "Studios"), ("Who books", "Members", "Members"), ("What it does", "Host, fill", "Run, grow")],
    "total": ("Same marketplace", "300,000+"),
    "source": ["Kuyy! public numbers: 4,000+ communities,", "300,000+ registered users, Sep 2026."]}),
 ("ClipboardSteps", {"title": ["Built to grow", "your studio"], "steps": [
    "Bookings, payments and passes in one dashboard.", "Members check in by QR.",
    "Your classes listed on the Kuyy! app.", "Revenue and attendance at a glance."]}),
 ("InvoiceCta", {"no": "NO. 001 · LAUNCH", "title": ["Run a studio?", "Start here."],
    "items": [("30-day free trial", "Rp 0")], "total": "Rp 0", "pill": "Start free trial"}),
]

CAPTION = ("Kuyy! grew with community hosts, like tennis clubs, who brought their members to the app. "
           "Kuyy! Business opens the same marketplace to studios, with growth infrastructure to run bookings, payments and members. "
           "Start free trial at business.kuyy.id #kuyybusiness")

NOTE = ("COLLAB POST · post from @kuyy.business, invite @kuyy.app as collaborator\n\n"
        "CAPTION\n" + CAPTION + "\n\n"
        "BEFORE POSTING\n"
        "· Post it on a blue day of the business grid (the day after a mist post) so the checkerboard holds.\n"
        "· @kuyy.app's team approves: on their grid this slide uses the business look, not the Kuyy! Feed style.\n"
        "· 'Launch · Oct 2026': change to the real launch month.\n"
        "· Swap the QR for business.kuyy.id.")

idx = json.load(open(INDEX))
top = max(v["y"] + v["h"] for v in idx["boards"].values() if v.get("page") == "p0") + 120 + 300
written = []
for i, (layout, data) in enumerate(SLIDES):
    ground, body = LAYOUTS[layout](data)
    assert ground == "blue"
    name = f"collab-{i+1}-{layout.lower()}.dc.html"
    title = f"Collab announcement · slide {i+1}"
    with open(os.path.join(OUT, name), "w") as f:
        f.write(page(title, ground, body))
    idx["boards"][name] = {"x": i * 1160, "y": top, "w": 1080, "h": 1350, "title": title, "page": "p0"}
    idx["order"].append(name)
    written.append(name)
idx["notes"]["tcollab"] = {"x": 0, "y": top - 250, "text": "Collab announcement · @kuyy.business × @kuyy.app",
                           "kind": "title1", "maxW": 4 * 1080 + 3 * 80, "page": "p0"}
idx["notes"]["ncollab"] = {"x": 4 * 1160, "y": top, "w": 760, "maxH": 1300, "page": "p0", "fill": "green",
                           "size": "l", "text": NOTE}
with open(os.path.join(OUT, "canvas.json"), "w") as f:
    json.dump(idx, f, ensure_ascii=False, indent=1)
print(json.dumps({f"project/{n}": f"project/{n}" for n in written}))
