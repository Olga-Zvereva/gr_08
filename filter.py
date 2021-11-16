from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
pixels_array = np.array(img)
width = len(pixels_array)
height = len(pixels_array[1])
width_mosaic = 10
grad = 50


def get_brightness_gray(pixels_array, i, j, width_mosaic):
    color = np.sum(pixels_array[i: i + width_mosaic, j: j + width_mosaic])
    return int(color // 3 // width_mosaic ** 2)


def get_mosaic(pixels_array, grad, width_mosaic):
    for i in range(0, width - width_mosaic + 1, width_mosaic):
        for j in range(0, height - width_mosaic + 1, width_mosaic):
            average_brightness = get_brightness_gray(pixels_array, i, j, width_mosaic)
            pixels_array[i: i + width_mosaic, j: j + width_mosaic] = np.full(3, int(average_brightness // grad) * grad)
    return pixels_array


pixels_array = get_mosaic(pixels_array, grad, width_mosaic)
result_image = Image.fromarray(pixels_array)
result_image.save('res.jpg')
