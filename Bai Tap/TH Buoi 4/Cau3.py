import cv2

img = cv2.imread('')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 100, 200)

cv2.imshow("Canny", canny)
cv2.imwrite('', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
