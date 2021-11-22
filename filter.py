import numpy as np
from PIL import Image


def crop_img(pixels, distance):
    height_overflow = len(pixels) % distance
    width_overflow = len(pixels[1]) % distance
    return pixels[:len(pixels) - height_overflow, :len(pixels[0]) - width_overflow]


def get_average_brightness(pixels, x, y, distance):
    brightness = 0
    for x_n in range(x, x + distance):
        for y_n in range(y, y + distance):
            [r, g, b] = pixels[y_n][x_n]
            pixel = np.array([r, g, b]).astype(np.int32)
            brightness += int(np.sum(pixel))
    return brightness // distance**2


def change_to_color(pixels, x, y, color, distance):
    for y_n in range(y, y + distance):
        for x_n in range(x, x + distance):
            pixels[y_n][x_n] = color


img = Image.open("img2.jpg")
pixels = np.array(img)
distance = int(input("Размер мозайки: "))
gradation = int(input("Градаций серого: "))
gradation_step = 256 // gradation

pixels = crop_img(pixels, distance)
height = len(pixels)
width = len(pixels[1])

for x in range(0, width, distance):
    for y in range(0, height, distance):
        avg_brightness = get_average_brightness(pixels, x, y, distance) / 3
        color = np.full(
            3,
            int(avg_brightness//gradation_step) * gradation_step,
            dtype=np.uint8
        )
        change_to_color(pixels, x, y, color, distance)

res = Image.fromarray(pixels)
res.save('res.jpg')