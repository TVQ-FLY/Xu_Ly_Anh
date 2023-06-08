import cv2

face_cascade = cv2.CascadeClassifier('D:\\Tran Quyen\\Code\\Xu Ly Anh\\Nhan dien khuon mat\\haar-cascade-files\\haarcascade_frontalface_default.xml')

img = cv2.imread('D:\Tran Quyen\Code\Xu Ly Anh\Nhan dien khuon mat\\full.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()
