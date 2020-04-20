import cv2 as cv

cap = cv.VideoCapture('vtest.avi')   # 1- capture the video

ret, frame1 = cap.read()
ret, frame2 = cap.read()    # 2- reading the the video frame through two channels
# start a while loop to take the difference in video frames
while cap.isOpened():
    try:

        diff = cv.absdiff(frame1, frame2)   # 3- take the difference between the two frames
        gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY) # 4- mark the difference in grayscale
        blur = cv.GaussianBlur(gray, (5,5), 0)  # 5- Using a kernel filter with gaussian distribution
        _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)   # threshold on grayscale to tune motion detection
        dilated = cv.dilate(thresh, None, iterations=3) # TO FILTER THE UNWANTED CONTOURS INSIDE THE RESULT
        contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)    # find the contours resulted from frames substraction
        cv.drawContours(frame1, contours, -1, (255,0,0), 2) # draw all contours

        # *********This section to adjust the tracking boundaries to a rectangle..............
        # for contour in contours:
        #     (x,y,w,h) = cv.boundingRect(contour)

        #     if cv.contourArea(contour) > 900:
        #         cv.rectangle(frame1, (x,y), (x+w,y+h), (255,0,0), 2)
        #     else:
        #         continue

        # *********This section to adjust the tracking boundaries to a rectangle..............

        cv.imshow('motion_track', frame1)
        frame1 = frame2
        ret, frame2 = cap.read()    # frame 2 is is captured after the first frame with time mentioned in waitkey()

        K = cv.waitKey(40)
        if K == 27:
            break
    
    except:
        print('no more video frames')
        break
    
cv.destroyAllWindows()
