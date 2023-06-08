# Bo loc trung binh
# import cv2

# img = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png")

# img_filtered = cv2.blur(img, (3, 3))

# cv2.imshow("img_filtered", img_filtered)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Bộ lọc trung vị
# import cv2

# img = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png")

# img_filtered = cv2.medianBlur(img, 3)

# cv2.imshow("MedianBlur", img_filtered)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Bộ lọc Gauss
# import cv2

# img = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png")

# img_filtered = cv2.GaussianBlur(img, (3, 3), 0)

# cv2.imshow("GaussianBlur", img_filtered)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Bộ lọc Bilateral
# import cv2

# img = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png")

# img_filtered = cv2.bilateralFilter(img, 5, 75, 75)

# cv2.imshow("bilateralFilter", img_filtered)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Thay doi kich thuoc Kenel
# import cv2
# import numpy as np

# cv2.namedWindow("image")
# kernel_size = 3

# def on_trackbar(val):
#     global kernel_size
#     kernel_size = val if val % 2 != 0 else val + 1

# cv2.createTrackbar("kernel size", "image", kernel_size, 31, on_trackbar)

# while True:
#     img = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png")
#     blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
#     cv2.imshow("image", blurred)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cv2.destroyAllWindows()
