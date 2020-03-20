# import cv2 as cv

# print(cv.__version__)

# # second_task
# img = cv.imread('nature.jpg', 0)    # 0 means reading it in grayscale 1 colored
# cv.imshow('new_img',img)
# cv.waitKey(5000)    # the number to hold image in seconds
# cv.destroyAllWindows()

# # third task
# cv.imwrite('messigray.png',img)

# # task 4
# import numpy as np
# import cv2 as cv
# img = cv.imread('nature.jpg',0)
# cv.imshow('image',img)
# k = cv.waitKey(0)
# if k == 27:         # wait for ESC key to exit
#     cv.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv.imwrite('messigray.png',img)
#     cv.destroyAllWindows()


# task 5
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('afganG.jpg',0)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.imshow(img, cmap = 'gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
