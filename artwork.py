from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
BOLD = FONT_DIR / 'DejaVuSans-Bold.ttf'
REGULAR = FONT_DIR / 'DejaVuSans.ttf'


@dataclass(frozen=True)
class Story:
    region: str
    headline: str
    fact: str


STORIES = (
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
)
PALETTE = {'EUROPE': '#2f8f8a', 'AFRICA': '#b4563a', 'ASIA': '#4a58a8',
           'MIDDLE EAST': '#a8323c', 'AMERICAS': '#2f6fa8', 'SPORT AND CULTURE': '#b8862f'}


def load(path, size):
    return ImageFont.truetype(str(path), size)


def fit(draw, text, path, width, start):
    for size in range(start, 5, -1):
        font = load(path, size)
        if draw.textlength(text, font=font) <= width:
            return font
    raise ValueError(f'Text does not fit: {text}')


def tracked(draw, xy, text, font, colour, spacing):
    x, y = xy
    for char in text:
        draw.text((x, y), char, font=font, fill=colour)
        x += draw.textlength(char, font=font) + spacing


def masthead(draw):
    draw.rectangle((0, 0, 1024, 149), fill='#16181d')
    tracked(draw, (44, 22), 'WORLD BRIEFING', load(BOLD, 15), '#cdc7b6', 3)
    title = 'SUNDAY 22 NOVEMBER 2026'
    draw.text((44, 48), title, font=fit(draw, title, BOLD, 940, 54), fill='#fbf8ee')
    draw.line((44, 120, 980, 120), fill='#4a4d54')
    draw.text((44, 128), 'THE DAY IN TWENTY-TWO STORIES - SIX REGIONS', font=load(REGULAR, 11), fill='#cdc7b6')
    draw.text((980, 128), 'EVENTS AND REPORTS FROM 22 NOVEMBER 2026', anchor='ra', font=load(REGULAR, 11), fill='#cdc7b6')


def footer(draw):
    sources = 'Sources: Reuters - Al Jazeera - CNN - The Guardian - Middle East Eye - The World in Summary'
    draw.text((44, 990), sources, font=load(REGULAR, 10), fill='#5b5e66')
    draw.text((980, 990), '22 NOVEMBER 2026', anchor='ra', font=load(REGULAR, 10), fill='#5b5e66')


def wrap_lines(draw, text, font, width):
    lines = []
    current = ''
    for word in text.split():
        candidate = f'{current} {word}' if current else word
        if draw.textlength(candidate, font=font) <= width:
            current = candidate
        else:
            if not current or draw.textlength(word, font=font) > width:
                raise ValueError(f'Word exceeds row width: {word}')
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > 2:
        raise ValueError(f'More than two lines: {text}')
    return lines


def measure_lines(draw, lines, font):
    boxes = [draw.textbbox((0, 0), line, font=font) for line in lines]
    ascent, descent = font.getmetrics()
    advance = ascent + descent
    height = (len(lines) - 1) * advance + max(box[3] for box in boxes)
    return advance, height


def render_row(draw, story, x, top, fonts):
    tag_font, headline_font, fact_font = fonts
    bottom = top + 75
    text_x = x + 18
    width = 462 - 18 - 10
    colour = PALETTE[story.region]
    headline = wrap_lines(draw, story.headline, headline_font, width)
    fact = wrap_lines(draw, story.fact, fact_font, width)
    headline_step, headline_height = measure_lines(draw, headline, headline_font)
    fact_step, fact_height = measure_lines(draw, fact, fact_font)
    headline_y = top + 22
    fact_y = headline_y + headline_height + 2
    if fact_y + fact_height > bottom - 3:
        raise ValueError(f'Row overflows: {story.headline}')
    draw.line((x, top, x + 461, top), fill='#ddd6c4')
    draw.rectangle((x, top + 6, x + 3, bottom - 6), fill=colour)
    tracked(draw, (text_x, top + 6), story.region, tag_font, colour, 2)
    for index, line in enumerate(headline):
        draw.text((text_x, headline_y + index * headline_step), line,
                  font=headline_font, fill='#1b1d22')
    for index, line in enumerate(fact):
        draw.text((text_x, fact_y + index * fact_step), line,
                  font=fact_font, fill='#33363d')


def draw_two_columns(image):
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 150, 1023, 980), fill='#f1ece0')
    fonts = (load(BOLD, 10), load(BOLD, 17), load(REGULAR, 12))
    if len(STORIES) != 22:
        raise ValueError('The page requires exactly twenty-two stories')
    for index, story in enumerate(STORIES):
        column, row = divmod(index, 11)
        render_row(draw, story, (44, 518)[column], 150 + row * 75, fonts)
    for x in (44, 518):
        draw.line((x, 975, x + 461, 975), fill='#ddd6c4')


def main():
    image = Image.new('RGB', (1024, 1024), '#f1ece0')
    draw = ImageDraw.Draw(image)
    masthead(draw)
    draw_two_columns(image)
    footer(draw)
    output = Path(__file__).with_name('entry.png')
    image.save(output)
    print(f'{image.width}x{image.height} RGB; {output.stat().st_size} bytes; 22 rows fitted')


if __name__ == '__main__':
    main()
