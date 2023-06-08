import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:\\Tran Quyen\\huong.jpg")

x1 = int(input("Nhap vao toa do x1: "))
y1 = int(input("Nhap vao toa do y1: "))
chieu_rong = int(input("Nhap vao chieu rong: "))
chieu_cao = int(input("Nhap vao chieu cao: "))

anh_cat = img[y1:y1 + chieu_cao, x1:x1 + chieu_rong]
anh_xam = cv2.cvtColor(anh_cat, cv2.COLOR_BGR2GRAY)
gau = cv2.GaussianBlur(anh_xam,(3,3), 0)
thich_nghi = cv2.adaptiveThreshold(anh_xam, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

plt.subplot(1,3,1), plt.imshow(anh_cat, cmap = 'gray'), plt.title("Anh cat")
plt.subplot(1,3,2), plt.imshow(gau, cmap = 'gray'), plt.title("Loc anh")
plt.subplot(1,3,3), plt.imshow(thich_nghi, cmap = 'gray'), plt.title("Phan nguong")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
