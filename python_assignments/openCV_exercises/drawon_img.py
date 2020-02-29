import cv2 as cv

img = cv.imread('afganG',0)
cv.line(img, (0,0), (255,255), (0,0,255), 5)    # start coordinate, end coordinate, color(BGR), thickness
cv.arrowedLine(img, (255,0), (255,255), (0,0,255), 10)  # start coordinate, end coordinate, color(BGR), thickness
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)  # start coordinate, end coordinate, color(BGR), thickness
cv.circle(img,(447,63), 63, (0,0,255), -1)  # center of circle, radius, color(BGR), thickness -1 means that it filled with the specified color
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1) # center location, lengths of the two axises, rotation, ellipse section 0 & 360 gives full ellipse, color(BGR), thickness -1 means full color

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA) # text, location, forntformat, fontsize, color, thickness, linetype

cv.imshow('afgan_girl', img)
cv.waitKey(0)
cv.destroyAllWindows()