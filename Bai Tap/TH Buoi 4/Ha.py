import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png", 0)

edges_canny = cv2.Canny(img, 100, 200)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
edges_sobel = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
edges_sobel = np.uint8(edges_sobel)

plt.subplot(2,2,1), plt.imshow(img, cmap= 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(img, cmap= 'gray')
plt.title('Canny edges'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(img, cmap= 'gray')
plt.title('Sobel edges'), plt.xticks([]), plt.yticks([])
plt.show()
