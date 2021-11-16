import argparse

from PIL import Image
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(
        description='Чёрно-белый пискельный фильтр')
    parser.add_argument(
        'input',
        type=str,
        help='Путь до входного .jpg файла')
    parser.add_argument(
        '--out',
        dest='output',
        type=str,
        help='Путь до выходного .jpg файла (default: res.jpg)')
    parser.add_argument(
        '--size',
        dest='filter_size',
        type=int,
        help='Размер фильтра для обработки (default: 10)')
    parser.add_argument(
        '--step',
        dest='step_count',
        type=int,
        help='Количество градиентов серого в выходном изображении'
             + '(default: 5)')
    args = parser.parse_args()
    return (args.input,
            args.output or DEFAULT_OUTPUT_FILE_PATH,
            args.filter_size or DEFAULT_FILTER_SIZE,
            args.step_count or DEFAULT_STEP_COUNT)


def apply_filter(image):
    for x in range(0, width-filter_size+1, filter_size):
        for y in range(0, height-filter_size+1, filter_size):
            filter = image[x:x+filter_size, y:y+filter_size]
            average = np.average(filter)
            average = int(average//step_size) * step_size
            filter.fill(average)


def crop(image):
    cropped_width = (width//filter_size) * filter_size
    cropped_height = (height//filter_size) * filter_size
    return image[:cropped_width, :cropped_height]


DEFAULT_OUTPUT_FILE_PATH = "res.jpg"
DEFAULT_FILTER_SIZE = 10
DEFAULT_STEP_COUNT = 5

input_path, output_path, filter_size, step_count = parse_args()
step_size = 256 / step_count

input_image = Image.open(input_path)
image = np.array(input_image)
width, height, _ = image.shape

image = crop(image)
apply_filter(image)

result_image = Image.fromarray(image)
result_image.save(output_path)
