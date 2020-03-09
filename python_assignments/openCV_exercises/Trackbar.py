import numpy as np
import cv2 as cv

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

def output(x):
    print(x)

# to create a switch for enabling or disablying the trackbar alternator
switch = '0:OFF\n 1:ON'
cv.createTrackbar(switch, 'image', 0, 1, output)
# to create a track bar
cv.createTrackbar('B', 'image', 0, 255, output) # Trackbar name, the image in connection, start varying point, end point, fuction to excute
cv.createTrackbar('G', 'image', 0, 255, output)
cv.createTrackbar('R', 'image', 0, 255, output)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1)
    if k == 27:
        break
    # to get the color channels (RGB) from the trackbar
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    S = cv.getTrackbarPos(switch, 'image')
    if S == 0:
        img[:] = [255, 0, 0]
    else:
        img[:] = [b, g, r]
    # to change the color of the image simultaneously with shifting the slider of trackbar
cv.destroyAllWindows()


