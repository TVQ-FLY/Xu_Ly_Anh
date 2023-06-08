import cv2
import numpy as np

img = cv2.imread("")

pts1 = np.float32([[317,9],[667,6],[330,59],[667,65]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300,300))

cv2.imshow("Phoi canh", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()