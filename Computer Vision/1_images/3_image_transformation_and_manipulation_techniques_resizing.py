# # Image Transformation and Manipulation Techniques
# Drawing Shapes:
#  - Lines
#  - Circles
#  - Rectangles

# Rotation and Flipping

# Resizing and Scaling (cv2.resize)

# Cropping using slicing

# Adding Text:
#  - Text Placement
#  - Font Selection

# Step 1: Resizing and Scaling Images
# resized = cv2.resize(src, dsize,     fx,     fy,   interpolation)
# variable             img, dimension, width, height, for controlling quality etc. Note: fx, fy and interpolation are optional

import cv2

img = cv2.imread("./Images/fruit.png", 1)
print(img.shape)
if img is None:
    print("Could not load image")
else:
    print("Image Loaded")
    resized = cv2.resize(img, (1000, 1000)) # 300 width and 300 height
    cv2.imshow("Original Image", img)
    cv2.imshow("Resized Image", resized)

    cv2.imwrite("Outputs/Resized_Output.png", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
