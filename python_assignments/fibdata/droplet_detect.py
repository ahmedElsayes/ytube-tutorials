import numpy as np
import cv2 as cv


img1 = cv.imread('image1.jpg')
img = cv.resize(img1,(512,512))
cv.namedWindow('track')

# threshold_var = 80

def output(x):
    print(x)

# Trackbar name, the image in connection, start varying point, end point, fuction to excute
cv.createTrackbar('thre', 'track', 150, 255, output)

while(1):
    threvar = cv.getTrackbarPos('thre', 'track')
    _, th1 = cv.threshold(img, threvar, 255, cv.THRESH_BINARY)
    # find the contours resulted from frames substraction
    cv.imshow('image', th1)
    k = cv.waitKey(1)
    if k == 27:
        break
    # now exploring different types of threshold
    # or Gaussian type [Numbers: threshold, number of pixels to be in calculation, the offset constant]
    # to get the color channels (RGB) from the trackbar
cv.destroyAllWindows()
