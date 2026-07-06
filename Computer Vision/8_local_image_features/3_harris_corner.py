import cv2                      # Import OpenCV library
import numpy as np              # Import NumPy for numerical operations

# -----------------------------
# Read the input image
# -----------------------------
img = cv2.imread("./Images/japan_street.jpg")

# Check if the image was loaded successfully
if img is None:
    raise FileNotFoundError("Image not found — check your path!")

# -----------------------------
# Convert the color image (BGR) to Grayscale
# Harris Corner Detection works only on grayscale images
# -----------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -----------------------------
# Convert image datatype from uint8 to float32
# Required by cv2.cornerHarris()
# -----------------------------
gray = np.float32(gray)

# -----------------------------
# Apply Harris Corner Detector
#
# Parameters:
# gray      : Input grayscale float32 image
# 2         : blockSize (2×2 neighborhood for the structure matrix)
# 5         : Sobel kernel size used to compute image gradients
# 0.04      : Harris detector free parameter (usually 0.04–0.06)
# -----------------------------
dst = cv2.cornerHarris(gray, 2, 5, 0.04)

# -----------------------------
# Dilate (expand) detected corner responses
# This is ONLY for better visualization.
# It makes corner points thicker and easier to see.
#
# None means use the default 3×3 structuring element.
# -----------------------------
dst = cv2.dilate(dst, None)

# -----------------------------
# Threshold the Harris response.
#
# dst.max() gives the strongest corner response.
# 0.01 * dst.max() is the threshold.
#
# Every pixel whose Harris score is greater than
# 1% of the strongest corner is considered a corner.
#
# Those pixels in the original image are colored RED.
#
# OpenCV uses BGR format:
# [Blue, Green, Red]
# [0, 0, 255] = Red
# -----------------------------
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# -----------------------------
# Create resizable windows
# WINDOW_NORMAL allows resizing by dragging the window.
# -----------------------------
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Harris Corner Output", cv2.WINDOW_NORMAL)

# -----------------------------
# Display the original image
# (with detected corners marked in red)
# -----------------------------
cv2.imshow("Original", img)

# -----------------------------
# Display the Harris response image.
#
# Bright pixels = Strong corner response
# Dark pixels   = Weak or no corner response
# -----------------------------
cv2.imshow("Harris Corner Output", dst)

# -----------------------------
# Keep the windows open until
# the user presses the ESC key.
# -----------------------------
while True:

    # Wait 1 millisecond for a key press
    key = cv2.waitKey(1) & 0xFF

    # ASCII code 27 = ESC key
    if key == 27:
        break

# -----------------------------
# Close all OpenCV windows
# -----------------------------
cv2.destroyAllWindows()