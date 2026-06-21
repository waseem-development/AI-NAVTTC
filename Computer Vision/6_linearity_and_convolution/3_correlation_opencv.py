import cv2
import numpy as np

# 1. Load image (grayscale recommended for 2D kernel)
img = cv2.imread("./Images/japan_street.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("Image not found. Check path.")

# 2. Define kernel
kernel = np.ones((3,3), dtype=np.float32)

# 3. Apply correlation / convolution
# ddepth = -1 → same output type as input image
filtered_img = cv2.filter2D(img, ddepth=-1, kernel=kernel)

# 4. Show results
cv2.imshow("Original", img)
cv2.imshow("Filtered", filtered_img)

# 5. Wait for ESC key
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()