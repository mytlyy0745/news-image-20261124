"""Draw the front page for Tuesday 24 November 2026 as one 1024x1024 PNG.

Everything here is drawn with Pillow from the news I verified this morning:
Nvidia reinstating Jensen Huang, the EU's 22nd Russia sanctions package,
the Serang factory fire, the Lisbon cost-of-living march, Verstappen's
Las Vegas win, Alcaraz's first ATP Finals title and the Saryu-Kamala
Express flag-off. Run: python3 draw.py  ->  entry.png beside this file.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 230)
INK = (22, 21, 18)
SOFT_INK = (74, 70, 62)
RED = (163, 31, 31)
BLUE = (31, 78, 121)
GREEN = (30, 122, 52)
ORANGE = (194, 87, 26)
PURPLE = (91, 45, 142)
TEAL = (15, 118, 110)
GOLD = (154, 123, 10)
CARD_BG = (255, 253, 247)
RULE = (180, 172, 152)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF = "DejaVuSerif-Bold.ttf"
SERIF_REG = "DejaVuSerif.ttf"
SANS = "DejaVuSans-Bold.ttf"
SANS_REG = "DejaVuSans.ttf"


def wrap(draw, text, fnt, max_width):
    """Split text into lines that fit max_width pixels."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def para(draw, xy, text, fnt, fill, max_width, leading):
    """Draw wrapped text; return the y just below the last line."""
    x, y = xy
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def kicker(draw, x, y, text, colour):
    fnt = font(SANS, 17)
    draw.text((x, y), text.upper(), font=fnt, fill=colour)
    return y + 24


def headline(draw, x, y, text, size, max_width, leading=None):
    fnt = font(SERIF, size)
    return para(draw, (x, y), text, fnt, INK, max_width, leading or size + 6)


def deck(draw, x, y, text, max_width, size=18):
    fnt = font(SANS_REG, size)
    return para(draw, (x, y), text, fnt, SOFT_INK, max_width, size + 6)


def glyph_eu(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], fill=BLUE)
    cx, cy, r = x + s // 2, y + s // 2, s // 3
    for i in range(12):
        import math
        a = math.pi * 2 * i / 12 - math.pi / 2
        gx, gy = cx + int(r * math.cos(a)), cy + int(r * math.sin(a))
        draw.ellipse([gx - 3, gy - 3, gx + 3, gy + 3], fill=(255, 210, 0))


def glyph_flame(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], fill=(253, 232, 210))
    draw.polygon([(x + s // 2, y + 8), (x + s - 10, y + s - 12),
                  (x + s // 2 + 6, y + s - 26), (x + 10, y + s - 12)],
                 fill=ORANGE)
    draw.polygon([(x + s // 2, y + s - 12), (x + s // 2 - 12, y + s - 30),
                  (x + s // 2 + 12, y + s - 30)], fill=(255, 200, 40))


def glyph_crowd(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], fill=(232, 238, 245))
    for i, dx in enumerate([14, 34, 54, 74]):
        draw.ellipse([x + dx - 7, y + 18, x + dx + 7, y + 32], fill=INK)
        draw.rectangle([x + dx - 9, y + 34, x + dx + 9, y + s - 14], fill=RED if i % 2 else BLUE)
    draw.line([(x + 8, y + 12), (x + s - 8, y + 12)], fill=INK, width=3)


def glyph_flag(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], fill=(238, 238, 238))
    for i in range(8):
        x0 = x + i * (s // 8)
        draw.rectangle([x0, y, x0 + s // 8, y + s], fill=INK if i % 2 == 0 else (255, 255, 255))
    draw.rectangle([x, y, x + s, y + s], outline=INK, width=2)


def glyph_ball(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], fill=(228, 244, 190))
    cx, cy = x + s // 2, y + s // 2
    draw.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], fill=(190, 220, 60), outline=INK, width=2)
    draw.arc([cx - 26, cy - 26, cx + 26, cy + 26], start=40, end=140, fill=(255, 255, 255), width=4)
    draw.arc([cx - 26, cy - 26, cx + 26, cy + 26], start=220, end=320, fill=(255, 255, 255), width=4)


def glyph_train(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], fill=(222, 235, 222))
    draw.rectangle([x + 12, y + 22, x + s - 12, y + 58], fill=TEAL)
    for i in range(3):
        wx = x + 20 + i * 24
        draw.rectangle([wx, y + 30, wx + 16, y + 48], fill=(255, 255, 255))
    draw.line([(x + 10, y + s - 16), (x + s - 10, y + s - 16)], fill=INK, width=3)
    draw.line([(x + 16, y + s - 8), (x + s - 16, y + s - 8)], fill=INK, width=3)


def story_card(draw, x, y, w, h, kicker_text, colour, title, body, glyph):
    draw.rectangle([x, y, x + w, y + h], fill=CARD_BG, outline=RULE, width=1)
    draw.rectangle([x, y, x + w, y + 5], fill=colour)
    tx = x + 16
    ty = y + 14
    kicker(draw, tx, ty, kicker_text, colour)
    glyph(draw, x + w - 108, ty, 92)
    after_head = headline(draw, tx, ty + 28, title, 24, w - 140, 29)
    deck(draw, tx, after_head + 6, body, w - 32, 16)


def chart(draw, x, y, w, h):
    """A small bar chart of Nvidia's jump: five flat days, then +31%."""
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255), outline=RULE, width=1)
    draw.text((x + 14, y + 10), "NVDA — THE COMEBACK", font=font(SANS, 15), fill=SOFT_INK)
    base = y + h - 34
    values = [52, 48, 55, 50, 46, 148]
    scale = (base - (y + 62)) / max(values)
    bw, gap = 34, 16
    total = len(values) * (bw + gap) - gap
    x0 = x + (w - total) // 2
    for i, v in enumerate(values):
        bx = x0 + i * (bw + gap)
        top = base - int(v * scale)
        colour = GREEN if i == len(values) - 1 else (150, 158, 168)
        draw.rectangle([bx, top, bx + bw, base], fill=colour)
        if i == len(values) - 1:
            label = "+31%"
            lf = font(SANS, 22)
            lw = draw.textlength(label, font=lf)
            draw.text((bx + (bw - lw) / 2, top - 30), label, font=lf, fill=GREEN)
    draw.line([(x + 12, base), (x + w - 12, base)], fill=INK, width=2)
    draw.text((x + 14, y + h - 26), "12–23 NOV 2026", font=font(SANS_REG, 14), fill=SOFT_INK)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    mx = 36
    draw.rectangle([14, 14, W - 15, H - 15], outline=INK, width=2)
    draw.rectangle([20, 20, W - 21, H - 21], outline=RULE, width=1)

    # Masthead.
    title = "THE WORLD IN ONE PAGE"
    tf = font(SERIF, 56)
    tw = draw.textlength(title, font=tf)
    draw.text(((W - tw) / 2, 34), title, font=tf, fill=INK)
    rule(draw, mx, 112, W - mx, 3)
    sub = "TUESDAY  ·  24 NOVEMBER 2026  ·  THE DAY'S WORLD NEWS, IN ONE IMAGE"
    sf = font(SANS, 21)
    sw = draw.textlength(sub, font=sf)
    draw.text(((W - sw) / 2, 124), sub, font=sf, fill=RED)
    rule(draw, mx, 158, W - mx, 1, RULE)

    # Lead story: Nvidia.
    ly = 172
    kicker(draw, mx, ly, "Tech · Markets — the lead story", RED)
    after_head = headline(draw, mx, ly + 28, "Huang is back at Nvidia — shares soar 31%", 40, 560, 47)
    after_deck = deck(draw, mx, after_head + 10,
                      "Eleven days after he resigned, the board voted unanimously to "
                      "reinstate Jensen Huang as chief executive. The stock closed up "
                      "31%, adding about $960bn of value.", 560, 19)
    draw.text((mx, after_deck + 8), "Board vote 22 Nov · announced 23 Nov",
              font=font(SANS_REG, 15), fill=SOFT_INK)
    chart(draw, 640, ly + 6, 348, 200)

    rule(draw, mx, 408, W - mx, 1, RULE)

    # Six more stories in a 2 x 3 grid.
    cw, ch, gap = 470, 168, 12
    rows = [
        (mx, 420, "Europe · Sanctions", BLUE, "EU's 22nd sanctions package on Russia",
         "About 60 banks face a SWIFT cut-off, crypto networks are targeted and 70+ shadow-fleet ships are listed.",
         glyph_eu),
        (mx + cw + gap, 420, "Indonesia · Tragedy", ORANGE, "24 dead in Indonesia factory fire",
         "Blaze at a candy factory in Cikande, Banten, on 21 Nov. About 30 people are still missing; a short circuit is suspected.",
         glyph_flame),
        (mx, 600, "Portugal · Protest", RED, "Lisbon marches over the cost of living",
         "Thousands braved rain on 21 Nov demanding higher pay and cheaper housing. Unions rally again at parliament today.",
         glyph_crowd),
        (mx + cw + gap, 600, "Sport · Formula 1", PURPLE, "Verstappen wins a wild Las Vegas GP",
         "A third Vegas win, by 0.64s from Norris, after 35 lead changes and 352 overtakes under the lights.",
         glyph_flag),
        (mx, 780, "Sport · Tennis", TEAL, "Alcaraz claims first ATP Finals crown",
         "Beat world No. 1 Zverev 6–2, 7–6 in Turin — the fourth man to hold all four Slams and the Finals title.",
         glyph_ball),
        (mx + cw + gap, 780, "India · Nepal", GOLD, "A train links Ram's and Sita's birthplaces",
         "Modi and Nepal's PM Shah flagged off the weekly Saryu-Kamala Express, Ayodhya to Janakpur, 604 km.",
         glyph_train),
    ]
    for x, y, kick, colour, title, body, glyph in rows:
        story_card(draw, x, y, cw, ch, kick, colour, title, body, glyph)

    # Footer strip.
    rule(draw, mx, 962, W - mx, 1, RULE)
    draw.rectangle([mx, 974, mx + 10, 984], fill=RED)
    draw.text((mx + 18, 972), "ALSO: Ukraine says it sank a Russian warship off Libya  ·  Chicago O'Hare halts flights briefly in the Thanksgiving rush",
              font=font(SANS_REG, 14), fill=SOFT_INK)
    return img


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "entry.png")
    build().save(out, format="PNG")
    print("wrote", out)
