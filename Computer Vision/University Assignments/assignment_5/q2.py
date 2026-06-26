import cv2
import numpy as np

img = cv2.imread("./Images/white_bg.jpeg", 0)

blur = cv2.GaussianBlur(img, (5,5), 0)

edges = cv2.Canny(
    blur,
    threshold1=100,
    threshold2=200
)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Gaussian Blur", cv2.WINDOW_NORMAL)
cv2.namedWindow("Canny Edges", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", blur)
cv2.imshow("Canny Edges", edges)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27: 
        break

cv2.destroyAllWindows()
