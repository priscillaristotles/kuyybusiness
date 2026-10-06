"""Pinned post 2 becomes the brand story (Samasta Aerial, told as a Studio case, mist).
Feed posts 01, 07, 13 move to other studio founders; post 05 stops being Samasta."""
import json, os, sys
from gen import page, LAYOUTS
from posts import POSTS

INDEX = sys.argv[1]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "canvas5", "project")
os.makedirs(OUT, exist_ok=True)

BRAND = [
 ("CaseFileCover", {"label": "Our story · Samasta Aerial", "h": ["Samasta Aerial went", "from 1 to 7 branches", "in 18 months."],
    "facts": [("TYPE", "Aerial"), ("BRANCHES", "7"), ("ON KUYY! BUSINESS", "6")],
    "photo": "Photo · a class at a Samasta branch"}),
 ("StatCards", {"before": "1", "after": "7", "unit": "studio branches", "months": ["[MON YYYY]", "[MON YYYY]"],
    "lead": ["Each branch made it clearer:", "the tools weren't built for us."],
    "source": ["Samasta Aerial's own records, [months].", "Shared by its founder."]}),
 ("QuoteNote", {"quote": ["I almost built my", "own software. I", "helped build Kuyy!", "Business instead."],
    "name": "Priscilla Aristotles", "role": "FOUNDER, SAMASTA · CBO, KUYY!",
    "detail": "Ran Samasta on other tools first.", "photo": "Photo · Priscilla"}),
 ("DemoTicket", {"label": "Free studio audit", "title": ["Start where", "we started."],
    "body": ["Book a free audit. We look", "at your studio with you."], "pill": "Book a free audit"}),
]
CAPTION = ("Kuyy! Business started in a studio. Priscilla grew Samasta Aerial from 1 to 7 branches in 4 cities "
           "on tools that didn't fit, then helped build the one that does. Book a free audit at business.kuyy.id #kuyybusiness")
CHECK = ("· Confirm 1 to 7 branches in 18 months, and fill the months on the before/after cards.\n"
         "· '6 on Kuyy! Business' comes from your edit to post 05: confirm.\n"
         "· Priscilla approves the quote. Real photos for the cover and the quote.\n"
         "· The free audit must exist as an offer, with a booking link for the QR (same as the collab post).\n"
         "· Worth adding: one number Kuyy! Business moved at Samasta, as a 5th slide. The story proves the founder; "
         "a product number proves the product.")

idx = json.load(open(INDEX))
files = {}

def write(name, title, ground, body):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(page(title, ground, body))
    files[f"project/{name}"] = f"project/{name}"

# --- pinned row: pin1 (4 slides) · pin2 brand story (4) · pin3 (1)
old = "pin2-1-pricesheet.dc.html"
y = idx["boards"][old]["y"]
del idx["boards"][old]
idx["order"].remove(old)
files[f"project/{old}"] = None
for i, (layout, data) in enumerate(BRAND):
    ground, body = LAYOUTS[layout](data)
    assert ground == "mist"
    name = f"pin2-{i+1}-{layout.lower()}.dc.html"
    title = f"Pinned 2 · Brand story · slide {i+1}"
    write(name, title, ground, body)
    idx["boards"][name] = {"x": (4 + i) * 1160, "y": y, "w": 1080, "h": 1350, "title": title, "page": "p0"}
    idx["order"].append(name)
idx["boards"]["pin3-1-productscreen.dc.html"]["x"] = 8 * 1160
idx["notes"]["pT"]["maxW"] = 9 * 1080 + 8 * 80
idx["notes"]["npin2"].update({"x": 7 * 1160, "fill": "orange",
    "text": "PINNED 2 · BRAND STORY\nCAPTION\n" + CAPTION + "\n\nBEFORE POSTING\n" + CHECK})
idx["notes"]["npin3"]["x"] = 8 * 1160

# --- feed posts 01, 05, 07, 13
for post in POSTS:
    n = post["n"]
    if n not in (1, 5, 7, 13):
        continue
    nslides = len(post["slides"])
    for i, (layout, data) in enumerate(post["slides"]):
        ground, body = LAYOUTS[layout](data)
        name = "Main.dc.html" if (n == 1 and i == 0) else f"p{n:02d}-{i+1}-{layout.lower()}.dc.html"
        assert name in idx["boards"], name
        title = f"{n:02d} · slide {i+1} · {layout}" if nslides > 1 else f"{n:02d} · {layout}"
        write(name, title, ground, body)
    kind = "carousel" if nslides > 1 else "single"
    idx["notes"][f"t{n:02d}"]["text"] = f"{n:02d} · {post['date']} · {post['name']} · mist {kind}  ·  HOLD"
    idx["notes"][f"c{n:02d}"].update({"fill": "orange",
        "text": "CAPTION\n" + post["caption"] + "\n\nBEFORE POSTING\n" + post["check"]})

with open(os.path.join(OUT, "canvas.json"), "w") as f:
    json.dump(idx, f, ensure_ascii=False, indent=1)
print(json.dumps(files))
