import cv2
import numpy as np
from scipy import signal

def convolution_scipy(F, H):
    return signal.convolve2d(F, H, mode='same')

img = cv2.imread("./Images/japan_street.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3,3), dtype=np.float32)

print("start")
filtered_img = convolution_scipy(img, kernel)
print("done")

filtered_img = cv2.normalize(filtered_img, None, 0, 255, cv2.NORM_MINMAX)
filtered_img = filtered_img.astype(np.uint8)

cv2.imshow("Original", img)
cv2.imshow("Convolution", filtered_img)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()