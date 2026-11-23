from PIL import ImageDraw, ImageFont

from artwork import PALETTE, STORIES

BOLD_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REGULAR_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def wrap_words(draw, text, font, width):
    lines = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}" if current else word
        if draw.textlength(candidate, font=font) <= width:
            current = candidate
        else:
            if not current:
                raise ValueError(f"Word does not fit: {word}")
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > 2:
        raise ValueError(f"Text needs more than two lines: {text}")
    return lines


def draw_rows(image):
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 150, 1023, 980), fill="#f1ece0")
    region_font = ImageFont.truetype(BOLD_PATH, 10)
    headline_font = ImageFont.truetype(BOLD_PATH, 17)
    fact_font = ImageFont.truetype(REGULAR_PATH, 12)
    if len(STORIES) != 22:
        raise ValueError("The layout requires exactly twenty-two stories")
    for index, story in enumerate(STORIES):
        column, row = divmod(index, 11)
        left = (44, 518)[column]
        top = 150 + row * 75
        right = left + 462
        bottom = top + 75
        colour = PALETTE[story.region]
        if row:
            draw.line((left, top, right - 1, top), fill="#ddd6c4")
        draw.rectangle((left, top + 6, left + 3, bottom - 6), fill=colour)
        text_left = left + 18
        cursor = text_left
        for letter in story.region:
            draw.text((cursor, top + 6), letter, font=region_font, fill=colour, anchor="lt")
            cursor += draw.textlength(letter, font=region_font) + 2
        width = right - text_left - 10
        headlines = wrap_words(draw, story.headline, headline_font, width)
        facts = wrap_words(draw, story.fact, fact_font, width)
        y = top + 22
        for line in headlines:
            draw.text((text_left, y), line, font=headline_font, fill="#1b1d22", anchor="lt")
            y += 20
        last_headline = headlines[-1]
        headline_bottom = draw.textbbox(
            (text_left, y - 20), last_headline, font=headline_font, anchor="lt"
        )[3]
        y = headline_bottom + 2
        for line in facts:
            draw.text((text_left, y), line, font=fact_font, fill="#33363d", anchor="lt")
            y += 16
