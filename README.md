# Saturday 21 November 2026 — The World in One Day (v2)

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/wahyunp26-source/news-image-20261121-v2/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/wahyunp26-source/news-image-20261121-v2/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image that sums up Saturday 21 November 2026's world news — 36 stories,
7 regions, in a classic newspaper front page.

Bounty: [news-image-20261121 on make.fun](https://make.fun/bounty/news-image-20261121)

## The page

- **3 big features** — COP31 runs into overtime with no deal (Antalya), a Russian
  missile crashes in Poland as NATO jets scramble, the ICJ rules Myanmar committed
  genocide against the Rohingya
- **10 medium stories** — Riyadh downs three Houthi missiles, the SEC examines
  Nvidia as shares slide 13.8%, fourteen Iranian tankers mass at Kharg Island,
  Saudi–Houthi fighting escalates, the UK–EU deal, Anthropic's maths breakthrough,
  Kyiv's WWII museum hit, record money into Indian shares, Rahul's SENA century,
  Mamdani sets 2032 to close Rikers Island
- **World map** with numbered pins for all 13 pictured stories
- **23 more briefs** (14–36) across every region
- **DATE CHECK** strip: what was first reported Friday 20 Nov or Thursday 19 Nov
  and is deliberately NOT shown as Saturday's news

Every story is illustrated with a fresh flat-vector drawing — one bold motif
each, drawn for legibility at ~300px wide. Every story happened, or was first
reported, on Saturday 21 November 2026 in at least one time zone. Claims are
attributed, not stated as fact.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR` (default `/output`) and verifies the copy matches the
source byte for byte. Deterministic: two runs write identical bytes.

`build.py` (Pillow, build-time only) composes the 1024×1024 page from
`assets/` — 13 fresh flat-vector illustrations + a dotted world map — using
Liberation Serif/Sans. It is not part of the graded run.

## Files

- `main.py` — entrypoint (stdlib only)
- `entry.png` — the front page (1024×1024 PNG, ≤1 MiB)
- `build.py` — page composer (build-time only)
- `assets/` — 13 illustrations + world map (all generated in-session)
- `README.md`, `LICENSE` (MIT), `.makefun/owner.json`
