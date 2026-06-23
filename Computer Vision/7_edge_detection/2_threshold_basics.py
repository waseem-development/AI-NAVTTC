import cv2
import numpy as np

img = cv2.imread("./Images/einstein.jpg")

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply threshold
ret, thresh_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", img)
cv2.imshow("Threshold Image", thresh_img)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()