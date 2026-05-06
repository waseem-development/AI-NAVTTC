import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./Images/fruit.png", cv2.IMREAD_GRAYSCALE)
print("Image Resolution:", img.shape)
patch = img[100:140, 30:60]   # 40×40 patch
cv2.imshow("Corpped Fruit Image",patch)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Patch shape:", patch.shape)   # (30, 30)
print("Patch values:\n", patch)      # raw pixel values          
