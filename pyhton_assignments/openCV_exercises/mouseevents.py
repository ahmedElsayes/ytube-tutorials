
# task 1
import numpy as np
import cv2 as cv

# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )

def event_click(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        xy = str(y) + ', ' + str(x)
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, xy, (x,y), font, 0.5, (255,0,0), 1, cv.LINE_AA)
        cv.imshow('image', img)
    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        xy = str(blue) + ', ' + str(green) + ', ' + str(red)
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, xy, (x,y), font, 0.5, (0,0,255), 1, cv.LINE_AA)
        cv.imshow('image', img)

# img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread('afganG.jpg')
cv.imshow('image', img)
cv.setMouseCallback('image',event_click)
cv.waitKey(0)
cv.destroyAllWindows()
