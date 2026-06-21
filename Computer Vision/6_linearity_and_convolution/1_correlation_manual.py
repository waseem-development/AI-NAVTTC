import numpy as np
import cv2

def correlated2d_manual(f,h):
    """G(i,j) = sum_k sum_l h[k,l] * f(i+k, j+l) --- No Flip"""
    n = h.shape[0] // 2                         # kernel half width
    f_padded = np.pad(f, n, mode="constant")    # zero-pad the border
    out = np.zeros_like(f, dtype=float)

    for i in range(f.shape[0]):
        for j in range(f.shape[1]):
            print(i, j)
            region = f_padded[i:i+h.shape[0], j:j+h.shape[1]]  # region = f_padded[1:4,1:4]
            out[i, j] = np.sum(region * h)     # direct overlay, dot product
    return out


img = cv2.imread("./Images/japan_street.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3,3))
print("start")
filtered_img = correlated2d_manual(img, kernel)
print("done")
cv2.imshow("Original", img)
cv2.imshow("Filtered", filtered_img)
while True:
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
cv2.destroyAllWindows()