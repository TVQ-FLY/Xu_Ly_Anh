import cv2
import numpy as np

def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def on_trackbar_change(val):
    global image, angle
    angle = val
    rotated_image = rotate_image(image, angle)
    cv2.imshow('Rotated Image', rotated_image)


image = cv2.imread('D:\\Tran Quyen\\Document\\Image\\full.png')
angle = 0

cv2.imshow('Original Image', image)

cv2.namedWindow('Rotated Image')
cv2.createTrackbar('Angle', 'Rotated Image', angle, 360, on_trackbar_change)

while True:
    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()
