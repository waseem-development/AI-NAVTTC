import cv2
import numpy as np

kernel = np.ones((3,3)) / 1/9

img = cv2.imread("./Images/noisy.jpg")
smooth = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Smooth", smooth)

while True:
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

cv2.destroyAllWindows()