from PIL import Image
import numpy as np

def cut_off_img(pixels, size):
    over_height = len(pixels) % size
    over_width = len(pixels[1]) % size
    return pixels[:len(pixels) - over_height, :len(pixels[1]) - over_width]

def get_colors(cutted_img, x, y):
    red = cutted_img[y][x][0]
    green = cutted_img[y][x][1]
    blue = cutted_img[y][x][2]
    return int(red) + int(green) + int(blue)

def set_colors(cutted_img, x, y, color, step):
    cutted_img[y][x][0] = int(color // step) * step
    cutted_img[y][x][1] = int(color // step) * step
    cutted_img[y][x][2] = int(color // step) * step

image = Image.open("img2.jpg")
pixels = np.array(image)
size = int(input("Размер мозайки: "))
step = 256 / int(input("Градация: "))
cutted_img = cut_off_img(pixels, size)
height = len(cutted_img)
width = len(cutted_img[1])
y = 0
while y < height:
    x = 0
    while x < width:
        color = 0
        for y1 in range(y, y + size):
            for x1 in range(x, x + size):
                color += get_colors(cutted_img, x1, y1)
        color = int(color // (size ** 2))
        for y1 in range(y, y + size):
            for x1 in range(x, x + size):
                set_colors(cutted_img, x1, y1, color / 3, step)
        x = x + size
    y = y + size

res = Image.fromarray(pixels)
res.save('res.jpg')
