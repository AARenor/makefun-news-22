from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


@dataclass(frozen=True)
class Story:
    region: str
    headline: str
    fact: str

STORIES: list[Story] = [
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

COLORS = {
    "EUROPE": "#2f8f8a", "AFRICA": "#b4563a", "ASIA": "#4a58a8",
    "MIDDLE EAST": "#a8323c", "AMERICAS": "#2f6fa8",
    "SPORT AND CULTURE": "#936714",
}
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")), size)


def tracked(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, face: ImageFont.FreeTypeFont, fill: str, spacing: int) -> None:
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=face, fill=fill, anchor="lt")
        x += draw.textlength(char, font=face) + spacing


def wrap(draw: ImageDraw.ImageDraw, text: str, face: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    for word in text.split():
        candidate = f"{lines[-1]} {word}" if lines else word
        if lines and draw.textlength(candidate, font=face) <= width:
            lines[-1] = candidate
        else:
            if draw.textlength(word, font=face) > width:
                raise ValueError(f"Word does not fit: {word}")
            lines.append(word)
    return lines


def render(out: Path) -> Path:
    if len(STORIES) != 22:
        raise ValueError("Exactly 22 stories required")
    image = Image.new("RGB", (1024, 1024), "#f1ece0")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1023, 149), fill="#16181d")
    tracked(draw, (44, 22), "WORLD BRIEFING", font(15, True), "#cdc7b6", 3)
    title = "SUNDAY 22 NOVEMBER 2026"
    title_size = 54
    while draw.textlength(title, font=font(title_size, True)) > 936:
        title_size -= 1
    draw.text((44, 48), title, font=font(title_size, True), fill="#fbf8ee", anchor="lt")
    draw.line((44, 120, 980, 120), fill="#4a4d54")
    draw.text((44, 128), "THE DAY IN TWENTY-TWO STORIES · SIX REGIONS", font=font(11), fill="#cdc7b6", anchor="lt")
    draw.text((980, 128), "EVENTS AND REPORTS FROM 22 NOVEMBER 2026", font=font(11), fill="#cdc7b6", anchor="rt")
    headline_font, fact_font = font(17, True), font(12)
    for index, story in enumerate(STORIES):
        x = 44 if index < 11 else 518
        top = 150 + (index % 11) * 75
        color = COLORS[story.region]
        if index % 11:
            draw.line((x, top, x + 462, top), fill="#ddd6c4")
        draw.rectangle((x, top + 6, x + 3, top + 68), fill=color)
        tracked(draw, (x + 14, top + 6), story.region, font(10, True), color, 2)
        headlines = wrap(draw, story.headline, headline_font, 444)
        facts = wrap(draw, story.fact, fact_font, 444)
        if len(headlines) > 2 or len(facts) > 2:
            raise ValueError(f"Too many lines: {story.headline}")
        y = top + 22
        for line in headlines:
            draw.text((x + 14, y), line, font=headline_font, fill="#1b1d22", anchor="lt")
            y += 19
        y += 2
        for line in facts:
            draw.text((x + 14, y), line, font=fact_font, fill="#33363d", anchor="lt")
            y += 14
        if y > top + 75:
            raise ValueError(f"Row overflow: {story.headline}")
    draw.text((44, 990), "Sources: Reuters · Al Jazeera · CNN · The Guardian · Middle East Eye · The World in Summary", font=font(10), fill="#5b5e66", anchor="lt")
    draw.text((980, 990), "22 NOVEMBER 2026", font=font(10), fill="#5b5e66", anchor="rt")
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.png"
    image.save(target, format="PNG", optimize=False, compress_level=9)
    print(f"wrote {target} ({target.stat().st_size} bytes, 1024x1024 RGB)", file=sys.stderr)
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    render(parser.parse_args().out)


if __name__ == "__main__":
    main()
