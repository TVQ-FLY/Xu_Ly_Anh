import cv2

# Open a video file
cap = cv2.VideoCapture('D:\\Tran Quyen\\Code\\Python\\Tran Van Quyen\\hi.mp4')

# Check if video file was successfully opened
if not cap.isOpened():
    print("Error opening video file")

# Loop through the video frames
while cap.isOpened():
    # Read a frame
    ret, frame = cap.read()

    # Check if end of video file has been reached
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Wait for a key press to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
