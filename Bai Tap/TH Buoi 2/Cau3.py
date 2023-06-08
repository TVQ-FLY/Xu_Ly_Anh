import cv2
img = cv2.imread('D:\\Tran Quyen\\h.jpg')
alpha = 0
def get_alpha(pos):
    global alpha
    alpha = pos if pos % 2 != 0 else pos + 1
beta = 0
def get_beta(pos):
    global beta
    beta = pos if pos % 2 != 0 else pos + 1
cv2.namedWindow('show')
cv2.resizeWindow('show', 500, 100)
cv2.createTrackbar('Truc X','show',1,4,get_alpha)
# cv2.createTrackbar('Truc Y','show',1,4,get_beta)
while True:
    output = cv2.resize(img, None,fx=0.5*alpha,fy= 0.5*alpha, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('anh',output)
  
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()


