import cv2

image = cv2.imread('D:\\Tran Quyen\\quyen.jpg')

img = cv2.resize(image, (400, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, nhi_phan = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(nhi_phan, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,0,255), 1)

cv2.imshow('Anh goc', img)
cv2.imshow('Countours', img.copy())
cv2.waitKey(0)
cv2.destroyAllWindows()

