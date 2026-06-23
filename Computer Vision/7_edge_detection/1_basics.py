# 1) Canny Edge Detection: used for
# --- Border Detection
# --- Separate Objects
# --- Feature Extraction
# --- Face Rcognition
# This is very important 

# syntax: cv2.canny(img, th1, th2)

# Thresholding: make the image black-and-white based on brightness
# --- If picture is slightly bright, make it completely white (255)
# --- If picture is slightly dark, make it completely black (0)
# 
import cv2
import numpy as np

img = cv2.imread("./Images/fruit.png", cv2.IMREAD_GRAYSCALE)

th1 = 50
th2 = 150

edges = cv2.Canny(img, 50, 150)
cv2.imshow("Original Image", img)
cv2.imshow("Canny Image", edges)

while True: 
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
cv2.destroyAllWindows()