from sqlite3 import Row
import cv2 as cv
import numpy as np

im1 = cv.imread("assets/anime.jpg")
im2 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
row = im1.shape[0]
col = im1.shape[1]
im3 = np.zeros((row, col), np.uint8)

for i in range(row):
    for j in range(col):
        im3[i, j] = 255-im2[i, j]  # we change their values to their negotions

cv.imshow("Negated Lelouch", im3)
cv.imshow("Lelouch", im2)

cv.waitKey(0)
cv.destroyAllWindows()
