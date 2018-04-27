import cv2
import numpy as np


def nothing(x):
    pass


device = cv2.VideoCapture(0)

cv2.namedWindow("Frame")

cv2.createTrackbar("Blue", "Frame", 0, 179, nothing)
cv2.createTrackbar("color/gray", "Frame", 0, 1, nothing)
while True:
    ret, frame = device.read()

    test = cv2.getTrackbarPos("Blue", "Frame")

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, str(test), (50, 150), font, 4, (0, 0, 255))

    s= cv2.getTrackbarPos("color/gray", "Frame")
    if s == 0:
        pass
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower_range = np.array([134, 0, 0])
    # upper_range = np.array([134, 200, 200])

    # mask = cv2.inRange(hsv, lower_range, upper_range)

    cv2.imshow("Frame", frame)

    # result = cv2.bitwise_and(frame, frame, mask=mask)
    # cv2.imshow("Result", result)

    key = cv2.waitKey(1)

    if key == 27:
        break

device.release()
cv2.destroyAllWindows()