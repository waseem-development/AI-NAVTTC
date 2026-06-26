import cv2
import numpy as np

# Read image
img = cv2.imread("./Images/white_bg.jpeg", cv2.IMREAD_GRAYSCALE)

# Step 1: Gaussian Smoothing
blur = cv2.GaussianBlur(img, (5, 5), 1)

# Step 2-5: Canny Edge Detector
# threshold1 = Low Threshold
# threshold2 = High Threshold
edges = cv2.Canny(
    blur,
    threshold1=100,
    threshold2=200
)

# Display results
cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", blur)
cv2.imshow("Canny Edges", edges)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27: 
        break

cv2.destroyAllWindows()