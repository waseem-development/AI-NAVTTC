import cv2
import numpy as np

img = cv2.imread("./Images/white_bg.jpeg", 0)

blur = cv2.GaussianBlur(img, (5,5), 0)

sobel_gx = cv2.Sobel(blur, cv2.CV_32F, 1, 0, ksize=3)
sobel_gy = cv2.Sobel(blur, cv2.CV_32F, 0, 1, ksize=3)

magnitude = cv2.magnitude(sobel_gx, sobel_gy)
magnitude = cv2.convertScaleAbs(magnitude)

threshold = 50

_, thresh = cv2.threshold(magnitude, threshold, 255, cv2.THRESH_BINARY)

cv2.namedWindow("Thresholded", cv2.WINDOW_NORMAL)
cv2.imshow("Thresholded", thresh)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()