"""Draw the original newspaper illustration used by this entry.

This is an offline design tool. The competition entrypoint copies the finished
PNG and needs only Python's standard library.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SIZE = 1024
PAPER = "#eeeae1"
CARD = "#fbf9f2"
INK = "#20333b"
MUTED = "#53666a"
RED = "#ad5946"
BLUE = "#547383"
GOLD = "#bd9955"
GREEN = "#72897b"
LINE = "#d6d2c8"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

STORIES = [
    {
        "tag": "CLIMATE  /  EURONEWS",
        "title": ("COP31 pact", "rejected"),
        "fact": "Fossil fuel omission splits delegates.",
        "icon": "climate",
        "color": GREEN,
    },
    {
        "tag": "UKRAINE  /  AL JAZEERA",
        "title": ("Ukraine seeks", "US missiles"),
        "fact": "Zelenskyy urges Patriot deliveries.",
        "icon": "ukraine",
        "color": BLUE,
    },
    {
        "tag": "SUDAN  /  THE RIO TIMES",
        "title": ("Drones hit", "Sudan capital"),
        "fact": "At least four dead; UN building hit.",
        "icon": "sudan",
        "color": RED,
    },
    {
        "tag": "LIBYA  /  AL ARABIYA",
        "title": ("Russian ship", "blast in Libya"),
        "fact": "Authorities suspect a drone attack.",
        "icon": "libya",
        "color": BLUE,
    },
    {
        "tag": "SOUTH KOREA  /  THE HINDU",
        "title": ("Korea education", "minister quits"),
        "fact": "AI cheating fears roiled exam plans.",
        "icon": "korea",
        "color": RED,
    },
    {
        "tag": "CHESS  /  CHESS.COM",
        "title": ("World chess", "ceremony"),
        "fact": "Sindarov draws white versus Gukesh.",
        "icon": "chess",
        "color": GOLD,
    },
]


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def fitting_font(draw: ImageDraw.ImageDraw, text: str, path: str, maximum: int, width: int) -> ImageFont.FreeTypeFont:
    for size in range(maximum, 16, -1):
        candidate = font(path, size)
        if draw.textlength(text, font=candidate) <= width:
            return candidate
    raise ValueError(f"Text does not fit: {text}")


def icon(draw: ImageDraw.ImageDraw, kind: str, x: int, y: int, color: str) -> None:
    """Draw a small original symbol for a story, without external images."""
    pale = "#f0eee6"
    draw.rounded_rectangle((x, y, x + 98, y + 98), radius=16, fill=pale)
    if kind == "climate":
        draw.ellipse((x + 13, y + 13, x + 82, y + 82), outline=color, width=4)
        draw.ellipse((x + 33, y + 13, x + 62, y + 82), outline=color, width=3)
        draw.line((x + 15, y + 47, x + 80, y + 47), fill=color, width=3)
        draw.arc((x + 17, y + 18, x + 79, y + 62), 15, 165, fill=color, width=2)
        draw.arc((x + 17, y + 32, x + 79, y + 76), 195, 345, fill=color, width=2)
        draw.line((x + 62, y + 60, x + 88, y + 86), fill=RED, width=6)
        draw.line((x + 88, y + 60, x + 62, y + 86), fill=RED, width=6)
    elif kind == "ukraine":
        draw.polygon([(x + 48, y + 12), (x + 78, y + 23), (x + 76, y + 56), (x + 68, y + 73), (x + 48, y + 86), (x + 28, y + 73), (x + 20, y + 56), (x + 18, y + 23)], outline=color, width=4)
        draw.line((x + 49, y + 62, x + 49, y + 30), fill=color, width=5)
        draw.polygon([(x + 49, y + 19), (x + 40, y + 35), (x + 58, y + 35)], fill=color)
        draw.line((x + 36, y + 68, x + 62, y + 68), fill=color, width=3)
    elif kind == "sudan":
        draw.rectangle((x + 13, y + 62, x + 85, y + 81), outline=color, width=4)
        draw.rectangle((x + 24, y + 51, x + 44, y + 81), outline=color, width=4)
        draw.line((x + 54, y + 60, x + 54, y + 81), fill=color, width=3)
        draw.line((x + 69, y + 60, x + 69, y + 81), fill=color, width=3)
        draw.line((x + 23, y + 29, x + 75, y + 29), fill=color, width=4)
        draw.line((x + 35, y + 18, x + 42, y + 36), fill=color, width=4)
        draw.line((x + 63, y + 18, x + 56, y + 36), fill=color, width=4)
        draw.ellipse((x + 43, y + 25, x + 55, y + 35), fill=color)
        draw.line((x + 49, y + 38, x + 49, y + 47), fill=color, width=3)
    elif kind == "libya":
        draw.polygon([(x + 12, y + 62), (x + 86, y + 62), (x + 73, y + 77), (x + 27, y + 77)], fill=color)
        draw.rectangle((x + 33, y + 49, x + 62, y + 61), fill=color)
        draw.rectangle((x + 43, y + 39, x + 54, y + 49), fill=color)
        draw.line((x + 13, y + 84, x + 85, y + 84), fill=color, width=3)
        draw.line((x + 70, y + 16, x + 70, y + 39), fill=RED, width=4)
        draw.line((x + 58, y + 27, x + 82, y + 27), fill=RED, width=4)
        draw.line((x + 61, y + 19, x + 79, y + 36), fill=RED, width=3)
        draw.line((x + 79, y + 19, x + 61, y + 36), fill=RED, width=3)
    elif kind == "korea":
        draw.rounded_rectangle((x + 20, y + 12, x + 76, y + 85), radius=5, outline=color, width=4)
        draw.line((x + 30, y + 61, x + 66, y + 61), fill=color, width=3)
        draw.line((x + 30, y + 70, x + 58, y + 70), fill=color, width=3)
        draw.text((x + 30, y + 22), "AI", fill=color, font=font(BOLD, 28))
        draw.line((x + 63, y + 13, x + 86, y + 36), fill=RED, width=5)
        draw.line((x + 86, y + 13, x + 63, y + 36), fill=RED, width=5)
    elif kind == "chess":
        for row in range(4):
            for col in range(4):
                if (row + col) % 2 == 0:
                    draw.rectangle((x + 11 + col * 19, y + 11 + row * 19, x + 29 + col * 19, y + 29 + row * 19), fill=color)
        draw.ellipse((x + 48, y + 31, x + 70, y + 53), fill=INK, outline=CARD, width=2)
        draw.polygon([(x + 52, y + 51), (x + 66, y + 51), (x + 75, y + 72), (x + 44, y + 72)], fill=INK, outline=CARD)
        draw.rounded_rectangle((x + 39, y + 70, x + 79, y + 80), radius=2, fill=INK, outline=CARD, width=2)
    else:
        raise ValueError(f"Unknown icon: {kind}")


def main() -> None:
    image = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, SIZE, 149), fill=INK)
    draw.rectangle((0, 149, SIZE, 154), fill=RED)

    draw.ellipse((36, 31, 113, 108), outline="#eeeae1", width=3)
    draw.ellipse((58, 31, 91, 108), outline="#eeeae1", width=2)
    draw.line((38, 69, 111, 69), fill="#eeeae1", width=2)
    draw.text((132, 31), "WORLD", font=font(SERIF, 36), fill=CARD)
    draw.text((132, 75), "BRIEFING", font=font(BOLD, 24), fill="#bfc9c4")
    draw.line((370, 29, 370, 116), fill="#718086", width=2)
    draw.text((397, 28), "SUNDAY", font=font(BOLD, 20), fill="#e9b6a6")
    draw.text((393, 60), "22 NOVEMBER 2026", font=font(BOLD, 44), fill=CARD)

    draw.text((36, 170), "THE WORLD IN SIX STORIES", font=font(BOLD, 19), fill=INK)
    draw.text((741, 170), "A GLOBAL SNAPSHOT", font=font(BOLD, 17), fill=MUTED)
    card_width = 464
    card_height = 237
    for index, story in enumerate(STORIES):
        x = 35 + (index % 2) * 490
        y = 206 + (index // 2) * 246
        draw.rounded_rectangle((x, y, x + card_width, y + card_height), radius=6, fill=CARD, outline=LINE, width=2)
        draw.rectangle((x, y, x + 7, y + card_height), fill=story["color"])
        draw.text((x + 22, y + 17), story["tag"], font=font(BOLD, 18), fill=story["color"])
        draw.line((x + 22, y + 43, x + card_width - 22, y + 43), fill=LINE, width=1)
        for line_number, text in enumerate(story["title"]):
            headline_font = fitting_font(draw, text, SERIF, 33, 305)
            draw.text((x + 21, y + 56 + 41 * line_number), text, font=headline_font, fill=INK)
        icon(draw, story["icon"], x + 340, y + 58, story["color"])
        draw.line((x + 22, y + 172, x + card_width - 22, y + 172), fill=LINE, width=1)
        fact_font = fitting_font(draw, story["fact"], SANS, 21, card_width - 44)
        draw.text((x + 22, y + 183), story["fact"], font=fact_font, fill=INK)

    draw.text((36, 961), "EVENTS AND REPORTS FROM 22 NOVEMBER 2026", font=font(BOLD, 19), fill=MUTED)
    draw.line((36, 996, 988, 996), fill=INK, width=3)
    image.save(ROOT / "entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
