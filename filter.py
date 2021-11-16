
from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
arrLengthX = len(arr[0])
arrLengthY = len(arr[1])
i = 0

while i < arrLengthX - 1:
    j = 0
    while j < arrLengthY - 1:
        s = 0
        for n in range(i, i + 10):
            for r in range(j, j + 10):
                for e in range(3):
                    s += arr[n][r][e]
        s = int(s // 300)
        for n in range(i, i + 10):
            for r in range(j, j + 10):
                arr[n][r][0] = int(s // 50) * 50
                arr[n][r][1] = int(s // 50) * 50
                arr[n][r][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
