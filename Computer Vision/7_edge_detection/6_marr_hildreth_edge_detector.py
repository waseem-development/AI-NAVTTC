import cv2
import numpy as np

img = cv2.imread("./Images/white_bg.jpeg", 0)

blur = cv2.GaussianBlur(img, (5,5), 1)

laplacian = cv2.Laplacian(blur, cv2.CV_64F)

laplacian_display = cv2.convertScaleAbs(laplacian)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", blur)
cv2.imshow("Laplacian", laplacian_display)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    
cv2.destroyAllWindows()


