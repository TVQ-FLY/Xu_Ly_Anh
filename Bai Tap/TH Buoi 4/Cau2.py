import cv2

img = cv2.imread('')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)

cv2.imshow("Anh tach bien", laplacian)
cv2.imwrite('', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()