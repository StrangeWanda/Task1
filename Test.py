import cv2
import numpy as np

imgs = [cv2.imread(f"{a}.webp") for a in "abcd"]
cp = (9,6)

objp = np.zeros((cp[0]*cp[1],3),np.float32)
objp[:,:2] = np.mgrid[0:cp[0],0:cp[1]].T.reshape(-1,2)

impoints=[]
obpoints=[]

for img in imgs:
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, cp, None)
    if ret == True:
        impoints.append(corners)
        obpoints.append(objp)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obpoints, impoints, gray.shape[::-1], None, None)

# now we do pose estimation of aruco markers
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
aruco_params = cv2.aruco.DetectorParameters_create()
#aruco_params.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_SUBPIX

v = cv2.VideoCapture(0)
while True:
    ret, frame = v.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=aruco_params)
    if len(corners) > 0:
        rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist)
        frame = cv2.aruco.drawAxis(frame, mtx, dist, rvec, tvec, 0.1)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 27:
        break
