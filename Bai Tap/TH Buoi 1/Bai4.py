import cv2

def on_trackbar(val):
    threshold_value = cv2.getTrackbarPos("Threshold", "Binary")
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary", binary_image)
    cv2.imwrite("binary_image.jpg", binary_image)

image = cv2.imread("D:\\Tran Quyen\\Document\\Image\\kp.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Binary")

cv2.createTrackbar("Threshold", "Binary", 0, 255, on_trackbar)

cv2.imshow("Original", image)
cv2.imshow("Binary", gray_image)

cv2.imwrite("D:\\Tran Quyen\\Document\\Image\\gray_img.jpg", gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
