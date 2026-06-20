import cv2
import numpy as np

img = cv2.imread("./Images/noisy.jpg")

sharpen_kernel = np.array([
    [0, -1 ,0],
    [-1, 5 ,-1],
    [0, -1 ,0],])

sharpened = cv2.filter2D(img, -1, sharpen_kernel)
cv2.imshow("Before", img)
cv2.imshow("After", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()