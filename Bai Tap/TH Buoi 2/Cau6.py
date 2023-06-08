import cv2

# Hàm gọi lại (callback function) cho trackbar tỉ lệ thu phóng
def on_scale_change(val):
    global scale
    # Chuyển đổi giá trị của trackbar về tỉ lệ thu phóng
    scale = val / 100.0
    update_image()

# Hàm cập nhật ảnh
def update_image():
    # Tính kích thước mới của ảnh dựa trên tỉ lệ thu phóng
    h, w = img_original.shape[:2]
    new_size = (int(w * scale), int(h * scale))

    # Thực hiện thu phóng ảnh
    img_output = cv2.resize(img_original, new_size, interpolation=cv2.INTER_LINEAR)

    # Hiển thị ảnh đã được xử lý trên cửa sổ
    cv2.imshow("Image", img_output)

# Load ảnh
img_original = cv2.imread("D:\Tran Quyen\Document\Image\quyen.png")

# Tạo cửa sổ và trackbar
cv2.namedWindow("Image")
cv2.createTrackbar("Scale", "Image", 100, 300, on_scale_change)

# Hiển thị ảnh ban đầu
update_image()

# Vòng lặp chính
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        # Lưu ảnh đã được xử lý
        cv2.imwrite("image_output.jpg", img_output)
        print("Saved image as 'image_output.jpg'")
    elif key == ord("q"):
        # Kết thúc chương trình
        break

# Giải phóng bộ nhớ và đóng cửa sổ
cv2.destroyAllWindows()
