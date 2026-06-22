import cv2
import numpy as np
# Identity Filter
identity_kernel = np.array([[0,0,0], 
                         [0,0,1], 
                         [0,0,0]])

# Shift Kernel
shift_kernel = np.array([[0,0,0], 
                         [0,0,1], 
                         [0,0,0]])

#  Box Kernel
box_kernel = np.array([[1/9,1/9,1/9], 
                         [1/9,1/9,1/9], 
                         [1/9,1/9,1/9]])

# Sharpening kernel
sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)


# Sobel Kernel X
sobel_x_kernel = np.array([[1, 0, -1],
                           [1, 0, -1],
                           [1, 0, -1]])

# Sobel Kernel Y
sobel_y_kernel = np.array([[1, 2, 1],
                           [0, 0, 0],
                           [-1, -2, -1]])

img = cv2.imread("./Images/einstein.jpg")
identity = cv2.filter2D(img, 0, identity_kernel)
shifted = cv2.filter2D(img, 0, shift_kernel)
box = cv2.filter2D(img, 0, box_kernel)
sharpened = cv2.filter2D(img, 0, box_kernel)
sobel_x = cv2.filter2D(img, 0, sobel_x_kernel)
sobel_y = cv2.filter2D(img, 0, sobel_y_kernel)
cv2.imshow("Original", img)
cv2.imshow("Identity Filter", identity)
cv2.imshow("Shift Filter", shifted)
cv2.imshow("Box Filter", box)
cv2.imshow("Sharpening Filter", sharpened)
cv2.imshow("Sobel X Filter", sobel_x)
cv2.imshow("Sobel Y Filter", sobel_y)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()