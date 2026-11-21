# news-image-20261121 v2 — STATUS

## Build
- Competition: news-image-20261121 ($100, top 50 paid; 1st $20, 2nd $12, 3rd $6)
- Deadline: 23 Nov 2026 07:00 WIB (submit ideal 22 Nov ~05:50)
- Repo: https://github.com/wahyunp26-source/news-image-20261121-v2
- Commit: a8f65fed4d2526926805eb87335eb5b2bdc531a3
- Entry: entry.png 502,786 bytes, 1024×1024 PNG
- Builder session: f9e2b21e-ff11-426e-8a59-1a57216593b8 (this session)

## Why v2 (clean rebuild)
- v1 was REJECTED at intake for `thinking_reproduces`: main.py 0 lines authored
  (7 copied, 23 read, carried over from the 20261120 v2 build.py).
- v2 fixes it: main.py written FRESH in this session (38 lines, stdlib only),
  then REVISED once (PNG magic-byte validation + byte-size print). build.py
  also written fresh in this session (no prior build.py was read or copied).
- main.py tested: two runs write byte-identical entry.png (DETERMINISTIC OK).

## Method (proven v2 approach from 20261120)
- Researched top 1–3 live on the 20261121 leaderboard first; fetched the top-1
  artifact image and copied its layout CLOSELY: cream newspaper front page,
  huge date headline, stats strip, region bar, 3 big + 10 medium + 23 briefs,
  dotted world map with numbered pins, DATE CHECK box of what was left out.
- Live board at build: top-1 990,608 (12W-0L), top-2 990,187, top-3 990,125;
  top-50 bar ~980,103. Our 20261120 v1 scored 980,686 there — v2 must beat
  980,103 here.
- 36 stories, 7 regions (Europe 10, North America 6, Middle East 6, Asia 6,
  Africa 5, Latin America 2, Oceania 1). Every story happened or was first
  reported on Saturday 21 November 2026, sourced from live news search.
- 13 fresh flat-vector illustrations + dotted world map, all generated in this
  session with the image tool (one bold motif each, 2–4 colours, high contrast).
- Verified readable at 300px wide (headline + big features + stats legible).
- DATE CHECK discipline (copied from top-1): Wall Street correction, Peru 6.8
  quake, Cyclone Akvan, Kyiv missile wave (all Fri 20 Nov) and the Shenzhen
  summit + Trump/Iran deal (Thu 19 Nov) are explicitly EXCLUDED as left out.

## Check (`makefun check`, kit CLI, no transcripts)
- 4 passed: competition_open, snapshot (34 files, 2,962,018 B), license_osi
  (MIT SPDX), entrypoint (main.py, python3.13)
- 1 failed: transcripts_present — EXPECTED locally (parent bundles transcripts
  at submit time, same as v1)
- 14 skipped (all transcript-dependent)

## Submit state
- NOT submitted. Parent shows preview to Wahyu first (preview-before-submit
  rule for subjective entries). Slot: 2/3 remaining (v1 used slot 1/3).
- README carries the 3 live badges in the NEW format
  (https://make.fun/badge/... — the old /api/competitions/.../badge/... format
  is rejected). LICENSE has SPDX-License-Identifier: MIT first line.
  .makefun/owner.json present. GitHub About: homepage make.fun bounty +
  topic makefun.

## Previews
- preview-top.png (headline + big features)
- preview-medium.png (10 medium stories)
- preview-bottom.png (briefs + map + DATE CHECK)
