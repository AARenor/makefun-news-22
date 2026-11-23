# World Briefing

A dense news front page for the make.fun competition **news-image-20261122**, covering events and reports from Sunday 22 November 2026.

[![make.fun news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/AARenor/makefun-news-22/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard)
[![reward](https://make.fun/badge/news-image-20261122/AARenor/makefun-news-22/reward.svg)](https://make.fun/bounty/news-image-20261122)

## Stories

These are the twenty-two stories supplied for the briefing, in image reading order. The image preserves the supplied facts; this rebuild does not independently verify the reports.

1. **Europe:** COP31 collapses. Fossil-fuel deadlock ends UN talks with no deal in Antalya.
2. **Europe:** France protests again. Sixth weekend of cost-of-living marches; clashes in Paris.
3. **Europe:** EU and Indonesia sign. Trade deal after ten years ends 98.5 percent of tariffs.
4. **Europe:** Finland airspace breach. Helsinki suspects a Russian helicopter crossed its airspace.
5. **Africa:** Russian ship sunk. Sea drones sink the corvette Merkury at Benghazi port.
6. **Africa:** Malta-flagged ship hit. A second drone attack strikes a merchant ship off Benghazi.
7. **Africa:** Drones hit Sudan. Sudan's army blames Ethiopia for strikes damaging a UN building.
8. **Africa:** Nigeria boat disaster. At least 24 mourners died when their boat capsized.
9. **Africa:** Kenya internet metering. Proposed law would meter internet use; privacy fears grow.
10. **Asia:** Korea minister quits. Education minister resigns over AI-cheating exam row.
11. **Asia:** Bangladesh unrest. Garment wage protests spread; thousands of border guards deploy.
12. **Asia:** Rajasthan crashes. Two road accidents in Rajasthan kill twelve people.
13. **Asia:** Indonesia factory fire. Three dead and 36 missing in a Serang confectionery fire.
14. **Asia:** Golden Horse Awards. A Hong Kong film wins best feature in Taipei.
15. **Middle East:** Bahrain strike wounds two. Bahrain says Iranian strikes injured two people.
16. **Middle East:** Settlers attack villages. Israeli settlers set fires in Palestinian villages; Eisenkot condemns.
17. **Middle East:** Hormuz tankers ablaze. Iran's navy says tankers breaking its rules were set alight.
18. **Americas:** Democrats reach 258. Biggest House majority since 1992 after a North Carolina recount.
19. **Americas:** East Coast storm. Heavy rain floods roads along the I-95 corridor before Thanksgiving.
20. **Americas:** Brazil thunderstorm. Five killed and 250 hurt in Tupancireta, Rio Grande do Sul.
21. **Sport and culture:** Alcaraz takes ATP Finals. He beats Zverev 6-2, 7-6 to win his first title.
22. **Sport and culture:** Marquez seals eighth title. Eighth MotoGP crown equals Agostini's record.

## Run

Run `python3 main.py` locally to write `out/entry.png`. In the make.fun container, the same program writes `/output/entry.png`. The `MAKEFUN_OUTPUT_DIR` environment variable can select another output folder. The entrypoint uses only Python's standard library and does not access the network.

`artwork.py` is the offline design source. It recreates the checked in image with Pillow and the DejaVu fonts installed on the design machine. Pillow is not needed to run the competition entry.

MIT license.
