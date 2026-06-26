import cv2
import numpy as np

img = cv2.imread("./Images/white_bg.jpeg", 0)

blur = cv2.GaussianBlur(img, (5,5), 1)

laplacian = cv2.Laplacian(blur, cv2.CV_64F)

laplacian_display = cv2.convertScaleAbs(laplacian)

# ---------- (b) Find the Zero Crossing ----------
# A zero crossing happens where the Laplacian changes sign between
# neighbouring pixels (the {+,-} , {+,0,-} , {-,+} , {-,0,+} cases from
# the Marr-Hildreth method). For every pixel we look at its 3x3
# neighbourhood: if that neighbourhood contains both a positive and a
# negative value, a zero crossing passes through this pixel.

def find_zero_crossing(lap):
    rows, cols = lap.shape
    zero_cross = np.zeros((rows, cols), dtype=np.uint8)
    slope = np.zeros((rows, cols), dtype=np.float64)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            neighborhood = lap[i-1:i+2, j-1:j+2]
            max_val = neighborhood.max()
            min_val = neighborhood.min()

            if max_val > 0 and min_val < 0:
                zero_cross[i, j] = 255
                # ---------- (c) Slope of the zero-crossing ----------
                # Slope of zero-crossing {a, -b} is |a + b|
                slope[i, j] = abs(max_val) + abs(min_val)

    return zero_cross, slope

zero_crossing_img, slope_map = find_zero_crossing(laplacian)

# Normalize slope map to 0-255 so it can be displayed / thresholded like an image
slope_display = cv2.normalize(slope_map, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Apply a threshold to the slope to keep only strong edges (as in the lecture:
# "Compute slope of zero-crossing, Apply a threshold to slope")
THRESHOLD = 30
_, edges_from_slope = cv2.threshold(slope_display, THRESHOLD, 255, cv2.THRESH_BINARY)

cv2.namedWindow("Laplacian", cv2.WINDOW_NORMAL)
cv2.namedWindow("Zero Crossing", cv2.WINDOW_NORMAL)
cv2.namedWindow("Slope Map", cv2.WINDOW_NORMAL)
cv2.namedWindow("Final Edges (Slope Thresholded)", cv2.WINDOW_NORMAL)

cv2.imshow("Laplacian", laplacian_display)
cv2.imshow("Zero Crossing", zero_crossing_img)
cv2.imshow("Slope Map", slope_display)
cv2.imshow("Final Edges (Slope Thresholded)", edges_from_slope)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()