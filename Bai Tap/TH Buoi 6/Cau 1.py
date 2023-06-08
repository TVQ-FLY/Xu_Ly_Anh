import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("hoa.png")

anh_xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gauss = cv2.GaussianBlur(anh_xam, (5,5), 1)
thich_nghi = cv2.adaptiveThreshold(anh_xam, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

kernel = np.ones((5,5), np.uint8)
dilated_img = cv2.dilate(anh_xam, kernel, iterations=1)
eroded_img = cv2.erode(anh_xam, kernel, iterations=1)
opened_img = cv2.morphologyEx(anh_xam, cv2.MORPH_OPEN, kernel)
closed_img = cv2.morphologyEx(anh_xam, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Anh xam", anh_xam)
cv2.imshow("Thich nghi", thich_nghi)

plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(2, 3, 2)
plt.imshow(anh_xam, cmap='gray')
plt.title('Grayscale Image')

plt.subplot(2, 3, 3)
plt.imshow(dilated_img, cmap='gray')
plt.title('Dilated Image')

plt.subplot(2, 3, 4)
plt.imshow(eroded_img, cmap='gray')
plt.title('Eroded Image')

plt.subplot(2, 3, 5)
plt.imshow(opened_img, cmap='gray')
plt.title('Opened Image')

plt.subplot(2, 3, 6)
plt.imshow(closed_img, cmap='gray')
plt.title('Closed Image')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
