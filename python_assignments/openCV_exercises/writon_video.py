# The tutorial to learn how to write on a video on it.
# the first lesson is to capture the video and show it in gray scale
import numpy as np
import cv2 as cv
import datetime
cap = cv.VideoCapture(0)    # (task 1)
# cap = cv.VideoCapture('vtest.avi')    # video capture from device (task 2)

# (task 4) adjusting and enquiring the camera parameters

# print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# cap.set(cv.CAP_PROP_FRAME_WIDTH, 700)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 400)

# to see after the change
# width = str(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = str(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# see if the script was able to connect with the camera
if cap is False:
    print('cannot access the camera')
    exit()

while True:
    ret, frame = cap.read() # this command read the video and store it in var (frame) and returns vat (ret) as boolean if it can read it or not
    if ret is False:
        print('cannot receive the frames')
        break
    # text = 'width: '+width+'height:'+height
    time_now = str(datetime.datetime.now())
    font = cv.FONT_HERSHEY_SIMPLEX
    # frame = cv.putText(frame,text,(20,40), font, 1,(255,0,0),1,cv.LINE_AA) # text, location, fontformat, fontsize, color, thickness, linetype
    frame = cv.putText(frame, time_now, (20,40), font, 1, (0,255,255), 1, cv.LINE_AA) # text, location, fontformat, fontsize, color, thickness, linetype
    # working on the variable frame to convert to gray color
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame_gray', frame)
    # the value inside the waitkey() dictate the frame rate per milisecond lower value mean high FBS, higher video quality
    if cv.waitKey(1) == ord('q'):
        break

# stop capturing 
cap.release()
cv.destroyAllWindows()