from PIL import Image
import numpy as np


def get_medium_pixel_brightness(r, g, b, number_cells):
    return r / number_cells + g / number_cells + b / number_cells


def get_medium_cell_brightness(pixels, start_vertical, start_horizontal, size):
    medium = 0
    for i in range(start_vertical, start_vertical + size):
        for j in range(start_horizontal, start_horizontal + size):
            R, G, B = pixels[i][j]
            medium += get_medium_pixel_brightness(R, G, B, size ** 2)
    return int(medium)


def get_new_color(medium_value, gradation):
    return int(medium_value // gradation) * gradation / 3


def convert_cell_to_pixel_art(pixels, start_vertical, start_horizontal,
                              size, grad_step, m_brightness):
    for i in range(start_vertical, start_vertical + size):
        for j in range(start_horizontal, start_horizontal + size):
            pixels[i][j] = [get_new_color(m_brightness, grad_step)] * 3
    return pixels


name_image = "img2.jpg"
name_result = "res.jpg"

img = Image.open(name_image)
image_pixels = np.array(img)
width = len(image_pixels)
height = len(image_pixels)

cell_size = 10
gradation_step = 50

index_of_vertical = 0
while index_of_vertical < width:
    index_of_horizontal = 0
    while index_of_horizontal < height:
        medium_brightness = get_medium_cell_brightness(image_pixels,
                                                       index_of_vertical,
                                                       index_of_horizontal,
                                                       cell_size)
        image_pixels = convert_cell_to_pixel_art(image_pixels,
                                                 index_of_vertical,
                                                 index_of_horizontal,
                                                 cell_size,
                                                 gradation_step,
                                                 medium_brightness)
        index_of_horizontal += cell_size
    index_of_vertical += cell_size

res = Image.fromarray(image_pixels)
res.save(name_result)

