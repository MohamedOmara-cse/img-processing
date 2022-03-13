import numpy as np
import cv2 as cv

img = cv.imread('photo.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('result.jpg',res)
