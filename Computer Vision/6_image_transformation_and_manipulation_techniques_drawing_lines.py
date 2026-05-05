import cv2
import numpy as np

img = cv2.imread("./Images/lena.png")

if img is None:
    print("Could not load the image")
else:
    h, w = img.shape[:2]

    center_x = w // 2
    center_y = h // 2

    color = (0, 0, 255)
    thickness = 2

    # -------------------------
    # X shape (diagonals)
    # -------------------------

    # top-left → bottom-right
    cv2.line(img, (0, 0), (w, h), color, thickness)

    # bottom-left → top-right
    cv2.line(img, (0, h), (w, 0), color, thickness)

    # -------------------------
    # + shape (cross)
    # -------------------------

    # horizontal line
    cv2.line(img, (0, center_y), (w, center_y), color, thickness) # start from row 0 and go to center of img then start from last row and go to center of img

    # vertical line
    cv2.line(img, (center_x, 0), (center_x, h), color, thickness)

    cv2.imshow("X + Cross Shape", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()