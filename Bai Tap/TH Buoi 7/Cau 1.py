import cv2
import matplotlib.pyplot as plt 

img = cv2.imread("D:\\Tran Quyen\\quyen.jpg")
# x1 = int(input("Nhap toa do x1: "))
# y1 = int(input("Nhap toa do y1: "))

# anh = img[0:x1, 0:y1]
# cv2.imshow("anh", )
hi = cv2.resize(img, (400, 500))
print(hi.shape[:2])
# x2 = int(input("Nhap toa do x2: "))
# y2 = int(input("Nhap toa do y2: "))

# anh_cat = img[y1:y2, x1:x2]

# anh_xam = cv2.cvtColor(anh_cat, cv2.COLOR_BGR2GRAY)
# anh_thichnghi = cv2.adaptiveThreshold(anh_xam, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# anh_canny = cv2.Canny(anh_xam, 100, 200)

# plt.subplot(2,2,1), plt.imshow(anh_cat, cmap='gray'), plt.title("Binh thuong"), plt.axis('off')
# plt.subplot(2,2,2), plt.imshow(anh_xam, cmap='gray'), plt.title("Anh xam"), plt.axis('off')
# plt.subplot(2,2,3), plt.imshow(anh_thichnghi, cmap='gray'), plt.title("Thich nghi"), plt.axis('off')
# plt.subplot(2,2,4), plt.imshow(anh_canny, cmap='gray'), plt.title("Tach bien"), plt.axis('off')
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
