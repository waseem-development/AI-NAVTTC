import cv2
import numpy as np

kernel = np.array([
    [-1, 0, 1],
    [-1, 0, 1], 
    [-1, 0, 1]])

img = cv2.imread("./Images/noisy.jpg")
filtered = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Filtered Image", filtered)

while True:
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cv2.destroyAllWindows()