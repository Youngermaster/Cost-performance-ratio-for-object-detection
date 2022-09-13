import numpy as np
import cv2

# creating the videocapture object
# and reading from the input file
# Change it to 0 if reading from webcam
cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()

    # if video finished or no Video Input
    if not success:
        break

    gray = cv2.resize(img, (500, 300))

    cv2.imshow('Image', gray)
    
    # press 'Q' if you want to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
