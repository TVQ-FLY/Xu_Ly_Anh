import cv2

img = cv2.imread('')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

cv2.imshow("Anh tach bien", sobel)
cv2.imwrite('tach_bien.jpg', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
