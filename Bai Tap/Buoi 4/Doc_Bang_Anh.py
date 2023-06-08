import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

image = cv2.imread('D:\Tran Quyen\Document\Image\Bar_Code.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

decoded_objects = pyzbar.decode(gray)

for obj in decoded_objects:
    print("Data:", obj.data)

    pts = np.array([obj.polygon], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(image,[pts],True,(0,255,0),3)

cv2.imshow("QR Code Image", image)
cv2.waitKey(0)
