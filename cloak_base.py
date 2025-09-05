import cv2
import time

# 1. Start webcam
cap = cv2.VideoCapture(0)  # 0 = default webcam
time.sleep(2)  # small delay to let camera adjust

# 2. Capture background (without you in frame)
ret, background = cap.read()
background = cv2.flip(background, 1)  # mirror effect

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # mirro
