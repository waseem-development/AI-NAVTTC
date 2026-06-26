import cv2
import numpy as np

img = cv2.imread("./Images/white_bg.jpeg")

blur = cv2.GaussianBlur(img, (3,3), 0)

sobel_x_kernel = np.array([[-1,-2,-1],
                             [ 0, 0, 0],
                             [ 1, 2, 1]], dtype=np.float32)

sobel_y_kernel = np.array([[-1,0,1],
                             [-2,0,2],
                             [-1,0,1]], dtype=np.float32)

gx = cv2.filter2D(blur, cv2.CV_32F, sobel_x_kernel)
gy = cv2.filter2D(blur, cv2.CV_32F, sobel_y_kernel)

# magnitude = np.sqrt(gx**2, gy**2)
magnitude = cv2.magnitude(gx, gy)
magnitude = cv2.convertScaleAbs(magnitude)

print(f"magnitude: {magnitude}")
cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", blur)
cv2.imshow("Sobel X", cv2.convertScaleAbs(gx))
cv2.imshow("Sobel Y", cv2.convertScaleAbs(gy))
cv2.imshow("Sobel Edge", magnitude)
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    
cv2.destroyAllWindows()


