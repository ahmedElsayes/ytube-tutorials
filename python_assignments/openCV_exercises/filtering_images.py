import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_init = cv.imread('color_balls.jpg')  # to read in grayscale

# make kernel filter to smooth the image
kernel = np.ones((5,5), np.float32) / 25

img = cv.cvtColor(img_init, cv.COLOR_BGR2RGB)
img_kernel = cv.filter2D(img, -1, kernel)  # kernel filter
blur = cv.blur(img, (5, 5))  # act like a low pass filter
Gblur = cv.GaussianBlur(img, (5, 5), 0)

# to get the image in grayscale
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
img_gray_kernel = cv.cvtColor(img_kernel, cv.COLOR_RGB2GRAY)
img_gray_blur = cv.cvtColor(blur, cv.COLOR_RGB2GRAY)
img_gray_Gblur = cv.cvtColor(Gblur, cv.COLOR_RGB2GRAY)
# img = cv.cvtColor(img_init, cv.COLOR_BGR2RGB)
threshold_var = 245     # modify this threshold till reaching the wanted result

# now exploring different types of threshold
# _, th1 = cv.threshold(img_gray, threshold_var, 255, cv.THRESH_BINARY_INV)
# _, th2 = cv.threshold(img_gray_kernel, threshold_var, 255, cv.THRESH_BINARY_INV)
# _, th3 = cv.threshold(img_gray_blur, threshold_var, 255, cv.THRESH_BINARY_INV)
_, th4 = cv.threshold(img_gray_Gblur, threshold_var, 255, cv.THRESH_BINARY_INV)

kernel2 = np.ones((5, 5), np.float32)
im_dilated1 = cv.dilate(th4, kernel2, iterations=1)
im_dilated2 = cv.dilate(th4, kernel2, iterations=5)
im_morph = cv.morphologyEx(th4, cv.MORPH_OPEN, kernel2) # make erosion first then dilation
im_eroded = cv.erode(th4, kernel2, iterations=2)


images = [img, img_kernel, blur, Gblur, img_gray,
          img_gray_kernel, img_gray_blur, img_gray_Gblur, im_dilated1, im_dilated2, im_morph, im_eroded]
length = len(images)
Titles = ['Original', 'img_kernel',
          'blur', 'Gblur', 'img_gray', 'img_gray_kernel', 'img_gray_blur', 'img_gray_Gblur', 'im_dilated1', 'im_dilated2', 'im_morph', 'im_eroded']


for ii in range(length):
    print(ii)
    plt.subplot(4, 3, ii+1), plt.imshow(images[ii], 'gray')
    plt.title(Titles[ii])
    plt.xticks([]), plt.yticks([])
plt.subplots_adjust(bottom=0.15, wspace=0.15, hspace=0.35)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
