import cv2
import numpy as np
import matplotlib.pyplot as plt

# cv2.getRotationMatrix2D(center, angle, scale)
# ------------------------------------------------------------
# This function creates a 2x3 transformation matrix used to rotate an image.
# The matrix contains information about:
#   - rotation (angle)
#   - scaling (zoom in/out)
#   - translation (so rotation happens around a specific point)

# center
# ------------------------------------------------------------
# A tuple (x, y) representing the point around which the image will rotate.
# Usually set to the center of the image:
#   center = (width // 2, height // 2)
# This ensures the image rotates around its middle instead of a corner.

# angle
# ------------------------------------------------------------
# The rotation angle in degrees.
#   Positive values  → rotate counterclockwise
#   Negative values  → rotate clockwise
# Example:
#   90   → rotate 90° counterclockwise
#  -90   → rotate 90° clockwise

# scale
# ------------------------------------------------------------
# A scaling factor applied during rotation.
#   1.0 → original size
#   >1  → zoom in
#   <1  → zoom out
# This allows resizing while rotating in a single step.

# ------------------------------------------------------------
# cv2.warpAffine(image, M, (width, height))
# ------------------------------------------------------------
# Applies the transformation matrix M to the image.

# image
# ------------------------------------------------------------
# The input image you want to transform.

# M
# ------------------------------------------------------------
# The 2x3 transformation matrix returned by cv2.getRotationMatrix2D().

# (width, height)
# ------------------------------------------------------------
# The size of the output image.
# Important: If the rotated image goes outside these bounds,
# parts of it may get cropped.

# ------------------------------------------------------------
# Overall Flow
# ------------------------------------------------------------
# 1. Compute transformation matrix M using:
#       cv2.getRotationMatrix2D(...)
# 2. Apply transformation using:
#       cv2.warpAffine(...)
# 3. Result = rotated (and possibly scaled) image


# cv2.flip(image, flipCode)
# ------------------------------------------------------------
# This function flips an image in different directions.

# image
# ------------------------------------------------------------
# The input image you want to flip.

# flipCode
# ------------------------------------------------------------
# This controls the direction of the flip:

#   0  → Vertical flip
#        (Top ↔ Bottom)
#        The image is flipped upside down.

#   >0 (usually 1) → Horizontal flip
#        (Left ↔ Right)
#        The image is mirrored like a mirror reflection.

#   <0 (usually -1) → Both vertical and horizontal flip
#        The image is flipped in both directions
#        (equivalent to rotating 180°)

# ------------------------------------------------------------
# Example behavior:
# ------------------------------------------------------------
# Original image → normal

# flipCode = 0
#   → image upside down

# flipCode = 1
#   → mirror image (like selfie camera)

# flipCode = -1
#   → rotated 180° effect (both flips applied)

# ------------------------------------------------------------
# Important Note:
# ------------------------------------------------------------
# cv2.flip does NOT rotate the image.
# It only mirrors it across axes.

img = cv2.imread("./Images/lena.png")

if img is None:
    print("Could not load the image")
else: 
    (h,w) = img.shape[:2]

    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.2)
    rotated_img = cv2.warpAffine(img, M, (w,h))
    flipped = cv2.flip(img, 1)
    cv2.imshow("Original Lena Image", img)
    cv2.imshow("Rotated Lena Image", rotated_img)
    cv2.imshow("Flipped Lena Image", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()