import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0) #opens the default camera
time.sleep(2) #pauses for 2 sec so the webcam adjusts to lighting before it captures anyhting

#capturing the background
for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)  #This is the background that will “replace” the cloak later.

while cap.isOpened():  #keeps the webcam running
    ret, frame = cap.read()
    if not ret:
        break
    frame = np.flip(frame, axis=1) #mirror effect

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #BGR=blue,green,red;HSV= hue saturation value

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])


    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2
#cv2.inRange() → Makes a mask where the color is within the given range.
#mask1 + mask2 → Combines both masks for full red detection.
#Mask = 1 where cloak is, 0 everywhere else.

mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8)) #removes small tiny dots
mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8)) # makes the detected area bigger and smoother

mask_inv = cv2.bitwise_not(mask) #msk_inv is everything except the cloak.

res1= cv2.bitwise_and(background, background, mask=mask) #bg where the cloak is present
res2 = cv2.bitwise_and(frame, frame, mask=mask_inv) #bg where the cloak is NOT present

final_output = cv2.addWeighted(res1,1,res2,1,0)

cv2.imshow("Invisibility Cloak", final_output)

if cv2.waitKey(1) & 0xFF == 27:  #press Esc to exit
    break

cap.release()
cv2.destroyAllWindows()


