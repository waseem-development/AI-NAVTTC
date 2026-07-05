import cv2
import numpy as np

# Import Image
img = cv2.imread("./Images/japan_street.jpg")
if img is None:
    raise FileNotFoundError("Image not found — check your path!")

# Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert from uint8 to float32
gray = np.float32(gray)

# Apply Harris Corner
dst = cv2.cornerHarris(gray, 2, 5, 0.04)

# Dilate (Thicken) the corners to be displayed in a good way
dst = cv2.dilate(dst, None)  # None means default 3x3 kernel

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Harris Corner Output", cv2.WINDOW_NORMAL)
cv2.imshow("Original", img)
cv2.imshow("Harris Corner Output", dst)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()