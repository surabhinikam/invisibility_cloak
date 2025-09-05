import cv2

cap = cv2.VideoCapture(0)

# Force window to appear
cv2.namedWindow("Webcam Feed", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam Feed", 640, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Webcam Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:  # press 'q' or Esc to exit
        break

cap.release()
cv2.destroyAllWindows()
print("Program ended, terminal is back to normal")
