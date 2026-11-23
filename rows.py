from PIL import ImageDraw

from artwork import BOLD, PALETTE, REGULAR, STORIES, Story, load, tracked, wrap


def draw_rows(image):
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 150, 1023, 980), fill="#f1ece0")
    region_font = load(BOLD, 10)
    headline_font = load(BOLD, 17)
    fact_font = load(REGULAR, 12)
    if len(STORIES) != 22:
        raise ValueError("The briefing requires twenty-two stories")
    for index, story in enumerate(STORIES):
        if not isinstance(story, Story):
            raise TypeError("Every row must contain a Story")
        column, row = divmod(index, 11)
        x = (44, 518)[column]
        y = 150 + row * 75
        colour = PALETTE[story.region]
        draw.rectangle((x, y + 5, x + 3, y + 69), fill=colour)
        if row:
            draw.line((x, y, x + 461, y), fill="#ddd6c4")
        text_x = x + 13
        text_width = 438
        tracked(draw, (text_x, y + 3), story.region, region_font, colour, 2)
        headlines = wrap(draw, story.headline, headline_font, text_width)
        facts = wrap(draw, story.fact, fact_font, text_width)
        headline_y = y + 17
        for line in headlines:
            draw.text((text_x, headline_y), line, font=headline_font, fill="#1b1d22")
            headline_y += 19
        fact_y = headline_y + 3
        for line in facts:
            box = draw.textbbox((text_x, fact_y), line, font=fact_font)
            if box[3] > y + 73:
                raise ValueError(f"Row overflows vertically: {story.headline}")
            draw.text((text_x, fact_y), line, font=fact_font, fill="#33363d")
            fact_y += 14
    print("22 rows fitted; 11 per column; at most two lines per headline and fact")
