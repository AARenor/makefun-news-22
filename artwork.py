"""Create the World Briefing newspaper artwork with Pillow."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
SIZE = 1024
PAPER = "#eeeae1"
INK = "#20333b"
MUTED = "#53666a"
LINE = "#d6d2c8"
COLORS = {
    "EUROPE": "#167f7a",
    "AFRICA": "#ae573d",
    "ASIA": "#514f9c",
    "MIDDLE EAST": "#a53248",
    "AMERICAS": "#326ca1",
    "SPORT AND CULTURE": "#a77b19",
}

STORIES = [
    ("EUROPE", "COP31 collapses", "Fossil-fuel deadlock ends UN talks with no deal in Antalya."),
    ("EUROPE", "France protests again", "Sixth weekend of cost-of-living marches; clashes in Paris."),
    ("EUROPE", "EU and Indonesia sign", "Trade deal after ten years ends 98.5 percent of tariffs."),
    ("EUROPE", "Finland airspace breach", "Helsinki suspects a Russian helicopter crossed its airspace."),
    ("AFRICA", "Russian ship sunk", "Sea drones sink the corvette Merkury at Benghazi port."),
    ("AFRICA", "Malta-flagged ship hit", "A second drone attack strikes a merchant ship off Benghazi."),
    ("AFRICA", "Drones hit Sudan", "Sudan's army blames Ethiopia for strikes damaging a UN building."),
    ("AFRICA", "Nigeria boat disaster", "At least 24 mourners died when their boat capsized."),
    ("AFRICA", "Kenya internet metering", "Proposed law would meter internet use; privacy fears grow."),
    ("ASIA", "Korea minister quits", "Education minister resigns over AI-cheating exam row."),
    ("ASIA", "Bangladesh unrest", "Garment wage protests spread; thousands of border guards deploy."),
    ("ASIA", "Rajasthan crashes", "Two road accidents in Rajasthan kill twelve people."),
    ("ASIA", "Indonesia factory fire", "Three dead and 36 missing in a Serang confectionery fire."),
    ("ASIA", "Golden Horse Awards", "A Hong Kong film wins best feature in Taipei."),
    ("ASIA", "Bahrain strike wounds two", "Bahrain says Iranian strikes injured two people."),
    ("MIDDLE EAST", "Settlers attack villages", "Israeli settlers burn Palestinian villages; Eisenkot condemns."),
    ("MIDDLE EAST", "Hormuz tankers ablaze", "Iran's navy says tankers breaking its rules were set alight."),
    ("AMERICAS", "Democrats reach 258", "Biggest House majority since 1992 after a North Carolina recount."),
    ("AMERICAS", "East Coast storm", "Heavy rain floods roads along the I-95 corridor before Thanksgiving."),
    ("AMERICAS", "Brazil thunderstorm", "Five killed and 250 hurt in Tupancireta, Rio Grande do Sul."),
    ("SPORT AND CULTURE", "Alcaraz takes ATP Finals", "He beats Zverev 6-2, 7-6 to win his first title."),
    ("SPORT AND CULTURE", "Marquez seals eighth title", "Eighth MotoGP crown equals Agostini's record."),
]


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    width: int,
    max_lines: int,
) -> list[str]:
    """Wrap on words and reject any content that exceeds its allotted space."""
    lines = []
    line = ""
    for word in text.split():
        candidate = f"{line} {word}" if line else word
        if draw.textlength(candidate, font=font) <= width:
            line = candidate
        else:
            if not line or draw.textlength(word, font=font) > width:
                raise ValueError(f"Word exceeds text width: {word}")
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    if len(lines) > max_lines:
        raise ValueError(f"Text exceeds {max_lines} lines: {text}")
    return lines


def checked_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    bounds: tuple[int, int, int, int],
) -> None:
    """Draw only if the visible text fits inside its designated rectangle."""
    left, top, right, bottom = draw.textbbox(xy, text, font=font, anchor="lt")
    if left < bounds[0] or top < bounds[1] or right > bounds[2] or bottom > bounds[3]:
        raise ValueError(f"Text exceeds its bounds: {text}")
    draw.text(xy, text, font=font, fill=fill, anchor="lt")


def main() -> None:
    image = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(image)
    regular = FONT_DIR / "DejaVuSans.ttf"
    bold = FONT_DIR / "DejaVuSans-Bold.ttf"
    region_font = ImageFont.truetype(str(bold), 10)
    headline_font = ImageFont.truetype(str(bold), 17)
    fact_font = ImageFont.truetype(str(regular), 12)
    small_font = ImageFont.truetype(str(bold), 10)
    date_font = ImageFont.truetype(str(bold), 38)
    footer_font = ImageFont.truetype(str(regular), 10)

    draw.rectangle((0, 0, SIZE - 1, 149), fill=INK)
    checked_text(draw, (32, 18), "WORLD BRIEFING", region_font, "#bfc9c4", (32, 0, 992, 149))
    checked_text(draw, (30, 43), "SUNDAY 22 NOVEMBER 2026", date_font, PAPER, (30, 0, 994, 111))
    draw.line((32, 111, 992, 111), fill="#718086", width=1)
    checked_text(
        draw, (32, 124), "THE DAY IN TWENTY-TWO STORIES · SIX REGIONS",
        small_font, PAPER, (32, 112, 510, 149),
    )
    report_label = "EVENTS AND REPORTS FROM 22 NOVEMBER 2026"
    report_x = 992 - int(draw.textlength(report_label, font=small_font))
    checked_text(
        draw, (report_x, 124), report_label,
        small_font, PAPER, (588, 112, 993, 149),
    )

    if len(STORIES) != 22:
        raise ValueError("The briefing must contain exactly 22 stories")
    row_top = 156
    row_height = 75
    column_width = 468
    for index, (region, headline, fact) in enumerate(STORIES):
        column, row = divmod(index, 11)
        x = 32 + column * 492
        y = row_top + row * row_height
        text_x = x + 14
        text_right = x + column_width
        text_width = text_right - text_x
        bounds = (text_x - 1, y, text_right, y + row_height - 2)
        color = COLORS[region]
        draw.rectangle((x, y + 2, x + 3, y + row_height - 5), fill=color)
        checked_text(draw, (text_x, y + 2), region, region_font, color, bounds)
        headline_lines = wrap_text(draw, headline, headline_font, text_width, 2)
        fact_lines = wrap_text(draw, fact, fact_font, text_width, 2)
        for line_number, line in enumerate(headline_lines):
            checked_text(
                draw, (text_x, y + 15 + line_number * 18), line,
                headline_font, INK, bounds,
            )
        fact_y = y + 15 + len(headline_lines) * 18 + 2
        for line_number, line in enumerate(fact_lines):
            checked_text(draw, (text_x, fact_y + line_number * 13), line, fact_font, MUTED, bounds)
        draw.line((x, y + row_height - 1, x + column_width, y + row_height - 1), fill=LINE, width=1)

    footer_y = 992
    sources = "Sources: Reuters · Al Jazeera · CNN · The Guardian · Middle East Eye · Cape Times · AllAfrica · Weather.com"
    checked_text(draw, (32, footer_y), sources, footer_font, INK, (32, 985, 820, 1020))
    checked_text(draw, (858, footer_y), "22 NOVEMBER 2026", small_font, MUTED, (858, 985, 992, 1020))
    image.save(ROOT / "entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
