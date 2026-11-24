# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mytlyy0745/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mytlyy0745/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Sum up 24 November's world news in one image: a newspaper front page for Tuesday 24 November 2026. Nvidia's board votes unanimously to reinstate Jensen Huang as CEO, 11 days after he resigned — Trump pressed the board, and the stock jumps 31%. The EU proposes its 22nd sanctions package on Russia: 60 banks cut from SWIFT, a crypto crackdown, 70+ shadow-fleet ships listed, and a ban on Russian teams competing under the Russian flag at EU events. A factory fire in Banten, Indonesia kills at least 24, with around 30 workers missing. Also: thousands march in Lisbon over the cost of living, Max Verstappen wins the Las Vegas Grand Prix, Carlos Alcaraz takes his first ATP Finals title, and Modi and Nepal PM Balendra Shah flag off the Saryu-Kamala Express train between India and Nepal.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` byte-identical to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It runs offline with the standard library only and writes the same bytes on every run. `draw.py` is the script that drew `entry.png` with PIL.
