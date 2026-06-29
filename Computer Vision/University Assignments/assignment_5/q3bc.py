import cv2
import numpy as np

img = cv2.imread("./Images/white_bg.jpeg", 0)

if img is None:
    print("Error: Image not found!")
    exit()

blur = cv2.GaussianBlur(img, (5, 5), 0)

lap = cv2.Laplacian(blur, cv2.CV_64F)

zero_cross = np.zeros_like(img)

rows, cols = lap.shape

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        patch = lap[i - 1:i + 2, j - 1:j + 2]
        if patch.max() > 0 and patch.min() < 0:
            zero_cross[i, j] = 255

gx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

slope = cv2.magnitude(gx, gy)
slope = cv2.normalize(slope, None, 0, 255, cv2.NORM_MINMAX)
slope = np.uint8(slope)


cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Gaussian Blur", cv2.WINDOW_NORMAL)
cv2.namedWindow("Laplacian", cv2.WINDOW_NORMAL)
cv2.namedWindow("Zero Crossing", cv2.WINDOW_NORMAL)
cv2.namedWindow("Slope (Gradient Magnitude)", cv2.WINDOW_NORMAL)

cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur", blur)
cv2.imshow("Laplacian", np.uint8(np.absolute(lap)))
cv2.imshow("Zero Crossing", zero_cross)
cv2.imshow("Slope (Gradient Magnitude)", slope)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cv2.destroyAllWindows()