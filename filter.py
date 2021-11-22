import argparse
import numpy as np
from PIL import Image


def crop_img(pixels, distance):
    height_overflow = len(pixels) % distance
    width_overflow = len(pixels[1]) % distance
    return pixels[:len(pixels) - height_overflow,
                  :len(pixels[0]) - width_overflow]


parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="path to image")
parser.add_argument("--output", dest="output", type=str, help="path to result image", default="res.jpg")
parser.add_argument("--size", dest="size", type=int, help="mozaik size", default=10)
parser.add_argument("--gradations", dest="gradation_count", type=int, help="How many gray gradations will be in result image", default=4)
args = parser.parse_args()

img = Image.open(args.input)
mozaik_size = args.size
gradation = args.gradation_count
res_file = args.output

pixels = np.array(img)
gradation_step = 256 / gradation

pixels = crop_img(pixels, mozaik_size)
height = len(pixels)
width = len(pixels[1])

for x in range(0, width - mozaik_size+1, mozaik_size):
    for y in range(0, height - mozaik_size+1, mozaik_size):
        mozaik = pixels[y:y + mozaik_size, x:x + mozaik_size]
        average = np.average(mozaik)
        average = int(average//gradation_step) * gradation_step
        mozaik.fill(average)

res = Image.fromarray(pixels)
res.save(res_file)