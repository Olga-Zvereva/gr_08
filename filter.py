from PIL import Image
import numpy as np


def avg_brightness(pixels, i, j, mosaic_size):
    return np.mean(pixels[i:i + mosaic_size, j:j + mosaic_size])


def set_grey_color(pixels, i, j, mosaic_size, brightness, graduation):
    pixels[i:i + mosaic_size, j:j + mosaic_size] = int(brightness // graduation)*graduation
    return pixels


def gray_filter(pixels, mosaic_size, graduation):
    rows = len(pixels)
    columns = len(pixels[1])
    for i in range(0, rows - mosaic_size + 1, mosaic_size):
        for j in range(0, columns - mosaic_size + 1, mosaic_size):
            pixels = set_grey_color(pixels, i, j, mosaic_size, avg_brightness(
                pixels, i, j, mosaic_size), graduation)
    return pixels


img = Image.open(input("Название изображения с расширением файла: "))
mosaic_size = int(input("Размер мозайки: "))
graduation = int(input("Градация: "))
res_name = input("Название получившейся картинки: ")
res = Image.fromarray(gray_filter(np.array(img), mosaic_size, graduation))
res.save(res_name)