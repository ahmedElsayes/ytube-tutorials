import cv2 as cv
# import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient_grayscale.jpg')
threshold_var = 80
# now exploring different types of threshold
_, th1 = cv.threshold(img, threshold_var, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, threshold_var, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, threshold_var, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, threshold_var, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, threshold_var, 255, cv.THRESH_TOZERO_INV)

# # example on the use of adabtive threshold to discreminate special types of images(ex: the one with inproper illuminations)
# th6 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
# # or Gaussian type [Numbers: threshold, number of pixels to be in calculation, the offset constant]
# th6 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# plt.imshow('Image', img)
# plt.imshow('th1', th1)
# plt.imshow('th2', th2)
# cv.imshow('th3', th3)
# cv.imshow('th4', th4)
# cv.imshow('th5', th5)

images = [img, th1, th2, th3, th4, th5]
Titles = ['Original', 'Binary', 'Binary_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']


for ii in range(6):
    print(ii)
    plt.subplot(2,3, ii+1), plt.imshow(images[ii], 'gray')
    plt.title(Titles[ii])
    plt.xticks([]), plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
