from sqlite3 import Row
import cv2 as cv


 #lecture1
im1 = cv.imread('assets/anime.jpg',1)
im1=cv.imread('assets/anime.jpg')
for i in range(100):
     for j in range(100):
         im1[i,j]=(0,0,255)
0,cv.IMREAD_GRAYSCALE #grayscale of our image
1,cv.IMREAD_UNCHANGED #unchanged version
cv.imshow("Anime" , im1)
cv.waitKey(0) #this means wait infinitely until i press the button
cv.destroyAllWindows()
