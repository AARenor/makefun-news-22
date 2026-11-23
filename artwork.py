from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
PAPER = '#f1ece0'
INK = '#1b1d22'
REGION_COLOURS = {
    'EUROPE': '#2f8f8a',
    'AFRICA': '#b4563a',
    'ASIA': '#4a58a8',
    'MIDDLE EAST': '#a8323c',
    'AMERICAS': '#2f6fa8',
    'SPORT AND CULTURE': '#896019',
}


@dataclass(frozen=True)
class Story:
    region: str
    headline: str
    fact: str


STORIES: list[Story] = [
    Story('EUROPE', 'COP31 collapses', 'Fossil-fuel deadlock ends UN talks with no deal in Antalya.'),
    Story('EUROPE', 'France protests again', 'Sixth weekend of cost-of-living marches; clashes in Paris.'),
    Story('EUROPE', 'EU and Indonesia sign', 'Trade deal after ten years ends 98.5 percent of tariffs.'),
    Story('EUROPE', 'Finland airspace breach', 'Helsinki suspects a Russian helicopter crossed its airspace.'),
    Story('AFRICA', 'Russian ship sunk', 'Sea drones sink the corvette Merkury at Benghazi port.'),
    Story('AFRICA', 'Malta-flagged ship hit', 'A second drone attack strikes a merchant ship off Benghazi.'),
    Story('AFRICA', 'Drones hit Sudan', "Sudan's army blames Ethiopia for strikes damaging a UN building."),
    Story('AFRICA', 'Nigeria boat disaster', 'At least 24 mourners died when their boat capsized.'),
    Story('AFRICA', 'Kenya internet metering', 'Proposed law would meter internet use; privacy fears grow.'),
    Story('ASIA', 'Korea minister quits', 'Education minister resigns over AI-cheating exam row.'),
    Story('ASIA', 'Bangladesh unrest', 'Garment wage protests spread; thousands of border guards deploy.'),
    Story('ASIA', 'Rajasthan crashes', 'Two road accidents in Rajasthan kill twelve people.'),
    Story('ASIA', 'Indonesia factory fire', 'Three dead and 36 missing in a Serang confectionery fire.'),
    Story('ASIA', 'Golden Horse Awards', 'A Hong Kong film wins best feature in Taipei.'),
    Story('MIDDLE EAST', 'Bahrain strike wounds two', 'Bahrain says Iranian strikes injured two people.'),
    Story('MIDDLE EAST', 'Settlers attack villages', 'Israeli settlers set fires in Palestinian villages; Eisenkot condemns.'),
    Story('MIDDLE EAST', 'Hormuz tankers ablaze', "Iran's navy says tankers breaking its rules were set alight."),
    Story('AMERICAS', 'Democrats reach 258', 'Biggest House majority since 1992 after a North Carolina recount.'),
    Story('AMERICAS', 'East Coast storm', 'Heavy rain floods roads along the I-95 corridor before Thanksgiving.'),
    Story('AMERICAS', 'Brazil thunderstorm', 'Five killed and 250 hurt in Tupancireta, Rio Grande do Sul.'),
    Story('SPORT AND CULTURE', 'Alcaraz takes ATP Finals', 'He beats Zverev 6-2, 7-6 to win his first title.'),
    Story('SPORT AND CULTURE', 'Marquez seals eighth title', "Eighth MotoGP crown equals Agostini's record."),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    return ImageFont.truetype(str(FONT_DIR / name), size)


def spaced(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str,
           face: ImageFont.FreeTypeFont, fill: str, tracking: int) -> None:
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=face, fill=fill, anchor='lt')
        x += draw.textlength(char, font=face) + tracking


def wrapped(draw: ImageDraw.ImageDraw, text: str,
            face: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    for word in text.split():
        candidate = f'{lines[-1]} {word}' if lines else word
        if lines and draw.textlength(candidate, font=face) <= width:
            lines[-1] = candidate
        else:
            if draw.textlength(word, font=face) > width:
                raise ValueError(f'Word does not fit: {word}')
            lines.append(word)
    return lines


def right(draw: ImageDraw.ImageDraw, y: int, text: str,
          face: ImageFont.FreeTypeFont, fill: str) -> None:
    draw.text((980, y), text, font=face, fill=fill, anchor='rt')


def draw_row(draw: ImageDraw.ImageDraw, story: Story, index: int) -> None:
    column, row = divmod(index, 11)
    x, top = (44 + column * 474), (150 + row * 75)
    colour = REGION_COLOURS[story.region]
    draw.rectangle((x, top + 6, x + 3, top + 69), fill=colour)
    if row:
        draw.line((x, top, x + 462, top), fill='#ddd6c4', width=1)
    text_x = x + 18
    width = 444
    spaced(draw, (text_x, top + 6), story.region, font(10, True), colour, 2)
    headline_face = font(17, True)
    fact_face = font(12)
    headlines = wrapped(draw, story.headline, headline_face, width)
    facts = wrapped(draw, story.fact, fact_face, width)
    if len(headlines) > 2 or len(facts) > 2:
        raise ValueError(f'Too many lines: {story.headline}')
    y = top + 22
    for line in headlines:
        draw.text((text_x, y), line, font=headline_face, fill=INK, anchor='lt')
        y += 19
    y += 2
    for line in facts:
        draw.text((text_x, y), line, font=fact_face, fill='#33363d', anchor='lt')
        y += 14
    if y > top + 75:
        raise ValueError(f'Row overflows: {story.headline}')


def masthead(draw: ImageDraw.ImageDraw) -> None:
    draw.rectangle((0, 0, 1023, 149), fill='#16181d')
    spaced(draw, (44, 22), 'WORLD BRIEFING', font(15, True), '#cdc7b6', 3)
    title = 'SUNDAY 22 NOVEMBER 2026'
    size = 54
    while draw.textlength(title, font=font(size, True)) > 940:
        size -= 1
    draw.text((44, 48), title, font=font(size, True), fill='#fbf8ee', anchor='lt')
    draw.line((44, 120, 980, 120), fill='#4a4d54', width=1)
    draw.text((44, 128), 'THE DAY IN TWENTY-TWO STORIES - SIX REGIONS',
              font=font(11), fill='#cdc7b6', anchor='lt')
    right(draw, 128, 'EVENTS AND REPORTS FROM 22 NOVEMBER 2026', font(11), '#cdc7b6')


def footer(draw: ImageDraw.ImageDraw) -> None:
    sources = ('Sources: Reuters - Al Jazeera - CNN - The Guardian - '
               'Middle East Eye - The World in Summary')
    draw.text((44, 990), sources, font=font(10), fill='#5b5e66', anchor='lt')
    right(draw, 990, '22 NOVEMBER 2026', font(10), '#5b5e66')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=ROOT)
    args = parser.parse_args()
    if len(STORIES) > 22:
        raise ValueError('The page holds at most 22 stories')
    image = Image.new('RGB', (1024, 1024), PAPER)
    draw = ImageDraw.Draw(image)
    masthead(draw)
    for index, story in enumerate(STORIES):
        draw_row(draw, story, index)
    footer(draw)
    args.out.mkdir(parents=True, exist_ok=True)
    image.save(args.out / 'entry.png', format='PNG')


if __name__ == '__main__':
    main()
