import cv2
import numpy as np
img = cv2.imread("D:\\Tran Quyen\\huong.jpg")

anh_xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x = int(input("Nhap vao gia tri phan nguong: "))
_,nhi_phan = cv2.threshold(anh_xam, x, 255, cv2.THRESH_BINARY)


kernel = np.ones((3,3), np.uint8)
dong_anh = cv2.erode(img, kernel, iterations=1)

mo_anh = cv2.dilate(dong_anh, kernel, iterations=1)
grad_x = cv2.Sobel(anh_xam, cv2.CV_32F, 1, 0, ksize=3)
grad_y = cv2.Sobel(anh_xam, cv2.CV_32F, 0, 1, ksize=3)
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)
grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

cv2.imshow("Anh phan nguong", nhi_phan)
cv2.imshow("Tach bien Sobel", grad)
cv2.imshow("Dong anh", dong_anh)
cv2.imshow("Mo anh", mo_anh)
while True: 
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite("D:\\Tran Quyen\\tachbien.png", grad)
    if cv2.waitKey(1) == ord('s'):
        break
cv2.destroyAllWindows()