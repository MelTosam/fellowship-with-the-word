from PIL import Image, ImageDraw
import os

os.makedirs('static/icons', exist_ok=True)

for size in [192, 512]:
    img = Image.new('RGB', (size, size), '#2D2640')
    draw = ImageDraw.Draw(img)
    margin = size // 4
    draw.ellipse([margin, margin, size-margin, size-margin], fill='#9B8EC4')
    center = size // 2
    r = size // 8
    draw.ellipse([center-r, center-r, center+r, center+r], fill='white')
    img.save(f'static/icons/icon-{size}.png')
    print(f'Created icon-{size}.png')
