import cv2
from scipy import signal
import numpy as np

pad = 15
img = cv2.imread("./Images/einstein.jpg")
if img is None:
    raise Exception("Image not found")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # <-- convert to 2D
kernel = np.ones((3,3))

zero_padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_CONSTANT)
replicate_border = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
reflect_border = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REFLECT)
wrap_border = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_WRAP)

cv2.imshow("Original", img)
cv2.imshow("Zero / Clip-Back", zero_padded)
cv2.imshow("Border Replicate", replicate_border)
cv2.imshow("Border Reflect", reflect_border)
cv2.imshow("Border Wrap", wrap_border)

G1 = signal.convolve2d(gray, kernel, mode='same', boundary='fill', fillvalue=0)   # zero
G2 = signal.convolve2d(gray, kernel, mode='same', boundary='symm')               # reflect
G3 = signal.convolve2d(gray, kernel, mode='same', boundary='wrap')               # wrap

cv2.imshow("Scipy Zero", G1.astype(np.uint8))
cv2.imshow("Scipy Reflect", G2.astype(np.uint8))
cv2.imshow("Scipy Wrap", G3.astype(np.uint8))

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()