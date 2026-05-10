import cv2 # import OpenCV
import numpy as np # import NumPy (for arrays)
# ── Load an image from disk ──────────────────────────────
# cv2.imread() reads the image file and returns a NumPy array
# The second argument:
# cv2.IMREAD_COLOR (=1) → load as colour (BGR, 3 channels)
# cv2.IMREAD_GRAYSCALE (=0) → load as grayscale (1 channel)
# cv2.IMREAD_UNCHANGED(-1) → load as-is including alpha
image = cv2.imread('./Images/japan_street.jpg', cv2.IMREAD_COLOR)
# ── Check if loading succeeded ───────────────────────────
# If the file was not found, imread returns None
if image is None:
    print('Error: Image not found!')
    exit(-1)
# ── Print image information ───────────────────────────────
print('Shape:', image.shape) # e.g. (512, 512, 3) → H x W x channels
print('dtype:', image.dtype) # e.g. uint8 → values 0–255
# ── Display the image in a window ────────────────────────
cv2.namedWindow('My Window', cv2.WINDOW_NORMAL) # create resizable window
cv2.imshow('My Window', image) # show image
cv2.waitKey(0) # wait for any key press
cv2.destroyAllWindows() 