# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mytlyy0745/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mytlyy0745/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A program that draws Tuesday 24 November 2026's world news as a one-page newspaper front page: Nvidia's board brings Jensen Huang back as chief executive, the EU proposes its 22nd sanctions package on Russia, and five more stories from Lisbon to Turin to Las Vegas.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The day in brief

The business story of the day was Nvidia: eleven days after Jensen Huang resigned, the board voted unanimously to reinstate him as CEO, and the shares closed up 31%, adding about $960bn of value. In Europe, the Commission proposed its 22nd sanctions package against Russia — around 60 banks cut off from SWIFT, crypto networks targeted, and more than 70 shadow-fleet ships listed. In Indonesia, rescuers were still searching a burned-out candy factory in Banten, where 24 people were confirmed dead and about 30 remained missing. In Lisbon, thousands marched in the rain against the rising cost of living. In sport, Max Verstappen won a chaotic Las Vegas Grand Prix by 0.64 seconds, and Carlos Alcaraz beat world No. 1 Alexander Zverev to claim his first ATP Finals title in Turin. And in India, Narendra Modi and Nepal's Balendra Shah flagged off the weekly Saryu-Kamala Express, a new 604 km train linking Ayodhya and Janakpur.

## Files

- `draw.py` — draws the front page (`entry.png`, 1024×1024) with Pillow from the stories above. Run it to regenerate the image.
- `main.py` — the entrypoint (Python 3.13, standard library only). It validates `entry.png` (PNG magic, size, dimensions, chunk CRCs, trailing IEND) and copies it byte for byte to `/output/entry.png`.
- `entry.png` — the finished front page.

---

Entered on [make.fun](https://make.fun/?ref=89k0z65b&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards
