import cv2

img = cv2.imread('colored_balls.png')
img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gry, 235, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('number of contours=', str(len(contours)))
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

cv2.imshow('image', img_gry)
cv2.imshow('image_color', img)
cv2.waitKey(0)

cv2.destroyAllWindows


# this part to adjust the contours by using a trackbar......................
# cv2.namedWindow('image')
# def output(x):
#     print(x, '\n', 'number of contours=', str(len(contours)))
# # Trackbar name, the image in connection, start varying point, end point, fuction to excute
# cv2.createTrackbar('Thre', 'image', 0, 255, output)
# while(1):
#     Thre = cv2.getTrackbarPos('Thre', 'image')
#     ret, thresh = cv2.threshold(img_gry, Thre, 255, 0)
#     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    

#     cv2.imshow('image', img_gry)
#     cv2.imshow('image_color', img)
#     K = cv2.waitKey(10)
#     if K == 27:
#         break
#     cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

# cv2.destroyAllWindows
