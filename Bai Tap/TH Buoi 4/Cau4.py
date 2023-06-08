import cv2
import matplotlib.pyplot as plt

img = cv2.imread('')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)

canny = cv2.Canny(gray, 100, 200)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')
axs[0, 1].imshow(sobel, cmap='gray')
axs[0, 1].set_title('Sobel Edge Detection')
axs[1, 0].imshow(laplacian, cmap='gray')
axs[1, 0].set_title('Laplacian Edge Detection')
axs[1, 1].imshow(canny, cmap='gray')
axs[1, 1].set_title('Canny Edge Detection')
plt.show()
