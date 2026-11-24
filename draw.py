#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news image, 1024x1024, deterministic."""
from PIL import Image, ImageDraw, ImageFont
import textwrap, os, math

W = H = 1024
BG = (244, 241, 232)
INK = (20, 20, 20)
RED = (178, 34, 34)
BLUE = (24, 64, 120)
TEAL = (14, 110, 110)
ORANGE = (204, 92, 0)
GREY = (90, 90, 90)
PANEL = (255, 255, 255)
LINE = (180, 175, 165)
GREEN = (18, 130, 60)

def font(name, size):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}.ttf", size)

F_TITLE = font("DejaVuSans-Bold", 64)
F_DATE = font("DejaVuSans", 26)
F_H1 = font("DejaVuSans-Bold", 44)
F_H2 = font("DejaVuSans-Bold", 30)
F_H3 = font("DejaVuSans-Bold", 26)
F_BODY = font("DejaVuSans", 24)
F_SMALL = font("DejaVuSans", 21)
F_TAG = font("DejaVuSans-Bold", 22)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def text_block(x, y, text, fnt, fill=INK, width=40, leading=None):
    lines = []
    for para in text.split("\n"):
        lines += textwrap.wrap(para, width=width)
    lh = leading or int(fnt.size * 1.25)
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y

def kicker(x, y, label, color):
    d.text((x, y), label, font=F_TAG, fill=color)
    return y + 30

def panel(x0, y0, x1, y1):
    d.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=PANEL, outline=LINE, width=2)

# ---------- masthead ----------
d.text((32, 18), "THE WORLD IN ONE DAY", font=F_TITLE, fill=INK)
d.line([32, 96, 992, 96], fill=INK, width=4)
d.text((32, 108), "TUESDAY 24 NOVEMBER 2026", font=F_DATE, fill=RED)
right = "ONE IMAGE  •  THE WHOLE DAY"
d.text((992 - d.textlength(right, font=F_DATE), 108), right, font=F_DATE, fill=GREY)
d.line([32, 148, 992, 148], fill=INK, width=2)

# ---------- lead: Nvidia reinstates Huang (168-470) ----------
panel(32, 168, 992, 470)
cx, cy = 185, 305
# chip: green square with pins
d.rectangle([cx-78, cy-78, cx+78, cy+78], fill=GREEN, outline=INK, width=3)
for i in range(5):
    x = cx - 56 + i * 28
    d.line([x, cy-78, x, cy-96], fill=INK, width=4)
    d.line([x, cy+78, x, cy+96], fill=INK, width=4)
    y = cy - 56 + i * 28
    d.line([cx-78, y, cx-96, y], fill=INK, width=4)
    d.line([cx+78, y, cx+96, y], fill=INK, width=4)
d.text((cx-38, cy-24), "NVDA", font=F_H2, fill=(255, 255, 255))
d.text((cx-42, cy+14), "+31%", font=F_H2, fill=(255, 255, 255))
d.text((cx-72, 420), "SANTA CLARA", font=F_SMALL, fill=GREY)
kicker(320, 190, "TECH  •  LEAD STORY", RED)
d.text((320, 222), "HUANG IS BACK", font=F_H1, fill=INK)
d.text((320, 272), "AT NVIDIA", font=F_H1, fill=INK)
text_block(320, 326, "Board votes unanimously to reinstate Jensen Huang as CEO, 11 days after he resigned. Trump pressed the board; shares jump 31%.", F_BODY, width=40, leading=29)
d.text((320, 440), "Board: “no national security risk”.", font=F_SMALL, fill=GREY)

# ---------- row 2 (492-748) ----------
panel(32, 492, 500, 748)
kicker(52, 510, "EU  •  SANCTIONS", RED)
d.text((52, 542), "EU unveils 22nd", font=F_H2, fill=INK)
d.text((52, 578), "Russia package", font=F_H2, fill=INK)
text_block(52, 624, "60 banks cut from SWIFT, crypto crackdown, 70+ shadow-fleet ships listed.", F_SMALL, width=24, leading=25)
# EU circle of stars, right column
ecx, ecy, er = 425, 680, 42
d.ellipse([ecx-er, ecy-er, ecx+er, ecy+er], fill=BLUE)
for k in range(12):
    a = math.pi * 2 * k / 12 - math.pi / 2
    sx = ecx + int(30 * math.cos(a))
    sy = ecy + int(30 * math.sin(a))
    d.ellipse([sx-3, sy-3, sx+3, sy+3], fill=(255, 220, 0))

panel(524, 492, 992, 748)
kicker(544, 510, "DISASTER  •  INDONESIA", RED)
d.text((544, 542), "Factory fire kills", font=F_H2, fill=INK)
d.text((544, 578), "at least 24", font=F_H2, fill=INK)
text_block(544, 624, "Candy factory blaze in Banten; rescuers search for around 30 missing workers.", F_SMALL, width=24, leading=25)
# flames, right column
d.polygon([(860, 700), (885, 645), (910, 700)], fill=ORANGE)
d.polygon([(915, 700), (938, 650), (960, 700)], fill=ORANGE)
d.rectangle([855, 700, 968, 726], fill=(60, 60, 60))

# ---------- row 3 (770-992) ----------
def small(x0, x1, tag, color, head, body):
    panel(x0, 770, x1, 992)
    kicker(x0+20, 786, tag, color)
    y = text_block(x0+20, 820, head, F_H3, width=15, leading=30)
    text_block(x0+20, y+4, body, F_SMALL, width=22, leading=25)

small(32, 344, "EUROPE", BLUE,
      "Lisbon marches\non living costs",
      "Thousands protest rising prices in Portugal.")
small(356, 668, "SPORT", TEAL,
      "Verstappen wins\nLas Vegas GP",
      "Alcaraz takes his first ATP Finals title in Turin.")
small(680, 992, "ASIA", ORANGE,
      "India–Nepal train\nrolls out",
      "Modi and PM Shah flag off the Saryu-Kamala Express.")

# ---------- footer ----------
F_SRC = font("DejaVuSans", 16)
d.text((32, 1000), "Sources: Reuters, CNN, AP, The Times of India  •  24 November 2026", font=F_SRC, fill=GREY)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, "PNG", optimize=True)
print("saved", out, os.path.getsize(out), "bytes")
