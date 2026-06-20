# Image Filtering Process
# Raw Image  |
#            | Gaussian Blur
#            | Median Blur
#            | Sharpening Filters

# Image Filtering VS Blurring

import cv2
import numpy as np

img = cv2.imread("./Images/noisy.jpg")

gaussian_blur_img = cv2.GaussianBlur(img, (7, 7), 0)
median_blur_img = cv2.medianBlur(img, 7)
# Create resizable windows
cv2.namedWindow("Noisy Lena", cv2.WINDOW_NORMAL)
cv2.namedWindow("Gaussian Blur", cv2.WINDOW_NORMAL)
cv2.namedWindow("Median Blur", cv2.WINDOW_NORMAL)
# Display images
cv2.imshow("Noisy Lena", img)
cv2.imshow("Gaussian Blur", gaussian_blur_img)
cv2.imshow("Median Blur", gaussian_blur_img)

print(img)
print("\n\n\n\n--------------------\n\n\n\n")
print(gaussian_blur_img)
print("\n\n\n\n--------------------\n\n\n\n")
print(median_blur_img)

# Wait until ESC is pressed
while True:
    key = cv2.waitKey(1) & 0xFF # 0xFF = 255

    if key == 27:  # ESC key
        break

cv2.destroyAllWindows()