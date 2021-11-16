from PIL import Image
import numpy as np


def func_average_brightness(pixels_array, mosaic, i, j):
    area = pixels_array[i:i + mosaic, j:j + mosaic]
    final_brightness = np.sum(area)
    return int(final_brightness // 3 // mosaic ** 2)


def new_pixels_color(pixels_array, mosaic, grayscale, average_brightness, i, j):
    pixel_value = int(average_brightness // grayscale) * grayscale
    pixels_array[i:i + mosaic, j:j + mosaic] = pixel_value
    return pixels_array


def grey_filter(input_image, mosaic, grayscale):
    pixels_array = np.array(input_image)
    height = len(pixels_array)
    width = len(pixels_array[1])
    for i in range(0, height - mosaic + 1, mosaic):
        for j in range(0, width - mosaic + 1, mosaic):
            average_brightness = func_average_brightness(pixels_array, mosaic, i, j)
            pixels_array = new_pixels_color(pixels_array, mosaic, grayscale, average_brightness, i, j)
    return pixels_array


def main():
    name_input_image = '{}.{}'.format(input('Имя входного изображения - '), input('Формат входного изображения - '))
    mosaic = int(input('Размер мозаики - '))
    grayscale = int(input('Величина градации серого - '))
    name_output_image = '{}.{}'.format(input('Имя выходного изображения - '), input('Формат выходного изображения - '))
    input_image = Image.open(name_input_image)
    gray_image = Image.fromarray(grey_filter(input_image, mosaic, grayscale))
    gray_image.save(name_output_image)
