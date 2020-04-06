import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('11.jpg')
img = cv.resize(img1, (800, 800))

# Trackbar name, the image in connection, start varying point, end point, fuction to excute
_, th1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
kernel2 = np.ones((5, 5), np.float32)
imerode = cv.erode(th1, kernel2, iterations=1)
imfinal = cv.dilate(imerode, kernel2, iterations=2)
# zz = imfinal[:, 400, 0]
imlength = len(imfinal)
count = 0

def subtractor(list):
    length = len(list)
    result = []
    for i in range(1, length, 1):
        iii = list[i]-list[i-1]
        result.append(iii)
    return result

blackpixels_perCloumn = []
for i in range(imlength):
    for ii in imfinal[:,i,0]:
        if ii == 255:
            continue
        else:
            # count = count+1
            count += 1
    blackpixels_perCloumn.append(count)
    count = 0
# print(blackpixels_perCloumn)
difference = subtractor(blackpixels_perCloumn)
# print(difference)
for e, zz in enumerate(difference):
    if zz > 7:
        print(e, zz)
        break_point = e-1
        break



XX = np.linspace(0,800,len(blackpixels_perCloumn))
plt.plot(XX,blackpixels_perCloumn)
plt.title("A number of black pixels per each column in the image")
plt.xlabel("column number")
plt.ylabel("intensity of black pixels")

# start coordinate, end coordinate, color(BGR), thickness / the line to mark the starting point for droplet formulation
cv.line(imfinal, (break_point, 10), (break_point, 790), (0, 0, 255), 2)
# find the contours resulted from frames substraction
plt.show()
# cv.imshow('image', th1)
cv.imshow('final_image', imfinal)
cv.imwrite('dropletStart_detection.jpg', imfinal)
K = cv.waitKey()
# now exploring different types of threshold
# or Gaussian type [Numbers: threshold, number of pixels to be in calculation, the offset constant]
# to get the color channels (RGB) from the trackbar
if K == 27:
    cv.destroyAllWindows()
