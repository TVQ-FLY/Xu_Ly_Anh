import cv2

image = cv2.imread('D:\Tran Quyen\quyen.png')

nhi_phan = 0
def get_nhiphan(x):
    global nhi_phan
    nhi_phan = x

cv2.namedWindow("Image")
cv2.createTrackbar('Nhi phan','Image',0,100,get_nhiphan)

while True:
    anh_xam = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, nhiphan = cv2.threshold(anh_xam, nhi_phan, 255, cv2.THRESH_BINARY)
    cv2.imshow("Image", nhiphan)
    if cv2.waitKey(1) == ord('a'):
        inverted_image = cv2.bitwise_not(nhiphan)
        cv2.imwrite('D:\\Tran Quyen\\inverted_image.jpg', inverted_image)
        print('Saved inverted image.')
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
