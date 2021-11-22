import numpy as np
from PIL import Image


def crop_img(pixels, distance):
    height_overflow = len(pixels) % distance
    width_overflow = len(pixels[1]) % distance
    return pixels[:len(pixels) - height_overflow,
                  :len(pixels[0]) - width_overflow]


img = Image.open("img2.jpg")
pixels = np.array(img)
mozaik_size = int(input("Размер мозайки: "))
gradation = int(input("Градаций серого: "))
gradation_step = 256 / gradation

pixels = crop_img(pixels, mozaik_size)
height = len(pixels)
width = len(pixels[1])

for x in range(0, width, mozaik_size):
    for y in range(0, height, mozaik_size):
        mozaik = pixels[x:x + mozaik_size + 1, y:y + mozaik_size + 1]
        average = np.average(mozaik)
        average = int(average//gradation_step) * gradation_step
        mozaik.fill(average)

res = Image.fromarray(pixels)
res.save('res.jpg')