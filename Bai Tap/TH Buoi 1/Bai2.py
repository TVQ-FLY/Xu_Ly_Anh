import cv2

img = cv2.imread("D:\\Tran Quyen\\Document\\Image\\kp.png")

x = int(input("Nhập tọa độ x: "))
y = int(input("Nhập tọa độ y: "))

color = img[x, y]

print("Giá trị màu tại điểm ảnh ({}, {}): {}".format(x, y, color))
