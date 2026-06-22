import cv2
import numpy as np


def correlated2d_manual(f, h):
    """
    G(i,j) = Σk Σl h[k,l] * f(i+k, j+l)
    CORRELATION (NO FLIP)
    """
    n = h.shape[0] // 2

    # zero-padding
    f_padded = np.pad(f, n, mode="constant")

    # output image
    out = np.zeros_like(f, dtype=float)

    # slide kernel over image
    for i in range(f.shape[0]):
        for j in range(f.shape[1]):
            region = f_padded[i:i+h.shape[0], j:j+h.shape[1]]
            out[i, j] = np.sum(region * h)

    return out


def convolve2d_manual(f, h):
    """
    CONVOLUTION = flip kernel by 180° then perform correlation
    """
    h_flipped = np.flipud(np.fliplr(h))
    return correlated2d_manual(f, h_flipped)


# ======================
# Load image
# ======================
img = cv2.imread("./Images/grayscale_cat.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("Image not found. Check path.")

# ======================
# Define kernel
# ======================
kernel = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=np.float32)

# ======================
# Apply operations
# ======================
correlation_img = correlated2d_manual(img, kernel)
convolution_img = convolve2d_manual(img, kernel)

# Normalize for display (because values can exceed [0,255])
correlation_img = cv2.normalize(correlation_img, None, 0, 255, cv2.NORM_MINMAX)
convolution_img = cv2.normalize(convolution_img, None, 0, 255, cv2.NORM_MINMAX)

correlation_img = correlation_img.astype(np.uint8)
convolution_img = convolution_img.astype(np.uint8)

# ======================
# Show results
# ======================
cv2.imshow("Original", img)
cv2.imshow("Correlation (No Flip)", correlation_img)
cv2.imshow("Convolution (180° Flip)", convolution_img)

while True:
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cv2.destroyAllWindows()