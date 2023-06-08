import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('hoa.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow('image')

cv2.createTrackbar('H min', 'image', 0, 255, nothing)
cv2.createTrackbar('H max', 'image', 255, 255, nothing)

cv2.createTrackbar('S min', 'image', 0, 255, nothing)
cv2.createTrackbar('S max', 'image', 255, 255, nothing)

cv2.createTrackbar('V min', 'image', 0, 255, nothing)
cv2.createTrackbar('V max', 'image', 255, 255, nothing)

while True:
    h_min = cv2.getTrackbarPos('H min', 'image')
    h_max = cv2.getTrackbarPos('H max', 'image')
    s_min = cv2.getTrackbarPos('S min', 'image')
    s_max = cv2.getTrackbarPos('S max', 'image')
    v_min = cv2.getTrackbarPos('V min', 'image')
    v_max = cv2.getTrackbarPos('V max', 'image')

    lower_color = np.array([h_min, s_min, v_min])
    upper_color = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower_color, upper_color)

    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('image', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()