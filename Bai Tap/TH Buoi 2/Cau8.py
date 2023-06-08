import cv2
import numpy as np

img = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png")

pts1 = np.float32([[170,2],[668,6],[100,338],[639,397]])
pts2 = np.float32([[0,0],[210,0],[0,297],[210,297]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(210,297))
  
cv2.imshow("results", dst)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
