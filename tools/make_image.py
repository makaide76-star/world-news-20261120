#!/usr/bin/env python3
"""Draw the entry image: the world news of Friday 20 November 2026 in one picture.

Pure PIL, deterministic (no randomness, no clock, no network).
Output: assets/entry.png (1024x1024).
Stories are the day's wire headlines of 20 Nov 2026, cross-checked across
SCMP, Dawn, Bangkok Post, China Times and OneTurn's daily digest.
Fixed grid layout (1024x1024):
  masthead 0-165 | hero 178-478 | markets 505-660 | conflict 678-838
  climate 856-940 | footer strip 952-1024
"""
from PIL import Image, ImageDraw, ImageFont
import os

S = 1024
PAPER = (247, 242, 231)
INK = (20, 32, 43)
RED = (176, 32, 40)
BLUE = (24, 62, 110)
GOLD = (198, 142, 32)
GREEN = (30, 110, 76)
GREY = (92, 96, 100)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (S, S), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

def text_block(x, y, text, font, fill, width, leading=1.25):
    for line in wrap(text, font, width):
        d.text((x, y), line, font=font, fill=fill)
        y += int(font.size * leading)
    return y

# ---------- masthead ----------
d.rectangle([0, 0, S, 44], fill=INK)
d.text((28, 11), "FRIDAY  ·  20 NOVEMBER 2026  ·  WORLD NEWS", font=F(SANS_B, 21), fill=(240, 235, 220))
r = "ONE DAY · ONE IMAGE"
d.text((S - 28 - d.textlength(r, font=F(SANS_B, 21)), 11), r, font=F(SANS_B, 21), fill=GOLD)
d.text((28, 58), "THE WORLD TODAY", font=F(SERIF_B, 74), fill=INK)
d.rectangle([28, 148, S - 28, 153], fill=INK)
d.rectangle([28, 158, S - 28, 160], fill=INK)

# ---------- hero left: Shenzhen summit ----------
HX, HW = 28, 618
d.text((HX, 178), "SHENZHEN · APEC SUMMIT", font=F(SANS_B, 21), fill=RED)
d.text((HX, 208), "TRUMP · XI · PUTIN", font=F(SERIF_B, 47), fill=INK)
d.text((HX, 268), "First three-way summit in history", font=F(SERIF_B, 30), fill=BLUE)
text_block(HX, 312, "The US, Chinese and Russian presidents meet in Shenzhen and sign a joint peace declaration — talking Ukraine and nuclear arms.",
           F(SANS, 21), INK, HW, 1.3)
# three flags at y 392-478
FY0, FH, FW = 392, 86, 196
fx = HX
for i in range(7):
    d.rectangle([fx, FY0 + i * (FH // 7), fx + FW, FY0 + (i + 1) * (FH // 7)], fill=(178, 34, 52) if i % 2 == 0 else WHITE)
d.rectangle([fx, FY0, fx + 84, FY0 + FH // 2], fill=(60, 59, 110))
for r_ in range(3):
    for c_ in range(4):
        d.ellipse([fx + 8 + c_ * 20, FY0 + 5 + r_ * 13, fx + 13 + c_ * 20, FY0 + 10 + r_ * 13], fill=WHITE)
fx2 = fx + FW + 14
d.rectangle([fx2, FY0, fx2 + FW, FY0 + FH], fill=(222, 41, 55))
d.polygon([(fx2 + 24, FY0 + 12), (fx2 + 29, FY0 + 27), (fx2 + 45, FY0 + 27), (fx2 + 32, FY0 + 37), (fx2 + 37, FY0 + 53), (fx2 + 24, FY0 + 43), (fx2 + 11, FY0 + 53), (fx2 + 16, FY0 + 37), (fx2 + 3, FY0 + 27), (fx2 + 19, FY0 + 27)], fill=(255, 222, 0))
for (sx, sy) in [(62, 10), (74, 26), (74, 42), (60, 54)]:
    d.ellipse([fx2 + sx, FY0 + sy, fx2 + sx + 10, FY0 + sy + 10], fill=(255, 222, 0))
fx3 = fx2 + FW + 14
for i, col in enumerate([WHITE, (0, 57, 166), (213, 43, 30)]):
    d.rectangle([fx3, FY0 + i * (FH // 3), fx3 + FW, FY0 + (i + 1) * (FH // 3)], fill=col)
for fx_ in (fx, fx2, fx3):
    d.rectangle([fx_, FY0, fx_ + FW, FY0 + FH], outline=INK, width=2)

# ---------- hero right: ICJ panel 178-478 ----------
IX, IW = 678, 318
d.rectangle([IX, 178, IX + IW, 478], fill=BLUE)
d.text((IX + 20, 194), "THE HAGUE · WORLD COURT", font=F(SANS_B, 17), fill=GOLD)
d.text((IX + 20, 226), "MYANMAR", font=F(SERIF_B, 39), fill=WHITE)
d.text((IX + 20, 272), "GUILTY OF", font=F(SERIF_B, 39), fill=WHITE)
d.text((IX + 20, 318), "GENOCIDE", font=F(SERIF_B, 39), fill=(255, 120, 110))
text_block(IX + 20, 372, "The ICJ's first genocide verdict against a state — over the Rohingya.",
           F(SANS, 20), (225, 232, 242), IW - 40, 1.3)

d.rectangle([28, 492, S - 28, 494], fill=GREY)

# ---------- markets 505-660 ----------
d.text((28, 505), "MARKETS · AI SELL-OFF", font=F(SANS_B, 21), fill=RED)
d.text((28, 534), "Stocks slide — even as an AI giant soars", font=F(SERIF_B, 34), fill=INK)
pts = [(28, 596), (120, 590), (210, 606), (300, 600), (390, 626), (468, 646)]
d.line(pts, fill=RED, width=6, joint="curve")
d.polygon([(468, 646), (448, 642), (458, 660)], fill=RED)
text_block(500, 588, "Nikkei −4.8% · S&P 500 −2%, a fifth straight fall. Anthropic's record Nasdaq debut closes 17% UP — euphoria and fear on the same day.",
           F(SANS, 21), INK, 496, 1.3)
d.rectangle([28, 670, S - 28, 672], fill=GREY)

# ---------- conflict 678-838 ----------
d.text((28, 684), "RIYADH · MISSILE STRIKE", font=F(SANS_B, 20), fill=RED)
d.text((28, 712), "Houthi missile hits the PIF Tower", font=F(SERIF_B, 25), fill=INK)
TY = 754
d.rectangle([28, TY + 6, 62, TY + 78], fill=INK)
d.polygon([(28, TY + 6), (45, TY - 12), (62, TY + 6)], fill=INK)
for wy in range(TY + 14, TY + 68, 13):
    d.rectangle([36, wy, 54, wy + 6], fill=GOLD)
d.polygon([(90, TY + 2), (98, TY + 14), (110, TY + 16), (99, TY + 25), (102, TY + 38), (90, TY + 30), (78, TY + 38), (81, TY + 25), (70, TY + 16), (82, TY + 14)], fill=RED)
text_block(128, TY, "Windows blown out across eight floors of Riyadh's tallest tower — the second strike on the financial district this month.",
           F(SANS, 19), INK, 344, 1.3)

UX = 540
d.text((UX, 684), "UKRAINE · WAR", font=F(SANS_B, 20), fill=RED)
d.text((UX, 712), "Embassies hit in Kyiv;", font=F(SERIF_B, 25), fill=INK)
d.text((UX, 744), "Kerch Bridge struck again", font=F(SERIF_B, 25), fill=INK)
text_block(UX, 786, "Russian barrage damages the Austrian and Dutch missions and a cathedral. Ukraine hits the Crimea bridge a 3rd time in 4 days.",
           F(SANS, 19), INK, 456, 1.3)

# ---------- climate 856-940 ----------
d.rectangle([28, 856, S - 28, 858], fill=GREY)
d.text((28, 866), "ANTALYA · COP31 CLIMATE TALKS", font=F(SANS_B, 20), fill=GREEN)
text_block(28, 896, "Draft deal drops fossil fuels: the phase-out pledge vanishes from the COP31 text as the summit wraps — Pacific nations call it an outrage.",
           F(SANS, 20), INK, 968, 1.3)

# ---------- footer strip ----------
d.rectangle([0, 952, S, S], fill=INK)
notes = [
    ("KENYA", "Last Ebola patient goes home — outbreak ends after 37 days"),
    ("SPACE", "Voyager 1 phones home from 1 light-day away"),
    ("ART", "Van Gogh sells for a record $190.4M"),
]
nx = 28
for tag, txt in notes:
    d.text((nx, 962), tag, font=F(SANS_B, 17), fill=GOLD)
    for j, ln in enumerate(wrap(txt, F(SANS, 16), 302)[:2]):
        d.text((nx, 986 + j * 19), ln, font=F(SANS, 16), fill=(235, 238, 240))
    nx += 330

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "entry.png")
img.save(out, format="PNG", optimize=True)
print("wrote", out, os.path.getsize(out), "bytes")
