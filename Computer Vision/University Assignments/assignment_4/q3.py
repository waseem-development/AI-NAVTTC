import cv2
import numpy as np

image_path = "./Images/noisy.jpg"

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("Image not found")

blur = cv2.GaussianBlur(img, (3,3), 0)

grad_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

gradient_mag = cv2.magnitude(grad_x, grad_y)
magnitude_8_bits = cv2.convertScaleAbs(gradient_mag)

thresh_val = 50
_, edge_map = cv2.threshold(magnitude_8_bits, thresh_val, 255, cv2.THRESH_BINARY)

cv2.imshow("Source Image", img)
cv2.imshow("Gradient X", cv2.convertScaleAbs(grad_x))
cv2.imshow("Gradient Y", cv2.convertScaleAbs(grad_y))
cv2.imshow("Gradient Magnitude", magnitude_8_bits)
cv2.imshow("Edge Map", edge_map)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()