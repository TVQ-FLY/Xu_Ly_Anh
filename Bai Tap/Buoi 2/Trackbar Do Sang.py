import cv2
img = cv2.imread("D:\\Tran Quyen\\Document\\Image\\full.png")

# Trackbar
beta = 0
def get_beta(pos):
    global beta
    beta = pos
alpha = 0
def get_alpha(pos):
    global alpha #khai bao bien toan cuc
    # alpha = pos
    alpha = pos


# Tao cua so hien thi thanh truot
cv2.namedWindow('Demo')
# Tao Trackbar
cv2.createTrackbar('Do sang', 'Demo', 0, 100, get_beta)
cv2.createTrackbar('Tuong phan', 'Demo', 0, 5, get_alpha)

while True:
    output = cv2.convertScaleAbs(img, alpha = alpha, beta = beta)
    cv2.imshow('Demo', output)
    if cv2.waitKey(10) == ord('q'):
        break
    
cv2.destroyAllWindows()