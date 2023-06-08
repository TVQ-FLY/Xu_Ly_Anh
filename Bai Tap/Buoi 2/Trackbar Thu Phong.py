import cv2
import numpy as np

def on_trackbar_change(val):
    global image, scale
    scale = val / 100.0
    rows, cols = image.shape[:2]
    resized_image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('Resized Image', resized_image)


image = cv2.imread('D:\\Tran Quyen\\Document\\Image\\full.png')
scale = 1.0

cv2.imshow('Original Image', image)

cv2.namedWindow('Resized Image')
cv2.createTrackbar('Scale', 'Resized Image', 100, 200, on_trackbar_change)

# Vòng lặp chờ đợi người dùng bấm phím ESC để thoát
while True:
    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()
