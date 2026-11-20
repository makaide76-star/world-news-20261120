# The World Today — 20 November 2026 in one image

A program that writes one image summing up the world's news of Friday,
20 November 2026: the first Trump–Xi–Putin summit in Shenzhen, the World
Court's genocide verdict against Myanmar, the AI sell-off on world markets,
strikes on Riyadh and Kyiv, the COP31 fossil-fuel row, and the day's
brighter notes.

## Run

    python3 main.py

Writes `/output/entry.png` (1024×1024 PNG, under 1 MiB). No network, no
dependencies beyond the Python 3 standard library, and every run writes
identical bytes.

## How the image was made

`tools/make_image.py` draws `assets/entry.png` with PIL from the day's
wire headlines (cross-checked across SCMP, Dawn, Bangkok Post, China
Times and OneTurn's daily digest). `main.py` ships that image, which is
the layout the headlines were composed into.
