from PIL import Image
import numpy as np


def avg_brightness(pixels, i, j, mosaic_size):
    brightness = 0
    for row in range(i, i + mosaic_size):
        for column in range(j, j + mosaic_size):
            r = pixels[row][column][0]
            g = pixels[row][column][1]
            b = pixels[row][column][2]
            M = r // 3 + g // 3 + b // 3
            brightness += M
    return int(brightness // mosaic_size**2)


def set_grey_color(pixels, i, j, mosaic_size, brightness, graduation):
    for row in range(i, i + mosaic_size):
        for column in range(j, j + mosaic_size):
            value = int(brightness // graduation)*graduation
            pixels[row][column][0] = value
            pixels[row][column][1] = value
            pixels[row][column][2] = value
    return pixels


def gray_filter(pixels, mosaic_size, graduation):
    rows = len(pixels)
    columns = len(pixels[1])
    for i in range(0, rows - mosaic_size + 1, mosaic_size):
        for j in range(0, columns - mosaic_size + 1, mosaic_size):
            pixels = set_grey_color(pixels, i, j, mosaic_size, avg_brightness(
                pixels, i, j, mosaic_size), graduation)
    return pixels


img = Image.open("img2.jpg")
mosaic_size = 10
graduation = 50
res = Image.fromarray(gray_filter(np.array(img), mosaic_size, graduation))
res.save('res.jpg')
