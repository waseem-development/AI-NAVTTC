import cv2
import numpy as np

img = cv2.imread("./Images/lena.png")

if img is None:
    print("Could not load the image")
else:
    # cv2.rectangle(img, pt1, pt2, color, thickness)
    # pt1 is top left corner
    # pt2 is bottom right corner
    color = (0, 0, 255)
    thickness = 2
    pt1 = (50,50)
    pt2 = (200, 200)
    cv2.rectangle(img, pt1, pt2, color, thickness)
    cv2.imshow("Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()