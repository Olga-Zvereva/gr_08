from PIL import Image
import numpy as np


def brightness_gray(arr, i, j, width_pixels):
    color = np.sum(arr[i: i + width_pixels, j: j + width_pixels]) // 3
    return int(color // width_pixels ** 2)


def transform_to_mosaic(arr, step, width_pixels):
    for i in range(0, len(arr), width_pixels):
        for j in range(0, len(arr[1]), width_pixels):
            avg_brightness = brightness_gray(arr, i, j, width_pixels)
            arr[i: i + width_pixels, j: j + width_pixels] = np.full(3, int(avg_brightness // step) * step)
    return arr


file_name = input("Введите имя файла, который надо преобразовать ")
res_name = input("Введите имя файла, куда надо сохранить измененную картинку ")
width_pixels = int(input("Введите размер мозаики "))
step = int(input("Введите количество градаций "))

img = Image.open(file_name)
arr = np.array(img)

arr = transform_to_mosaic(arr, step, width_pixels)

res = Image.fromarray(arr)
res.save(res_name)
