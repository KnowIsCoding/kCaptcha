# captcha_generator.py
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random
import string

def random_text(length=6, use_russian=False):
    if use_russian:
        letters = string.digits + "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else:
        letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def random_background(width, height):
    noise = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    background = Image.fromarray(noise)
    draw = ImageDraw.Draw(background)

    for _ in range(10):
        shape_type = random.choice(['rectangle', 'circle'])
        color = tuple(random.randint(0, 255) for _ in range(3))
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = x1 + random.randint(20, 100)
        y2 = y1 + random.randint(20, 100)

        if shape_type == 'rectangle':
            draw.rectangle([x1, y1, x2, y2], fill=color)
        elif shape_type == 'circle':
            draw.ellipse([x1, y1, x2, y2], fill=color)

    return background

def distort_text(image):
    width, height = image.size
    distorted_image = Image.new('RGBA', (width, height))
    
    for x in range(width):
        offset = int(5 * np.sin(x / 10.0))
        for y in range(height):
            if 0 <= y + offset < height:
                distorted_image.putpixel((x, y), image.getpixel((x, y + offset)))
    
    return distorted_image

def draw_3d_text(draw, text, position, font):
    x_offset = position[0]
    letter_positions = []

    for char in text:
        angle = random.randint(-30, 30)
        text_color = tuple(random.randint(0, 255) for _ in range(3))

        temp_image = Image.new('RGBA', (50, 100), (255, 255, 255, 0))
        temp_draw = ImageDraw.Draw(temp_image)

        temp_draw.text((5, 5), char, font=font, fill=text_color)
        rotated_image = temp_image.rotate(angle, expand=1)
        
        distorted_image = distort_text(rotated_image)

        shadow_offset = 2
        shadow_color = (50, 50, 50)

        draw.bitmap((x_offset + shadow_offset, position[1] + shadow_offset), distorted_image.convert("RGBA"), fill=shadow_color)
        draw.bitmap((x_offset, position[1]), distorted_image.convert("RGBA"))

        end_x = x_offset + distorted_image.size[0]
        center_y = position[1] + distorted_image.size[1] // 2

        letter_positions.append((end_x, center_y))

        x_offset += distorted_image.size[0] - 10

    for i in range(len(letter_positions) - 1):
        draw.line([letter_positions[i], letter_positions[i + 1]], fill=(255, 255, 255), width=2)

def add_background_text(draw, width, height):
    for _ in range(5):
        background_text = random_text(length=random.randint(4, 10), use_russian=random.choice([True, False]))
        
        font_size = random.randint(20, 40)
        
        try:
            font_path = "arial.ttf"
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            font = ImageFont.load_default()
        
        text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(50, 150))
        
        x_position = random.randint(0, width - 100)
        y_position = random.randint(0, height - 50)
        
        draw.text((x_position, y_position), background_text, font=font, fill=text_color)

def generate_captcha(use_russian=False):
    width, height = 400, 200
    background = random_background(width, height)
    
    draw = ImageDraw.Draw(background)

    fonts = ["arial.ttf", "times.ttf", "courier.ttf"]
    font_path = random.choice(fonts)
    
    font_size = random.randint(40, 60)
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    captcha_text = random_text(length=6, use_russian=use_russian)

    add_background_text(draw, width, height)

    draw_3d_text(draw, captcha_text.upper(), (50,height //4), font)

    return background,captcha_text