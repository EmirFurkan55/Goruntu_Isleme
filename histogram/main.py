import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("spiderman.jpg",0)
cv2.imshow("spiderman", image)
cv2.waitKey()

shape = image.shape
yukseklik = shape[0]
genislik = shape[1]

histogram = np.zeros(256)

for i in range(0, yukseklik):
    for j in range(0, genislik):
        histogram[image[i][j]] += 1

print(histogram)

plt.figure("Histogram")
plt.xlabel("Renk Değerleri")
plt.ylabel("Yoğunluk")
plt.plot(histogram)
plt.show()




