import numpy as np
import cv2 as cv

img1 = cv.imread('afganG.jpg')  # read it colored by default 0 for grayscale
img2 = cv.imread('nature.jpg')
# getting the attributes of specific image
print(img1.size)
print(img1.shape)
print(img1.dtype)

b,g,r = cv.split(img1)  # to split the image to it's three channels red, green, blue
img1 = cv.merge((b,g,r))    # tomerge the color channels and formulate the image again

# resizing the images to enable merging it in one image
img1 = cv.resize(img1, (512, 512))
img2 = cv.resize(img2, (512, 512))

img = cv.addWeighted(img1, .6, img2, .3, 0) # numbers define the transparency of each image, 0 defines the transparency of whole image

# This is space to adjust eh image by duplicating some features

# ............................

cv.imshow('merged_img', img)
cv.waitKey(0)
cv.destroyAllWindows()
