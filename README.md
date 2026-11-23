# World Briefing

An illustrated news front page for the make.fun competition **news-image-20261122**, covering events and reports from Sunday 22 November 2026.

[![make.fun news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/AARenor/makefun-news-22/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/AARenor/makefun-news-22/reward.svg)](https://make.fun/bounty/news-image-20261122)

## Stories

All sources below are dated 22 November 2026. The picture distinguishes the COP31 cover pact from other decisions made at the conference. It describes the Libya attack as suspected, not confirmed.

1. **Climate:** COP31's proposed cover pact was rejected after the EU and other countries objected to the absence of fossil fuel language. [Euronews](https://www.euronews.com/2026/11/22/cop31-climate-talks-fail-after-eu-and-others-reject-final-deal-proposal), 22 November 2026. [IISD's conference report](https://enb.iisd.org/antalya-un-climate-change-conference-cop31-22Nov2026), 22 November 2026, records other decisions the meeting did adopt.
2. **Ukraine:** President Volodymyr Zelenskyy urged the United States to approve the delivery of Patriot interceptor missiles. [Al Jazeera](https://www.aljazeera.com/news/2026/11/22/zelenskyy-urges-us-to-release-patriot-missiles), 22 November 2026.
3. **Sudan:** Drone strikes killed at least four people near Khartoum and damaged a United Nations building. [The Rio Times](https://www.riotimesonline.com/sudan-drones-hit-khartoum-un-building-nov-2026/) and [Al Jazeera with AFP](https://www.aljazeera.com/news/2026/11/22/rsf-drones-kill-four-in-khartoum), both 22 November 2026.
4. **Libya:** A Russian ship exploded in Benghazi. Libya's eastern government suspected a drone attack. [Al Arabiya English, with Reuters](https://english.alarabiya.net/News/africa/2026/11/22/libya-s-eastern-government-suspects-drone-attack-caused-explosion-on-russian-ship), published 22 November 2026.
5. **South Korea:** Education Minister Choi Kyo-jin resigned following criticism of the handling of fears of AI assisted cheating ahead of university entrance exams. [The Hindu, reporting AFP](https://www.thehindu.com/news/international/south-korea-education-minister-resigns-amid-ai-cheating-scandal/article71730601.ece), 22 November 2026.
6. **Chess:** At the world championship opening ceremony in Geneva, Javokhir Sindarov drew white for the first game against champion Gukesh Dommaraju. The game itself was scheduled for 24 November. [Chess.com](https://www.chess.com/news/view/2026-fide-chess-world-championship-opening-ceremony), 22 November 2026.

## Run

Run `python3 main.py` locally to write `out/entry.png`. In the make.fun container, the same program writes `/output/entry.png`. The `MAKEFUN_OUTPUT_DIR` environment variable can select another output folder. The entrypoint uses only Python's standard library and does not access the network.

`artwork.py` is the offline design source. It recreates the checked in image with Pillow and the DejaVu fonts installed on the design machine. Pillow is not needed to run the competition entry.

MIT license.
