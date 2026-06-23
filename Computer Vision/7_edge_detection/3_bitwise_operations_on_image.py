# Bitwise Operations on Images:
# --- Combine two iamges
# --- Cut out a specific part from one image using another image
# --- Flip / Remove Specific regions in an image

# ============================
# BITWISE OPERATIONS IN IMAGES
# ============================

# 1) BITWISE AND (&)
# -------------------
# Rule:
# pixel = 1 ONLY if BOTH images have pixel = 1
# otherwise pixel = 0

# In images:
# --- Keeps ONLY overlapping white/bright regions
# --- Used for masking (cutting a region from image)

# Example idea:
# image1 AND image2 = common visible area only


# 2) BITWISE OR (|)
# ------------------
# Rule:
# pixel = 1 if EITHER image has pixel = 1

# In images:
# --- Combines two images
# --- Shows everything from both images
# --- Used when merging masks or objects

# Example idea:
# image1 OR image2 = union of both images


# 3) BITWISE XOR (^)
# -------------------
# Rule:
# pixel = 1 if pixels are DIFFERENT
# pixel = 0 if pixels are SAME

# In images:
# --- Highlights differences between images
# --- Removes overlapping regions
# --- Useful for change detection

# Example idea:
# image1 XOR image2 = only non-common parts visible


import cv2
import numpy as np

img1 = np.zeros((300,300), dtype="uint8")
img2 = np.zeros((300,300), dtype="uint8")

cv2.circle(img1, (150, 150), 100, 255, -1) # -1 means fill this shape 
cv2.rectangle(img2, (100,100), (250, 250), 255, -1) # -1 means fill this shape 

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)

bitwise_not1 = cv2.bitwise_not(img1)
bitwise_not2 = cv2.bitwise_not(img2)

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)

cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT (img1)", bitwise_not1)
cv2.imshow("Bitwise NOT (img2)", bitwise_not2)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()