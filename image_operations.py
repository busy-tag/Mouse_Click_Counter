from PIL import Image, ImageDraw, ImageFont

def create_text_to_image(text_parts, width=240, height=280, background_color=(0, 0, 0), font_paths=None, font_sizes=None, text_colors=None, output_file="click_count.png", drive_letter="D"):
    output_file = f"{drive_letter}:\\{output_file}"
    image = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(image)
    
    y = 50

    if not font_paths:
        font_paths = ["MontserratBlack-3zOvZ.ttf"] * len(text_parts)
    if not font_sizes:
        font_sizes = [125] * len(text_parts)
    if not text_colors:
        text_colors = [(255, 255, 255)] * len(text_parts)

    for i, text in enumerate(text_parts):
        font = ImageFont.truetype(font_paths[i], font_sizes[i])
        text_bbox = draw.textbbox((0, y), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (width - text_width) // 2
        draw.text((text_x, y), text, font=font, fill=text_colors[i])
        y += text_height + 20

    image.save(output_file)

def generate_image(click_count, drive_letter):
    if click_count < 1000:
        font_size = 125
    elif click_count < 100000:
        font_size = 75
    elif click_count < 1000000:
        font_size = 50
    else:
        font_size = 25

    text_parts = [
        "Click Count",
        str(click_count)
    ]
    font_paths = ["MontserratBlack-3zOvZ.ttf", "MontserratBlack-3zOvZ.ttf"]
    font_sizes = [30, font_size] 
    text_colors = [(255, 255, 255), (0, 200, 0)] 

    create_text_to_image(
        text_parts=text_parts,
        font_paths=font_paths,
        font_sizes=font_sizes,
        text_colors=text_colors,
        drive_letter=drive_letter
    )