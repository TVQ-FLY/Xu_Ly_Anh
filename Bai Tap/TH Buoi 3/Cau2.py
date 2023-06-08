# a. Dùng chuột rê trên ảnh tạo thành hình chữ nhật, cắt ảnh từ vùng được chọn

import cv2

img = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png")

# variables
ix = -1
iy = -1
drawing = False

def draw_rectangle_with_drag(event, x, y, flags, param):
	
	global ix, iy, drawing, img
	
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		ix = x
		iy = y			
			
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			cv2.rectangle(img, pt1 =(ix, iy),
						pt2 =(x, y),
						color =(0, 255, 255),
						thickness =-1)
	
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		cv2.rectangle(img, pt1 =(ix, iy),
					pt2 =(x, y),
					color =(0, 255, 255),
					thickness =-1)
		
cv2.namedWindow(winname = "Title of Popup Window")
cv2.setMouseCallback("Title of Popup Window",
					draw_rectangle_with_drag)

while True:
	cv2.imshow("Title of Popup Window", img)
	
	if cv2.waitKey(10) == 27:
		break

cv2.destroyAllWindows()


 b. Dùng chuột chọn 4 điểm trên ảnh, thực hiện phép biến đổi phối cảnh với 4 điểm đã chọn

import cv2
import numpy as np

circles = np.zeros((4,2), np.int32)
counter = 0

def mouse(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter+1
        print(circles)
        cv2.circle(im,(x,y), 3,(0,255,0),-1)
im = cv2.imread('D:\\Tran Quyen\\Document\\Image\\quyen.png')
cv2.namedWindow('anh goc') 
while True:
    cv2.imshow('anh goc', im)
    cv2.setMouseCallback('anh goc', mouse)
    if counter == 4:
        w, h = 250,350
        MT1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        MT2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
        M = cv2.getPerspectiveTransform(MT1, MT2)
        output = cv2.warpPerspective(im, M, (w,h))
        cv2.imshow('Anh chieu', output)
    if cv2.waitKey(5) == ord('q'):
        break
cv2.destroyAllWindows()