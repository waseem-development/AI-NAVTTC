import cv2
import numpy as np

img = cv2.imread("./Images/lena.png")

if img is None:
    print("Could not load the image")
else:
    # cv2.circle(img, center, radius, color, thickness)
    color = (0, 0, 255)
    thickness = 2
    center = (250,230)
    radius = 175
    cv2.circle(img, center, radius, color, thickness)
    cv2.imshow("Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()