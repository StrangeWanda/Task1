import cv2
import time

I=cv2.VideoCapture(0)

while 1:

    _, f = I.read()

    print(type(f))

    cv2.imshow("Test", f)
    time.sleep(100)
