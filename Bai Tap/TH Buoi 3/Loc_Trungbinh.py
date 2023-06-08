import cv2

img = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png")

loc_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Loc trung binh", loc_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()