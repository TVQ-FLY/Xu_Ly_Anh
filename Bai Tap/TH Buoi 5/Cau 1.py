import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\Tran Quyen\Document\Image\kp.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
adaptive_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
ret, otsu_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.subplot(2,2,1), plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(binary_img, cmap='gray')
plt.title('Binary Thresholding'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(adaptive_img, cmap='gray')
plt.title('Adaptive Thresholding'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(otsu_img, cmap='gray')
plt.title('Otsu Thresholding'), plt.xticks([]), plt.yticks([])

plt.show()