import cv2

img = cv2.imread("")
(h,w) = img.shape[:2]
goc = 0
def get_goc(x):
    global goc 
    goc = x
cv2.namedWindow("Xoay")
cv2.createTrackbar('Goc','Xoay',0,360,get_goc)
while True:
    M = cv2.getRotationMatrix2D((w/2,h/2), goc, 1)
    ro = cv2.warpAffine(img, M,(w,h))
    cv2.imshow("Xoay", ro)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()