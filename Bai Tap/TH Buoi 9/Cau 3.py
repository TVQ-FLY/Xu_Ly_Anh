import cv2

img = cv2.imread("D:\\Tran Quyen\\h.jpg")

x = 0
def get_x(pos):
    global x
    x = pos

cv2.namedWindow("Canny")
cv2.createTrackbar('Nguong duoi','Canny',0,100,get_x)

while True:
    anh_xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,nhi_phan = cv2.threshold(anh_xam, 120, 255, cv2.THRESH_BINARY)
    canny = cv2.Canny(nhi_phan, x, x*3)
    cv2.imshow("Canny", canny)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()