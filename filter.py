import numpy as np
from PIL import Image
import warnings
warnings.filterwarnings("error")

img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 1:
    j = 0
    while j < a1 - 1:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                nn1 = arr[n][n1][0]
                nn2 = arr[n][n1][1]
                nn3 = arr[n][n1][2]
                try:
                    M = (nn1 + nn2 + nn3)/3
                except RuntimeWarning:
                    M = (int(nn1) + int(nn2) + int(nn3)) / 3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
