from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
width = len(arr)
height = len(arr[1])
width_pixels = 10
step = 50


def brightness_gray(arr, i, j, width_pixels):
    color = np.sum(arr[i: i + width_pixels, j: j + width_pixels]) // 3
    return int(color // width_pixels ** 2)


def transform_to_mosaic(arr, step, width_pixels):
    for i in range(0, width, width_pixels):
        for j in range(0, height, width_pixels):
            avg_brightness = brightness_gray(arr, i, j, width_pixels)
            arr[i: i + width_pixels, j: j + width_pixels] = np.full(3, int(avg_brightness // step) * step)
    return arr


arr = transform_to_mosaic(arr, step, width_pixels)
res = Image.fromarray(arr)
res.save('res.jpg')
