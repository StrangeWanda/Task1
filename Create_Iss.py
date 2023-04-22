# Take pics and save them in a folder when user presses c
import cv2

cap = cv2.VideoCapture(0)

i = 0

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("c"):
        cv2.imwrite(f"{i}.jpg", frame)
        i += 1
        break
