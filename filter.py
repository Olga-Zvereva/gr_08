rom PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)
width = len(arr)
height = len(arr[1])
width_pixels = 10
step = 50


def brightness_gray(arr, i, j, width_pixels):
    s = 0
    for x in range(i, i + width_pixels):
        for y in range(j, j + width_pixels):
            r = arr[x][y][0]
            g = arr[x][y][1]
            b = arr[x][y][2]
            color = (int(r) + int(g) + int(b)) // 3
            s += color
    s = int(s // width_pixels ** 2)
    return s


def transform_to_mosaic(arr, step, width_pixels):
    i = 0
    while i < width:
        j = 0
        while j < height:
            avg_brightness = brightness_gray(arr, i, j, width_pixels)
            for x in range(i, i + width_pixels):
                for y in range(j, j + width_pixels):
                    arr[x][y][0] = int(avg_brightness // step) * step
                    arr[x][y][1] = int(avg_brightness // step) * step
                    arr[x][y][2] = int(avg_brightness // step) * step
            j = j + width_pixels
        i = i + width_pixels
    return arr


arr = transform_to_mosaic(arr, step, width_pixels)

res = Image.fromarray(arr)
res.save('res.jpg')

