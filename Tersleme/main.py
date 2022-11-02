import cv2
import numpy as np

image = cv2.imread('spiderman.jpg',0)
cv2.imshow(" Image", image)

shape = image.shape
yukseklik  = shape[0]
yogunluk = shape[1]

TerslenmisImage = np.zeros([yukseklik,yogunluk], dtype=np.uint8)
for i in range(0, yukseklik):
    for j in range(0, yogunluk):
        TerslenmisImage[i,j] = 255 - image[i,j]

cv2.imshow("Terslenmis Image",TerslenmisImage)
cv2.waitKey()