import numpy as np
import cv2 as cv


def output(x):
    pass


cv.namedWindow('Tracking')

# to create a trackbar in HSV system for color alternation
# Trackbar name, the image in connection, start varying point, end point, fuction to excute
cv.createTrackbar('LH', 'Tracking', 0, 255, output)
cv.createTrackbar('LS', 'Tracking', 0, 255, output)
cv.createTrackbar('LV', 'Tracking', 0, 255, output)
cv.createTrackbar('UH', 'Tracking', 255, 255, output)
cv.createTrackbar('US', 'Tracking', 255, 255, output)
cv.createTrackbar('UV', 'Tracking', 255, 255, output)


while(1):
    # frame = cv.imread('colored_balls.png')
    frame = cv.imread('colored.jpeg')

    Newframe = cv.resize(frame, (700, 700))
    hsv = cv.cvtColor(Newframe, cv.COLOR_BGR2HSV)
    
    l_h = cv.getTrackbarPos('LH', 'Tracking')
    l_s = cv.getTrackbarPos('LS', 'Tracking')
    l_v = cv.getTrackbarPos('LV', 'Tracking')

    u_h = cv.getTrackbarPos('UH', 'Tracking')
    u_s = cv.getTrackbarPos('US', 'Tracking')
    u_v = cv.getTrackbarPos('UV', 'Tracking')

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, lower_bound, upper_bound)
    resulted_img = cv.bitwise_and(Newframe, Newframe, mask=mask)

    cv.imshow('Newframe', Newframe)
    cv.imshow('mask', mask)
    cv.imshow('resulted_img', resulted_img)

    k = cv.waitKey(1)
    if k == 27:
        break
    # to change the color of the image simultaneously with shifting the slider of trackbar
cv.destroyAllWindows()
