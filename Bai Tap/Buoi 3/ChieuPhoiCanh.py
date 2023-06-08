import cv2
import numpy as np

img = cv2.imread("D:\\Tran Quyen\\Code\\Xu Ly Anh\\Bai Tap\\Buoi 3\\test.jpg")

m1 = np.float32([[573,605],[1417,621],[553,1033],[1393,1021]])
m2 = np.float32([[0,0],[600,0],[0,300],[600,300]])

M = cv2.getPerspectiveTransform(m1, m2)
img1 = cv2.warpPerspective(img, M, (600, 300))

# Ham click chuot
def click_chuot(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Toa do cua chuot la:({}, {})".format(x, y))


cv2.imshow("Click chuot lay toa do", img)
cv2.setMouseCallback("Click chuot lay toa do", click_chuot)

cv2.imshow("Anh ban dau", img)
cv2.imshow("Dich chuyen", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()