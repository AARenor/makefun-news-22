"""Draw the fixed world briefing for Sunday 22 November 2026."""

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONTS = Path('/usr/share/fonts/truetype/dejavu')
COLORS = {
    'EUROPE': '#2f8f8a',
    'AFRICA': '#b4563a',
    'ASIA': '#4a58a8',
    'MIDDLE EAST': '#a8323c',
    'AMERICAS': '#2f6fa8',
    'SPORT AND CULTURE': '#b8862f',
}
STORIES = [
    ('EUROPE', 'COP31 collapses', 'Fossil-fuel deadlock ends UN talks with no deal in Antalya.'),
    ('EUROPE', 'France protests again', 'Sixth weekend of cost-of-living marches; clashes in Paris.'),
    ('EUROPE', 'EU and Indonesia sign', 'Trade deal after ten years ends 98.5 percent of tariffs.'),
    ('EUROPE', 'Finland airspace breach', 'Helsinki suspects a Russian helicopter crossed its airspace.'),
    ('AFRICA', 'Russian ship sunk', 'Sea drones sink the corvette Merkury at Benghazi port.'),
    ('AFRICA', 'Malta-flagged ship hit', 'A second drone attack strikes a merchant ship off Benghazi.'),
    ('AFRICA', 'Drones hit Sudan', "Sudan's army blames Ethiopia for strikes damaging a UN building."),
    ('AFRICA', 'Nigeria boat disaster', 'At least 24 mourners died when their boat capsized.'),
    ('AFRICA', 'Kenya internet metering', 'Proposed law would meter internet use; privacy fears grow.'),
    ('ASIA', 'Korea minister quits', 'Education minister resigns over AI-cheating exam row.'),
    ('ASIA', 'Bangladesh unrest', 'Garment wage protests spread; thousands of border guards deploy.'),
    ('ASIA', 'Rajasthan crashes', 'Two road accidents in Rajasthan kill twelve people.'),
    ('ASIA', 'Indonesia factory fire', 'Three dead and 36 missing in a Serang confectionery fire.'),
    ('ASIA', 'Golden Horse Awards', 'A Hong Kong film wins best feature in Taipei.'),
    ('MIDDLE EAST', 'Bahrain strike wounds two', 'Bahrain says Iranian strikes injured two people.'),
    ('MIDDLE EAST', 'Settlers attack villages', 'Israeli settlers set fires in Palestinian villages; Eisenkot condemns.'),
    ('MIDDLE EAST', 'Hormuz tankers ablaze', "Iran's navy says tankers breaking its rules were set alight."),
    ('AMERICAS', 'Democrats reach 258', 'Biggest House majority since 1992 after a North Carolina recount.'),
    ('AMERICAS', 'East Coast storm', 'Heavy rain floods roads along the I-95 corridor before Thanksgiving.'),
    ('AMERICAS', 'Brazil thunderstorm', 'Five killed and 250 hurt in Tupancireta, Rio Grande do Sul.'),
    ('SPORT AND CULTURE', 'Alcaraz takes ATP Finals', 'He beats Zverev 6-2, 7-6 to win his first title.'),
    ('SPORT AND CULTURE', 'Marquez seals eighth title', "Eighth MotoGP crown equals Agostini's record."),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    return ImageFont.truetype(str(FONTS / name), size)


def spaced(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str,
           face: ImageFont.FreeTypeFont, fill: str, gap: int) -> None:
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=face, fill=fill, anchor='lt')
        x += draw.textlength(char, font=face) + gap


def wrap(draw: ImageDraw.ImageDraw, text: str,
         face: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    line = ''
    for word in text.split():
        candidate = f'{line} {word}' if line else word
        if draw.textlength(candidate, font=face) > width:
            if not line or draw.textlength(word, font=face) > width:
                raise ValueError(f'Word too wide: {word}')
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    if len(lines) > 2:
        raise ValueError(f'More than two lines: {text}')
    return lines


def render(destination: Path) -> None:
    image = Image.new('RGB', (1024, 1024), '#f1ece0')
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1023, 149), fill='#16181d')
    spaced(draw, (44, 22), 'WORLD BRIEFING', font(15, True), '#cdc7b6', 3)
    date = 'SUNDAY 22 NOVEMBER 2026'
    date_size = 54
    while draw.textlength(date, font=font(date_size, True)) > 940:
        date_size -= 1
    draw.text((44, 48), date, font=font(date_size, True), fill='#fbf8ee', anchor='lt')
    draw.line((44, 120, 980, 120), fill='#4a4d54')
    draw.text((44, 128), 'THE DAY IN TWENTY-TWO STORIES - SIX REGIONS',
              font=font(11), fill='#cdc7b6', anchor='lt')
    draw.text((980, 128), 'EVENTS AND REPORTS FROM 22 NOVEMBER 2026',
              font=font(11), fill='#cdc7b6', anchor='rt')
    region_font = font(10, True)
    headline_font = font(17, True)
    fact_font = font(12)
    for index, (region, headline, fact) in enumerate(STORIES):
        x = 44 if index < 11 else 518
        top = 150 + (index % 11) * 75
        if index % 11:
            draw.line((x, top, x + 461, top), fill='#ddd6c4')
        draw.rectangle((x, top + 6, x + 3, top + 68), fill=COLORS[region])
        text_x = x + 14
        spaced(draw, (text_x, top + 6), region, region_font, COLORS[region], 2)
        headlines = wrap(draw, headline, headline_font, 434)
        facts = wrap(draw, fact, fact_font, 434)
        for line_index, line in enumerate(headlines):
            draw.text((text_x, top + 22 + line_index * 20), line,
                      font=headline_font, fill='#1b1d22', anchor='lt')
        last_headline_height = draw.textbbox(
            (0, 0), 'Ag', font=headline_font, anchor='lt'
        )[3]
        fact_y = top + 22 + (len(headlines) - 1) * 20 + last_headline_height + 2
        for line_index, line in enumerate(facts):
            draw.text((text_x, fact_y + line_index * 14), line,
                      font=fact_font, fill='#33363d', anchor='lt')
    draw.text((44, 990), 'Sources: Reuters - Al Jazeera - CNN - The Guardian - Middle East Eye - The World in Summary',
              font=font(10), fill='#5b5e66', anchor='lt')
    draw.text((980, 990), '22 NOVEMBER 2026', font=font(10), fill='#5b5e66', anchor='rt')
    destination.mkdir(parents=True, exist_ok=True)
    output = destination / 'entry.png'
    image.save(output, optimize=True)
    print(f'{output}: {output.stat().st_size} bytes, 1024x1024 pixels', file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path(__file__).resolve().parent)
    render(parser.parse_args().out)


if __name__ == '__main__':
    main()
