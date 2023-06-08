import cv2

img = cv2.imread("D:\\Tran Quyen\\Document\\Image\\kp.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold = 127 
max_value = 255 
ret, binary_img = cv2.threshold(gray_img, threshold, max_value, cv2.THRESH_BINARY)

cv2.imshow("Gray", gray_img)
cv2.imshow("Binary", binary_img)
cv2.imwrite("D:\\Tran Quyen\\Document\\Image\\gray_img.jpg", gray_img)
cv2.imwrite("D:\\Tran Quyen\\Document\\Image\\binary_img.jpg", binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
