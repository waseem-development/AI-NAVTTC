import cv2
import numpy as np
from scipy import signal

def correlation_scipy(F,H):
    G = signal.correlate2d(F, H, mode='same')  # same shape as F
    return G

img = cv2.imread("./Images/japan_street.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3,3), dtype=np.float32)
print("start")
filtered_img = correlation_scipy(img, kernel)
print("done")
cv2.imshow("Original", img)
cv2.imshow("Filtered", filtered_img)
while True:
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
cv2.destroyAllWindows()