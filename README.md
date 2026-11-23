# World Briefing

A dense news front page for the make.fun competition **news-image-20261122**, covering events and reports from Sunday 22 November 2026.

[![make.fun news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/AARenor/makefun-news-22/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/AARenor/makefun-news-22/reward.svg)](https://make.fun/bounty/news-image-20261122)

## Stories

The requested briefing treats all items as reports from 22 November 2026; source dates are not all independently confirmed. The supplied source list names Reuters, Al Jazeera, CNN, The Guardian, Middle East Eye, Cape Times, AllAfrica and Weather.com without mapping outlets to stories. Unconfirmed attributions and inaccessible pages are marked below. The requested headlines are preserved.

1. **Europe:** COP31 collapses ([CNN](https://www.cnn.com/2026/11/22/climate/cop31-summit-collapses-in-fossil-fuel-failure)).
2. **Europe:** France protests again ([France 24](https://www.france24.com/en/asia-pacific/20261122-the-week-in-pictures-xi-hosts-trump-and-putin-cop31-and-more-french-protests)).
3. **Europe:** Poland house fire ([Xinhua, citing PAP](https://english.news.cn/20261122/bcadd59be9824a18b96cdca9f67305e5/c.html)).
4. **Europe:** Gen Z protests widen (supplied briefing; outlet attribution unverified).
5. **Africa:** Russian ship sunk ([Al Jazeera](https://www.aljazeera.com/news/2026/11/22/suspected-drone-strike-hits-russian-vessel-in-libya)).
6. **Africa:** Malta-flagged ship hit (supplied briefing; outlet attribution unverified).
7. **Africa:** Drones hit Sudan ([Al Jazeera](https://www.aljazeera.com/news/2026/11/22/rsf-drones-kill-four-in-khartoum)).
8. **Africa:** Nigeria boat disaster ([P.M. News](https://pmnewsnigeria.com/2026/11/22/bayelsa-boat-disaster-fg-moves-to-uncover-cause)).
9. **Africa:** Women's Shutdown ([Women For Change](https://womenforchange.co.za/magazine/wfc-announces-womens-shutdown-2026/), published 21 October 2026 for the action on 21 November 2026).
10. **Africa:** Malawi protests (supplied briefing; outlet attribution unverified).
11. **Asia:** Korea minister quits ([The Korea Times](https://koreatimes.co.kr/southkorea/education/20261122/education-minister-resigns-amid-backlash-over-csat-anti-cheating-measures)).
12. **Asia:** Bangladesh unrest (supplied briefing; outlet attribution unverified).
13. **Asia:** Rajasthan crashes ([NewsBytes](https://newsbytesapp.com/news/india/two-rajasthan-road-crashes-kill-12-several-injured-sunday/tldr)).
14. **Asia:** Indonesia factory fire ([DW](https://www.dw.com/en/dozens-missing-as-deadly-fire-hits-indonesian-candy-factory/a-80012342)).
15. **Asia:** Golden Horse Awards ([Taipei Golden Horse Film Festival](https://www.goldenhorse.org.tw/awards/ceremony/info/?r=en), ceremony on 22 November 2026; publication date unconfirmed).
16. **Asia:** Bahrain strike wounds two ([Middle East Eye](https://www.middleeasteye.net/live-blog/live-blog-update/bahrain-says-iranian-strike-wounds-two-one-critically), publication date unconfirmed).
17. **Americas:** Democrats reach 258 ([The Washington Post](https://www.washingtonpost.com/politics/2026/11/22/house-democrats-will-have-largest-majority-21st-century-after-latest-race-call/)).
18. **Americas:** East Coast storm ([East Idaho News](https://www.eastidahonews.com/2026/11/east-coast-storm-could-disrupt-holiday-travel-after-battering-florida/), page inaccessible).
19. **Americas:** Brazil thunderstorm (supplied briefing; outlet attribution unverified).
20. **Americas:** Peru quake (supplied briefing; outlet attribution unverified).
21. **Sport and culture:** Alcaraz takes ATP Finals ([Reuters](https://www.reuters.com/sports/tennis/alcaraz-charges-past-world-number-one-zverev-clinch-atp-finals-title-2026-11-22/), page inaccessible).
22. **Sport and culture:** Marquez seals eighth title ([Reuters](https://www.reuters.com/sports/marquez-wins-eighth-motogp-title-portugal-2026-11-22/), page inaccessible).

## Run

Run `python3 main.py` locally to write `out/entry.png`. In the make.fun container, the same program writes `/output/entry.png`. The `MAKEFUN_OUTPUT_DIR` environment variable can select another output folder. The entrypoint uses only Python's standard library and does not access the network.

`artwork.py` is the offline design source. It recreates the checked in image with Pillow and the DejaVu fonts installed on the design machine. Pillow is not needed to run the competition entry.

MIT license.
