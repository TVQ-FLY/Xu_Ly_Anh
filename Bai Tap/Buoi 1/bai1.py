import cv2

image = cv2.imread("D:\\Tran Quyen\\Document\\Image\\avartar.png")

cv2.imshow('Original', image)

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('newImage.jpg', image)
cv2.imshow("new image grayscale", gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

