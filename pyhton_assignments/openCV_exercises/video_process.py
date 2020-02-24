# The tutorial to learn how to capture the video in openCV and process it.
# the first lesson is to capture the video and show it in gray scale
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)    # (task 1)
# cap = cv.VideoCapture('vtest.avi')    # video capture from device (task 2)

# (task 4) adjusting and enquiring the camera parameters
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

cap.set(cv.CAP_PROP_FRAME_WIDTH, 900)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 500)

# to see after the change
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# see if the script was able to connect with the camera
if cap is False:
    print('cannot access the camera')
    exit()

while True:
    ret, frame = cap.read() # this command read the video and store it in var (frame) and returns vat (ret) as boolean if it can read it or not
    if ret is False:
        print('cannot receive the frames')
        break
    # working on the variable frame to convert to gray color
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame_gray', gray)
    # the value inside the waitkey() dictate the frame rate per milisecond lower value mean high FBS, higher video quality
    if cv.waitKey(1) == ord('q'):
        break

# stop capturing 
cap.release()
cv.destroyAllWindows()

# Task3 ............writing a video from the one we capture
# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture(0)
# # Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480), True) # fbs, video size, color 
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv.flip(frame, 0)
#     # write the flipped frame
#     out.write(frame)
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break
# # Release everything if job is finished
# cap.release()
# out.release()
# cv.destroyAllWindows()