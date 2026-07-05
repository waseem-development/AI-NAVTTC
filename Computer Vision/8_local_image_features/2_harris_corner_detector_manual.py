import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.signal import convolve2d

# -----------------------------------------------------------
# B. HARRIS ERROR FUNCTION E(u,v) AND STRUCTURE MATRIX M
# -----------------------------------------------------------

def compute_structure_matrix(img,
                             sigma_grad=1.0,
                             sigma_window=1.5):
    """
    Compute the Harris Structure Matrix.

        M = [[Σ w Ix²,   Σ w IxIy],
             [Σ w IxIy,  Σ w Iy²]]
    """

    # -----------------------------------------
    # 1. Smooth image
    # -----------------------------------------
    img_smooth = gaussian_filter(img,
                                 sigma=sigma_grad)

    # -----------------------------------------
    # 2. Sobel kernels
    # -----------------------------------------
    Kx = np.array([
        [-1,0,1],
        [-2,0,2],
        [-1,0,1]
    ], dtype=np.float32)

    Ky = Kx.T

    # -----------------------------------------
    # 3. Image gradients
    # -----------------------------------------
    Ix = convolve2d(
        img_smooth,
        Kx,
        mode='same',
        boundary='symm'
    )

    Iy = convolve2d(
        img_smooth,
        Ky,
        mode='same',
        boundary='symm'
    )

    # -----------------------------------------
    # 4. Gradient products
    # -----------------------------------------
    Ix2 = Ix * Ix
    Iy2 = Iy * Iy
    IxIy = Ix * Iy

    # -----------------------------------------
    # 5. Gaussian weighted sums
    # -----------------------------------------
    M11 = gaussian_filter(
        Ix2,
        sigma=sigma_window
    )

    M22 = gaussian_filter(
        Iy2,
        sigma=sigma_window
    )

    M12 = gaussian_filter(
        IxIy,
        sigma=sigma_window
    )

    return M11, M12, M22, Ix, Iy


# -----------------------------------------------------------
# Harris Response
# -----------------------------------------------------------

def harris_response(M11,
                    M12,
                    M22,
                    k=0.05):

    det_M = M11 * M22 - M12**2

    trace_M = M11 + M22

    R = det_M - k * (trace_M ** 2)

    return R


# -----------------------------------------------------------
# Example
# -----------------------------------------------------------

img = cv2.imread(
    "./Images/white_bg.jpeg",
    cv2.IMREAD_GRAYSCALE
)

if img is None:
    raise FileNotFoundError(
        "image not found."
    )

img = img.astype(np.float32) / 255.0

# -----------------------------------------
# Compute Structure Matrix
# -----------------------------------------

M11, M12, M22, Ix, Iy = compute_structure_matrix(
    img,
    sigma_grad=1,
    sigma_window=1.5
)

# -----------------------------------------
# Harris Response
# -----------------------------------------

R = harris_response(
    M11,
    M12,
    M22,
    k=0.05
)

print("Maximum Harris Response :", np.max(R))
print("Minimum Harris Response :", np.min(R))

# -----------------------------------------------------------
# Visualization
# -----------------------------------------------------------

plt.figure(figsize=(15,10))

plt.subplot(231)
plt.imshow(img,
           cmap='gray')
plt.title("Original")
plt.axis("off")

plt.subplot(232)
plt.imshow(Ix,
           cmap='gray')
plt.title("Gradient Ix")
plt.axis("off")

plt.subplot(233)
plt.imshow(Iy,
           cmap='gray')
plt.title("Gradient Iy")
plt.axis("off")

plt.subplot(234)
plt.imshow(M11,
           cmap='jet')
plt.title("M11 = ΣwIx²")
plt.colorbar()

plt.subplot(235)
plt.imshow(M12,
           cmap='jet')
plt.title("M12 = ΣwIxIy")
plt.colorbar()

plt.subplot(236)
plt.imshow(M22,
           cmap='jet')
plt.title("M22 = ΣwIy²")
plt.colorbar()

plt.tight_layout()
plt.show()

# -----------------------------------------------------------
# Harris Response Visualization
# -----------------------------------------------------------

plt.figure(figsize=(8,6))

plt.imshow(R,
           cmap='jet')

plt.colorbar()

plt.title("Harris Response R")

plt.axis("off")

plt.show()