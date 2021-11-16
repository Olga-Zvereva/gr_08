from PIL import Image
import numpy as np
def get_average_brightness(array_of_pixels, mosaic_size, i, j):
    total_brightness = 0
    for row in range(i, i + mosaic_size):
        for column in range(j, j + mosaic_size):
            r = array_of_pixels[row][column][0]
            g = array_of_pixels[row][column][1]
            b = array_of_pixels[row][column][2]
            brightness = r // 3 + g // 3 + b // 3
            total_brightness += brightness
    return int(total_brightness // mosaic_size ** 2)


def change_pixels_color(array_of_pixels, mosaic_size, grayscale, average_brightness, i, j):
    pixel_value = int(average_brightness // grayscale) * grayscale
    for row in range(i, i + mosaic_size):
        for column in range(j, j + mosaic_size):
            array_of_pixels[row][column] = [pixel_value] * 3
    return array_of_pixels


def grey_filter(image, mosaic_size, grayscale):
    array_of_pixels = np.array(image)
    height = len(array_of_pixels)
    width = len(array_of_pixels[1])
    for i in range(0, height - mosaic_size + 1, mosaic_size):
        for j in range(0, width - mosaic_size + 1, mosaic_size):
            average_brightness = get_average_brightness(array_of_pixels, mosaic_size, i, j)
            array_of_pixels = change_pixels_color(array_of_pixels, mosaic_size, grayscale, average_brightness, i, j)
    return array_of_pixels


input_image = Image.open("img2.jpg")
image_in_gray_tones = Image.fromarray(grey_filter(input_image, 10, 50))
image_in_gray_tones.save('res.jpg') 
