import cv2

img = cv2.imread("D:\\Tran Quyen\\quyen.jpg")
print(img.shape[:2])
kenel = 3
def get_kenel(x):
    global kenel
    kenel = x

cv2.namedWindow("Bo loc trung binh")
cv2.createTrackbar("Kenel","Bo loc trung binh",0,10,get_kenel)

while True:
    trung_binh = cv2.blur(img, (kenel, kenel))
    cv2.imshow("Bo loc trung binh", trung_binh)
    if cv2.waitKey(1) == ord('s'):
        break
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite("D:\\Tran Quyen\\trung binh.png",trung_binh)
cv2.destroyAllWindows()