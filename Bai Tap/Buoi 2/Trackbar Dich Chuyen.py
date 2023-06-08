import cv2
import numpy as np

def on_trackbar_change(val):
    global image, dx, dy
    dx, dy = val, val
    rows, cols = image.shape[:2]
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
    cv2.imshow('Translated Image', translated_image)


image = cv2.imread('D:\\Tran Quyen\\Document\\Image\\full.png')
dx, dy = 0, 0

cv2.imshow('Original Image', image)

cv2.namedWindow('Translated Image')
cv2.createTrackbar('Dich anh', 'Translated Image', 0, 100, on_trackbar_change)
while True:
    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()
