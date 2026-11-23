import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


@dataclass(frozen=True)
class Story:
    region: str
    headline: str
    fact: str


STORIES = [
    Story("EUROPE", "COP31 collapses", "Fossil-fuel deadlock ends UN talks with no deal in Antalya."),
    Story("EUROPE", "France protests again", "Sixth weekend of cost-of-living marches; clashes in Paris."),
    Story("EUROPE", "EU and Indonesia sign", "Trade deal after ten years ends 98.5 percent of tariffs."),
    Story("EUROPE", "Finland airspace breach", "Helsinki suspects a Russian helicopter crossed its airspace."),
    Story("AFRICA", "Russian ship sunk", "Sea drones sink the corvette Merkury at Benghazi port."),
    Story("AFRICA", "Malta-flagged ship hit", "A second drone attack strikes a merchant ship off Benghazi."),
    Story("AFRICA", "Drones hit Sudan", "Sudan's army blames Ethiopia for strikes damaging a UN building."),
    Story("AFRICA", "Nigeria boat disaster", "At least 24 mourners died when their boat capsized."),
    Story("AFRICA", "Kenya internet metering", "Proposed law would meter internet use; privacy fears grow."),
    Story("ASIA", "Korea minister quits", "Education minister resigns over AI-cheating exam row."),
    Story("ASIA", "Bangladesh unrest", "Garment wage protests spread; thousands of border guards deploy."),
    Story("ASIA", "Rajasthan crashes", "Two road accidents in Rajasthan kill twelve people."),
    Story("ASIA", "Indonesia factory fire", "Three dead and 36 missing in a Serang confectionery fire."),
    Story("ASIA", "Golden Horse Awards", "A Hong Kong film wins best feature in Taipei."),
    Story("MIDDLE EAST", "Bahrain strike wounds two", "Bahrain says Iranian strikes injured two people."),
    Story("MIDDLE EAST", "Settlers attack villages", "Israeli settlers set fires in Palestinian villages; Eisenkot condemns."),
    Story("MIDDLE EAST", "Hormuz tankers ablaze", "Iran's navy says tankers breaking its rules were set alight."),
    Story("AMERICAS", "Democrats reach 258", "Biggest House majority since 1992 after a North Carolina recount."),
    Story("AMERICAS", "East Coast storm", "Heavy rain floods roads along the I-95 corridor before Thanksgiving."),
    Story("AMERICAS", "Brazil thunderstorm", "Five killed and 250 hurt in Tupancireta, Rio Grande do Sul."),
    Story("SPORT AND CULTURE", "Alcaraz takes ATP Finals", "He beats Zverev 6-2, 7-6 to win his first title."),
    Story("SPORT AND CULTURE", "Marquez seals eighth title", "Eighth MotoGP crown equals Agostini's record."),
]

PALETTE = {
    "EUROPE": "#2f8f8a",
    "AFRICA": "#b4563a",
    "ASIA": "#4a58a8",
    "MIDDLE EAST": "#a8323c",
    "AMERICAS": "#2f6fa8",
    "SPORT AND CULTURE": "#b8862f",
}


def draw_masthead(image):
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1023, 149), fill="#16181d")
    font = ImageFont.truetype(FONT_BOLD, 15)
    x = 44
    for letter in "WORLD BRIEFING":
        draw.text((x, 22), letter, font=font, fill="#cdc7b6")
        x += draw.textlength(letter, font=font) + 3
    date = "SUNDAY 22 NOVEMBER 2026"
    size = 60
    while True:
        font = ImageFont.truetype(FONT_BOLD, size)
        if draw.textlength(date, font=font) <= 940:
            break
        size -= 1
    draw.text((44, 48), date, font=font, fill="#fbf8ee")
    draw.line((44, 120, 980, 120), fill="#4a4d54")
    font = ImageFont.truetype(FONT_REGULAR, 11)
    draw.text((44, 128), "THE DAY IN TWENTY-TWO STORIES / SIX REGIONS", font=font, fill="#cdc7b6")
    draw.text((980, 128), "EVENTS AND REPORTS FROM 22 NOVEMBER 2026", anchor="ra", font=font, fill="#cdc7b6")


def draw_footer(image):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_REGULAR, 10)
    draw.text((44, 990), "Sources: Reuters / Al Jazeera / CNN / The Guardian / Middle East Eye / The World in Summary", font=font, fill="#5b5e66")
    draw.text((980, 990), "22 NOVEMBER 2026", anchor="ra", font=font, fill="#5b5e66")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path(__file__).with_name("entry.png"))
    args = parser.parse_args()
    from rows import draw_rows

    image = Image.new("RGB", (1024, 1024), "#f1ece0")
    draw_masthead(image)
    draw_rows(image)
    draw_footer(image)
    image.save(args.out, format="PNG")
    print(f"wrote {args.out}: {image.width}x{image.height}, {args.out.stat().st_size} bytes", file=sys.stderr)


if __name__ == "__main__":
    main()
