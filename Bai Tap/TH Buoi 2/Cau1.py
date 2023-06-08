import cv2
import numpy as np

img = cv2.imread("D:\\ha.png")

pts1 = np.float32([[343,31],[643,34],[356,127],[646,125]])
pts2 = np.float32([[0,0],[310,0],[0,297],[310,297]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(310,297))
  
cv2.imshow("results", dst)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()