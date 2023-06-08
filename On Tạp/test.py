import cv2

img = cv2.imread("D:\\Tran Quyen\\h.jpg")

print("Kích thước của ảnh là: {}".format(img.shape))
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()