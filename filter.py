from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                p1 = arr[n][n1][0]
                p2 = arr[n][n1][1]
                p3 = arr[n][n1][2]
                M = np.array([p1, p2, p3]).astype(np.int32)
                s += sum(M)
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int((s // 50) * 50)/3
                arr[n][n1][1] = int((s // 50) * 50)/3
                arr[n][n1][2] = int((s // 50) * 50)/3
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')