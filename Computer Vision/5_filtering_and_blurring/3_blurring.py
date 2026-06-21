import cv2 
import numpy as np

img = cv2.imread("./Images/noisy.jpg")

smooth = cv2.blur(img, (3,3))
gaussian_blur = cv2.GaussianBlur(img, (3,3), 0)

cv2.imshow("Original Noisy Image", img)
cv2.imshow("Smooth Image", smooth)
cv2.imshow("Gaussian Blur Image", gaussian_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()