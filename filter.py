from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
pixels_array = np.array(img)
width = len(pixels_array)
height = len(pixels_array[1])
width_mosaic = 10
grad = 50


def get_brightness_gray(pixels_array, i, j, width_mosaic):
    final_brightness = 0
    for row in range(i, i + width_mosaic):
        for column in range(j, j + width_mosaic):
            red = pixels_array[row][column][0]
            green = pixels_array[row][column][1]
            blue = pixels_array[row][column][2]
            color = int(red) + int(green) + int(blue)
            final_brightness += color // 3
    return int(final_brightness // width_mosaic ** 2)


def get_mosaic(pixels_array, grad, width_mosaic):
    i = 0
    while i < width:
        j = 0
        while j < height:
            average_brightness = get_brightness_gray(pixels_array, i, j, width_mosaic)
            for row in range(i, i + width_mosaic):
                for column in range(j, j + width_mosaic):
                    pixels_array[row][column][0] = int(average_brightness // grad) * grad
                    pixels_array[row][column][1] = int(average_brightness // grad) * grad
                    pixels_array[row][column][2] = int(average_brightness // grad) * grad
            j = j + width_mosaic
        i = i + width_mosaic
    return pixels_array


pixels_array = get_mosaic(pixels_array, grad, width_mosaic)
result_image = Image.fromarray(pixels_array)
result_image.save('res.jpg')
