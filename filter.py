from PIL import Image
import numpy as np


KERNEL_SIZE = 10
STEP_COUNT = 5
STEP_SIZE = 256 // STEP_COUNT
input_image = Image.open("img2.jpg")
image = np.array(input_image)
width, height, _ = image.shape

for x in range(0, width-KERNEL_SIZE+1, KERNEL_SIZE):
    for y in range(0, height-KERNEL_SIZE+1, KERNEL_SIZE):
        kernel = image[x:x+KERNEL_SIZE, y:y+KERNEL_SIZE]
        average = np.average(kernel)
        average = int(average//STEP_SIZE) * STEP_SIZE
        kernel.fill(average)

result_image = Image.fromarray(image)
result_image.save('res.jpg')
