import cv2

img = cv2.imread("D:\\Tran Quyen\\huong.jpg")
tx = 1
def get_tx(x):
    global tx
    tx = x
ty = 1
def get_ty(x):
    global ty
    ty = x
cv2.namedWindow("Image")
cv2.createTrackbar('Tx','Image',1,50,get_tx)
cv2.createTrackbar('Ty','Image',1,50,get_ty)

while True:
    output = cv2.resize(img, None, fx = tx, fy = ty, interpolation = cv2.INTER_LINEAR)
    cv2.imshow("Image", output)
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite("D:\\Tran Quyen\\anh.png",output)
    if cv2.waitKey(1) == ord('q'):
        break
    if cv2.waitKey(1) == ord('p'):
        print("Kich thuoc cua anh la:{}".format(output.shape))
cv2.destroyAllWindows()