import cv2
import numpy as np

img = cv2.imread("./Images/lena.png")

if img is None:
    print("Could not load the image")
else:
    color = (0,0,255)
    thickness = 3
    text = f"This is Lena\'s Image for CV practice"
    # cv2.putText(img, text, org, font, fontScale, colorm thickness)
    cv2.putText(img, text, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, thickness)
    cv2.imshow("Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()