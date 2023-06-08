import cv2
image = cv2.imread('')
(rows, cols) = img.shape[:2]
alpha = 0
def set_alpha(pos):
    global alpha
    alpha = pos
cv2.namedWindow('show')
cv2.resizeWindow('show', 500, 100)
cv2.createTrackbar('goc quay','show',0,360, set_alpha)

while True:
    M = cv2.getRotationMatrix2D(center = (cols/2,rows/2), angle=alpha, scale=1)
    ro = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('show',ro)

    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()