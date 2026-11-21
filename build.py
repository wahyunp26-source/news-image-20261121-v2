#!/usr/bin/env python3
"""Compose the Saturday 21 November 2026 front page (1024x1024).

Build-time only: reads the flat-vector illustrations in assets/ and writes
entry.png. The graded entrypoint (main.py) only copies entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")

W, H = 1024, 1024
CREAM = (247, 242, 231)
INK = (26, 26, 26)
RED = (185, 28, 28)
GREY = (90, 86, 78)
NAVY = (31, 58, 95)
RULE = (26, 26, 26)


def font(name, size, bold=False):
    base = "/usr/share/fonts/truetype/liberation/"
    if name == "serif":
        f = "LiberationSerif-Bold.ttf" if bold else "LiberationSerif-Regular.ttf"
    else:
        f = "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"
    return ImageFont.truetype(base + f, size)


def wrap(draw, text, fnt, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(path, w, h):
    im = Image.open(path).convert("RGB")
    tw, th = im.size
    target = w / h
    src = tw / th
    if src > target:
        nw = int(th * target)
        x0 = (tw - nw) // 2
        im = im.crop((x0, 0, x0 + nw, th))
    else:
        nh = int(tw / target)
        y0 = (th - nh) // 2
        im = im.crop((0, y0, tw, y0 + nh))
    return im.resize((w, h), Image.LANCZOS)


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


# ---------------------------------------------------------------- stories
BIG = [
    ("cop31", "1 ANTALYA, TÜRKIYE · CLIMATE",
     "COP31 runs into overtime with no deal",
     "Talks pass their Friday deadline with no deal; a third draft is due "
     "Saturday as countries split over fossil fuels. (Reuters)"),
    ("poland", "2 POLAND · NATO",
     "Russian missile crashes in Poland as NATO jets scramble",
     "A Russian Kh-101 missile comes down in south-east Poland during a large "
     "attack on Ukraine; NATO scrambles jets. (Reuters)"),
    ("icj", "3 THE HAGUE · JUSTICE",
     "ICJ rules Myanmar committed genocide against the Rohingya",
     "The court rules 9–6 that Myanmar committed genocide in 2017 and orders "
     "inquiry and compensation; Myanmar rejects it. (AP)"),
]

MED = [
    ("riyadh", "4 RIYADH · CONFLICT",
     "Coalition downs three Houthi missiles over Riyadh",
     "Three missiles fired at the capital destroyed; third night of alerts. (Reuters)"),
    ("nvidia", "5 SANTA CLARA · TECH",
     "SEC examines Nvidia's books as shares slide 13.8%",
     "Regulator probes accounting issues as the chip stock falls sharply. (CNBC)"),
    ("kharg", "6 KHARG ISLAND · ENERGY",
     "Fourteen Iranian tankers mass at Kharg Island",
     "Tankers prepare to sail as a convoy to test a US blockade. (Reuters)"),
    ("yemen", "7 YEMEN · CONFLICT",
     "Saudi–Houthi fighting escalates across Yemen",
     "Strikes hit four cities; claims put the dead at 41, including 11 children. (AP)"),
    ("ukeu", "8 BRUSSELS · POLITICS",
     "UK and EU seal deal to scrap most food checks",
     "Deal drops most food checks and links carbon markets from 2028. (GOV.UK)"),
    ("maths", "9 SAN FRANCISCO · AI",
     "Anthropic may have solved the biggest maths problem",
     "The lab says its model cracked a long-standing maths puzzle. (Reports)"),
    ("kyiv", "10 KYIV · WAR",
     "Russian strike damages Kyiv's WWII museum",
     "Offensive hits the WWII museum days after the Crimean Bridge strike. (Reports)"),
    ("india", "11 NEW DELHI · MARKETS",
     "Record Rs 1.22 lakh crore pours into Indian shares",
     "Foreign investors put a record sum into Indian equities. (Depository data)"),
    ("cricket", "12 WELLINGTON · CRICKET",
     "Rahul completes the SENA set in Wellington",
     "Rahul's century gives him Test hundreds in all four SENA countries. (Scorecard)"),
    ("rikers", "13 NEW YORK · POLITICS",
     "Mamdani sets 2032 to close Rikers Island",
     "Mayor unveils a plan to shut the jail complex by 2032. (Reports)"),
]

BRIEFS = [
    ("NEW YORK", "Trump calls for Nvidia to reinstate 'brilliant' Jensen Huang", "AP"),
    ("WASHINGTON", "Trump threatens tax on US firms building AI data centres abroad", "Reuters"),
    ("EUROPE", "Gen Z protests sweep 25 countries over wars, costs and climate", "Al Jazeera"),
    ("COPENHAGEN", "Denmark expels Russian diplomat over alleged plot to kill rapper", "Al Jazeera"),
    ("PARIS", "French police sentenced for beating music producer Michel Zecler", "Reports"),
    ("NEW DELHI", "Nepal's PM begins first foreign visit in Delhi", "PTI"),
    ("TAIPEI", "Taiwan reports China-linked accounts to Meta over election meddling", "Reports"),
    ("KYIV", "Russia targets Kyiv crossings days after Ukraine hits Crimean Bridge", "Reports"),
    ("GAZA", "Displaced children celebrate World Children's Day", "Al Jazeera"),
    ("GAZA", "Israeli drone attacks kill seven Palestinians in central Gaza", "Al Jazeera"),
    ("STRAIT OF HORMUZ", "IRGC claims it downed a US MQ-9 drone", "Al Jazeera"),
    ("SOUTH AFRICA", "Nearly 600 women killed within three months", "Reports"),
    ("JOHANNESBURG", "ANC scrambles after worst result since 1994", "BBC"),
    ("CONGO", "Ebola crisis hits children as ~100 schools close", "Reports"),
    ("RABAT", "Morocco commits €366m to a defence manufacturing base", "Reports"),
    ("NIGERIA", "Boat carrying mourners to a funeral capsizes, four dead", "Al Jazeera"),
    ("CALIFORNIA", "State subpoenas Nvidia over possible China chip sales", "Reports"),
    ("WASHINGTON", "US declassifies more UFO footage filmed in the Middle East", "Reports"),
    ("SAN SALVADOR", "Bukele seeks a third term that could keep him in power to 2033", "Reports"),
    ("HAITI", "Two Salvadoran soldiers killed handling explosives", "Al Jazeera"),
    ("PRAGUE", "Czechia weighs a faster air-defence buildup", "Reports"),
    ("TALLINN", "Estonia to close crossings along Russia from 1 December", "Reports"),
    ("BRUSSELS", "EU Council provides €1bn in military aid to Ukraine", "Reports"),
]

STATS = [
    ("0", "climate deal agreed at COP31"),
    ("14", "Iranian tankers massing at Kharg Island"),
    ("100,000", "people in the UK–EU youth mobility scheme"),
    ("Rs 1.22 lakh cr", "record foreign money into Indian shares"),
    ("600", "women killed in South Africa in three months"),
    ("3", "Houthi missiles downed over Riyadh"),
]

REGIONS = [
    ("Europe", 10, (31, 78, 156)),
    ("North America", 6, (192, 57, 43)),
    ("Middle East", 6, (180, 140, 20)),
    ("Asia", 6, (123, 45, 139)),
    ("Africa", 5, (30, 132, 73)),
    ("Latin America", 2, (211, 84, 0)),
    ("Oceania", 1, (22, 160, 133)),
]

# pins on the cropped map: (x fraction, y fraction, story number)
PINS = [
    (0.562, 0.309, 1), (0.521, 0.154, 2), (0.485, 0.120, 3),
    (0.605, 0.440, 4), (0.175, 0.315, 5), (0.615, 0.380, 6),
    (0.590, 0.530, 7), (0.465, 0.200, 8), (0.135, 0.240, 9),
    (0.552, 0.160, 10), (0.677, 0.404, 11), (0.920, 0.880, 12),
    (0.245, 0.261, 13),
]

LEFT_OUT = [
    ("Wall Street enters correction", "Fri 20 Nov"),
    ("6.8 quake shakes Peru", "Fri 20 Nov"),
    ("Cyclone Akvan landfall, Odisha", "Fri 20 Nov"),
    ("Russia's missile wave on Kyiv", "Fri 20 Nov"),
    ("Shenzhen summit (Trump–Xi)", "Thu 19 Nov"),
    ("Trump: Iran wants a deal", "Thu 19 Nov"),
]


def main():
    page = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(page)
    mx = 28
    cw = W - 2 * mx

    # top strip
    d.text((mx, 8), "THE WORLD IN ONE DAY", font=font("sans", 11, True), fill=RED)
    right = "36 STORIES · 7 REGIONS · EVERY ONE DATED SATURDAY 21 NOVEMBER 2026"
    d.text((W - mx - d.textlength(right, font=font("sans", 10, True)), 9),
           right, font=font("sans", 10, True), fill=INK)
    d.line([(mx, 26), (W - mx, 26)], fill=RULE, width=2)

    # headline + sub-headline
    d.text((mx, 30), "Saturday 21 November 2026", font=font("serif", 50, True), fill=INK)
    d.text((mx, 84), "COP31 runs into overtime · Missile crashes in Poland · "
           "ICJ: Myanmar guilty of genocide · Riyadh downs three missiles",
           font=font("serif", 14), fill=GREY)
    d.line([(mx, 106), (W - mx, 106)], fill=RULE, width=1)

    # stats strip
    col = cw // 6
    for i, (num, label) in enumerate(STATS):
        x = mx + i * col
        d.text((x, 112), num, font=font("serif", 23, True), fill=INK)
        text_block(d, x, 138, wrap(d, label, font("sans", 8), col - 8),
                   font("sans", 8), GREY, 10)
    d.line([(mx, 166), (W - mx, 166)], fill=RULE, width=1)

    # region bar + legend
    total = sum(n for _, n, _ in REGIONS)
    x = mx
    for _, n, color in REGIONS:
        wseg = int(cw * n / total)
        d.rectangle([x, 172, x + wseg - 1, 180], fill=color)
        x += wseg
    lx = mx
    for name, n, color in REGIONS:
        d.rectangle([lx, 186, lx + 8, 194], fill=color)
        lx += 11
        s = f"{name} {n}"
        d.text((lx, 184), s, font=font("sans", 9, True), fill=INK)
        lx += int(d.textlength(s, font=font("sans", 9, True))) + 12

    # big features
    bw = (cw - 24) // 3
    by = 206
    for i, (img, kicker, head, deck) in enumerate(BIG):
        x = mx + i * (bw + 12)
        page.paste(fit(os.path.join(ASSETS, img + ".webp"), bw, 92), (x, by))
        if i == 0:
            d.rounded_rectangle([x + 6, by + 6, x + 78, by + 26], radius=3, fill=RED)
            d.text((x + 12, by + 9), "NO DEAL", font=font("sans", 11, True), fill=(255, 255, 255))
        y = by + 98
        d.text((x, y), kicker, font=font("sans", 9, True), fill=RED)
        y += 12
        y = text_block(d, x, y, wrap(d, head, font("serif", 16, True), bw),
                       font("serif", 16, True), INK, 17)
        text_block(d, x, y + 2, wrap(d, deck, font("sans", 10), bw),
                   font("sans", 10), INK, 11)

    # medium rows
    mw = (cw - 48) // 5
    for row in range(2):
        my = 378 + row * 128
        for j in range(5):
            img, kicker, head, deck = MED[row * 5 + j]
            x = mx + j * (mw + 12)
            page.paste(fit(os.path.join(ASSETS, img + ".webp"), mw, 60), (x, my))
            y = my + 66
            d.text((x, y), kicker, font=font("sans", 8, True), fill=RED)
            y += 11
            y = text_block(d, x, y, wrap(d, head, font("serif", 11, True), mw),
                           font("serif", 11, True), INK, 12)
            text_block(d, x, y + 1, wrap(d, deck, font("sans", 8), mw),
                       font("sans", 8), INK, 10)

    # also-on bar
    d.rectangle([mx, 638, W - mx, 654], fill=NAVY)
    d.text((mx + 10, 643), "ALSO ON SATURDAY 21 NOVEMBER — 23 MORE STORIES",
           font=font("sans", 11, True), fill=(255, 255, 255))

    # briefs, two columns
    by = 662
    half = cw // 2
    for idx, (city, head, src) in enumerate(BRIEFS):
        col_i = 0 if idx < 12 else 1
        row_i = idx if idx < 12 else idx - 12
        x = mx + col_i * half
        y = by + row_i * 13
        num = 14 + idx
        line = f"{num} {city} — {head} ({src})"
        d.text((x, y), line, font=font("sans", 9), fill=INK)

    # bottom: map + date check
    d.text((mx, 826), "WHERE IT HAPPENED", font=font("sans", 11, True), fill=INK)
    mapw, maph = 470, 148
    mmap = Image.open(os.path.join(ASSETS, "map.webp")).convert("RGB")
    mw0, mh0 = mmap.size
    mmap = mmap.crop((0, 120, mw0, 962))
    mmap = mmap.resize((mapw, maph), Image.LANCZOS)
    page.paste(mmap, (mx, 842))
    d2 = ImageDraw.Draw(page)
    for fx, fy, num in PINS:
        px, py = mx + int(fx * mapw), 842 + int(fy * maph)
        d2.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED,
                   outline=(255, 255, 255), width=1)
        s = str(num)
        d2.text((px - d2.textlength(s, font=font("sans", 7, True)) / 2, py - 5),
                s, font=font("sans", 7, True), fill=(255, 255, 255))
    d.text((mx, 994), "Pins 1–13 mark the drawn stories.",
           font=font("sans", 8), fill=GREY)

    bx = mx + 500
    bw2 = W - mx - bx
    d.rectangle([bx, 826, W - mx, 990], outline=RED, width=2)
    d.text((bx + 10, 832), "DATE CHECK — WHAT WE LEFT OUT",
           font=font("sans", 11, True), fill=RED)
    y = 854
    for item, when in LEFT_OUT:
        d.text((bx + 10, y), "×", font=font("sans", 10, True), fill=RED)
        d.text((bx + 26, y), item, font=font("sans", 10), fill=INK)
        wlen = d.textlength(when, font=font("sans", 10, True))
        d.text((W - mx - 10 - wlen, y), when, font=font("sans", 10, True), fill=GREY)
        y += 20
    d.text((bx + 10, y + 4), "Also Fri: Kyiv bridge · ICJ ruling · Oman tanker fire · "
           "SCO forum opens · Houthi workshops.",
           font=font("sans", 8), fill=GREY)

    # footer
    d.text((mx, 1006), "Every story here happened, or was first reported, on "
           "Saturday 21 November 2026. Sources named beside each story. "
           "Original drawings, not photographs.",
           font=font("serif", 10), fill=GREY)

    page.save(os.path.join(HERE, "entry.png"), "PNG")
    print("wrote entry.png", os.path.getsize(os.path.join(HERE, "entry.png")))


if __name__ == "__main__":
    main()
