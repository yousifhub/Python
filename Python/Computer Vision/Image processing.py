import cv2
import numpy as np
import random

img = cv2.imread("Computer Vision/assets/Image/test imgs/hl2 lambda.png", 1)
img = cv2.resize(img, (0, 0), fx=3, fy=3)

while True:
    for i in range(675):
        for j in range(img.shape[1]):
            img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    cv2.imshow("Random", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()