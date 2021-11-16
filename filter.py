from PIL import Image
import numpy as np


def get_average(kernel):
    average = 0
    for x in range(KERNEL_SIZE):
        for y in range(KERNEL_SIZE):
            red = int(kernel[x][y][0])
            green = int(kernel[x][y][1])
            blue = int(kernel[x][y][2])
            average += (red + green + blue) / 3
    average = average / (KERNEL_SIZE*KERNEL_SIZE)
    average = int(average//STEP_SIZE) * STEP_SIZE
    return average


def fill_with(value, kernel):
    for x in range(KERNEL_SIZE):
        for y in range(KERNEL_SIZE):
            kernel[x][y][0] = value
            kernel[x][y][1] = value
            kernel[x][y][2] = value


KERNEL_SIZE = 10
STEP_COUNT = 5
STEP_SIZE = 256 // STEP_COUNT
input_image = Image.open("img2.jpg")
image = np.array(input_image)
width = len(image)
height = len(image[1])

for x in range(0, width-KERNEL_SIZE+1, KERNEL_SIZE):
    for y in range(0, height-KERNEL_SIZE+1, KERNEL_SIZE):
        kernel = image[x : x+KERNEL_SIZE, y : y+KERNEL_SIZE]
        average = get_average(kernel)
        fill_with(average, kernel)

result_image = Image.fromarray(image)
result_image.save('res.jpg')
