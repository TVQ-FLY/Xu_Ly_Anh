import cv2
import matplotlib.pyplot as plt

img = cv2.imread("")

anh_xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(anh_xam, 127, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
erode = cv2.erode(thresh, kernel, iterations=1)
dilate = cv2.dilate(thresh, kernel, iterations=1)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contour = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 2)


plt.subplot(231), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(232), plt.imshow(cv2.cvtColor(erode, cv2.COLOR_BGR2RGB))
plt.subplot(233), plt.imshow(cv2.cvtColor(dilate, cv2.COLOR_BGR2RGB))
plt.subplot(234), plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))
plt.subplot(235), plt.imshow(cv2.cvtColor(closing, cv2.COLOR_BGR2RGB))
plt.subplot(236), plt.imshow(cv2.cvtColor(img_contour, cv2.COLOR_BGR2RGB))

plt.show()