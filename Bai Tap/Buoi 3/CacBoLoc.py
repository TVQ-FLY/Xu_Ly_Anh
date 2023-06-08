import cv2
import numpy as np

img = cv2.imread('D:\\Tran Quyen\\Document\\Image\\full.png')

quyen = cv2.blur(img, (50, 50))
quyen60k2 = cv2.medianBlur(img,5)
quyen2k1 = cv2.bilateralFilter(img,9,5,75)

cv2.imshow('Anh ban dau', img)
cv2.imshow('Bo loc trung binh', quyen)
cv2.imshow('Bo loc trung vi', quyen60k2)
cv2.imshow('Bo loc Bilateral', quyen2k1)
print("Code by tran van quyen")
cv2.waitKey(0)

cv2.destroyAllWindows()

# sigma_space
# sigma_color