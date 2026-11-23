import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
PAPER = "#f1ece0"
DARK = "#16181d"
LIGHT = "#fbf8ee"


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


def masthead(image):
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1023, 149), fill=DARK)
    tracked(draw, (44, 22), "WORLD BRIEFING", load(BOLD, 15), "#cdc7b6", 3)
    title = "SUNDAY 22 NOVEMBER 2026"
    draw.text((44, 48), title, font=fit(draw, title, BOLD, 940, 49), fill=LIGHT)
    draw.line((44, 120, 980, 120), fill="#4a4d54")
    small = load(REGULAR, 11)
    draw.text((44, 128), "THE DAY IN TWENTY-TWO STORIES - SIX REGIONS", font=small, fill="#cdc7b6")
    right(draw, (980, 128), "EVENTS AND REPORTS FROM 22 NOVEMBER 2026", small, "#cdc7b6")


def footer(image):
    draw = ImageDraw.Draw(image)
    font = load(REGULAR, 10)
    sources = "Sources: Reuters - Al Jazeera - CNN - The Guardian - Middle East Eye - The World in Summary"
    draw.text((44, 990), sources, font=fit(draw, sources, REGULAR, 790, 10), fill="#5b5e66")
    right(draw, (980, 990), "22 NOVEMBER 2026", font, "#5b5e66")


def main():
    if __name__ == "__main__":
        sys.modules["artwork"] = sys.modules[__name__]
    from rows import draw_rows

    image = Image.new("RGB", (1024, 1024), PAPER)
    masthead(image)
    draw_rows(image)
    footer(image)
    output = Path(__file__).with_name("entry.png")
    image.save(output, format="PNG")
    print(f"{image.width}x{image.height} RGB; {output.stat().st_size} bytes")


def load(path, size):
    return ImageFont.truetype(path, size)


def fit(draw, text, path, width, size, minimum=8):
    for candidate in range(size, minimum - 1, -1):
        font = load(path, candidate)
        if draw.textlength(text, font=font) <= width:
            return font
    raise ValueError(f"Text exceeds {width} pixels: {text}")


def tracked(draw, position, text, font, colour, spacing):
    start, y = position
    cursor = start
    for index, letter in enumerate(text):
        draw.text((cursor, y), letter, font=font, fill=colour)
        cursor += draw.textlength(letter, font=font)
        if index + 1 < len(text):
            cursor += spacing
    return cursor - start


def right(draw, position, text, font, colour):
    edge, y = position
    origin = edge - draw.textlength(text, font=font)
    draw.text((origin, y), text, font=font, fill=colour)


def wrap(draw, text, font, width, maximum=2):
    lines = []
    current = ""
    for word in text.split():
        proposed = f"{current} {word}" if current else word
        if draw.textlength(proposed, font=font) <= width:
            current = proposed
        else:
            if not current or draw.textlength(word, font=font) > width:
                raise ValueError(f"Word exceeds row width: {word}")
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > maximum:
        raise ValueError(f"Story needs {len(lines)} lines: {text}")
    return lines


if __name__ == "__main__":
    main()
