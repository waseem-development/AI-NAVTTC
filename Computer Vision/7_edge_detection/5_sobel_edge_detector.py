import cv2
import numpy as np

img = cv2.imread("./Images/white_bg.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (3,3), 0)

# x-direction
gx = cv2.Sobel(blur, cv2.CV_32F, 1, 0, ksize=3)

# y-direction
gy = cv2.Sobel(blur, cv2.CV_32F, 0, 1, ksize=3)

magnitude = cv2.magnitude(gx, gy)
magnitude = cv2.convertScaleAbs(magnitude)

cv2.imshow("Original", img)
cv2.imshow("Sobel X", cv2.convertScaleAbs(gx))
cv2.imshow("Sobel Y", cv2.convertScaleAbs(gy))
cv2.imshow("Magnitude", magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()