import numpy as np
from PIL import Image
import warnings

warnings.filterwarnings("error")

img = Image.open("img2.jpg")
img_pixels = np.array(img)
width = len(img_pixels)
height = len(img_pixels[1])
x = 0
while x < width - 1:
    y = 0
    while y < height - 1:
        sum_of_10_pixels = 0
        for cur_x in range(x, x + 10):
            for cur_y in range(y, y + 10):
                red = img_pixels[cur_x][cur_y][0]
                greed = img_pixels[cur_x][cur_y][1]
                blue = img_pixels[cur_x][cur_y][2]
                try:
                    average_pixels_value = (red + greed + blue) / 3
                except RuntimeWarning:
                    average_pixels_value = (int(red) + int(greed) + int(blue)) / 3
                sum_of_10_pixels += average_pixels_value
        sum_of_10_pixels = int(sum_of_10_pixels // 100)
        for cur_x in range(x, x + 10):
            for cur_y in range(y, y + 10):
                img_pixels[cur_x][cur_y][0] = int(sum_of_10_pixels // 50) * 50
                img_pixels[cur_x][cur_y][1] = int(sum_of_10_pixels // 50) * 50
                img_pixels[cur_x][cur_y][2] = int(sum_of_10_pixels // 50) * 50
        y = y + 10
    x = x + 10
res_image = Image.fromarray(img_pixels)
res_image.save('res.jpg')
