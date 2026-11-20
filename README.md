# world-news-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/makaide76-star/world-news-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/makaide76-star/world-news-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up the world's news of Friday 20 November 2026 — the first Trump–Xi–Putin summit in Shenzhen, the World Court's genocide verdict against Myanmar, the AI sell-off on world markets, strikes on Riyadh and Kyiv, and the COP31 fossil-fuel row — composed as a newspaper front page by a deterministic Python program.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.png` (1024×1024 PNG, under 1 MiB). No network, no
dependencies beyond the Python 3 standard library, and every run writes
identical bytes.

## How the image was made

`tools/make_image.py` draws `assets/entry.png` with PIL from the day's
wire headlines, cross-checked across SCMP, Dawn, Bangkok Post, China
Times and OneTurn's daily digest of 20 November 2026. `main.py` ships
that image, which is the layout the headlines were composed into.

---

<sub>Entered on [make.fun](https://make.fun/?ref=cskmaypt&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
