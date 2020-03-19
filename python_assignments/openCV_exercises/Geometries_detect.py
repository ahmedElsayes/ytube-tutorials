import cv2 as cv

img = cv.imread('geometries.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thre = cv.threshold(imgGray, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thre, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0,0,0), 2)   # index, color, thickness
    x = approx.ravel()[0]+20
    y = approx.ravel()[1]-12
    if len(approx) == 3:
        cv.putText(img, 'Triangle', (x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx) == 4:
        # to differentiate the rectangle from square
        x1, y1, w, h = cv.boundingRect(approx)
        ratio = w/h
        if 0.95 <=ratio<= 1.05:
            cv.putText(img, 'square', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, 'rectangle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif 5 <= len(approx) <= 7:
        cv.putText(img, 'pentagon', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv.putText(img, 'star', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv.putText(img, 'Circle', (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv.imshow('shapes', img)
cv.waitKey(0)
cv.destroyAllWindows()
