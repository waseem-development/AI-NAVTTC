import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# -----------------------------------------------------------
# A. CORRELATION, AUTO-CORRELATION, AND SSD
# -----------------------------------------------------------

def cross_correlation(f, h):
    """
    Cross-correlation:
    Measures similarity between image f and template h.
    Higher value = better match.
    """

    h_flipped = h[::-1, ::-1]
    return convolve2d(f, h_flipped,
                      mode='same',
                      boundary='symm')


def auto_correlation(f):
    """
    Auto-correlation of an image.
    Measures similarity with shifted versions of itself.
    """

    f_flipped = f[::-1, ::-1]
    return convolve2d(f,
                      f_flipped,
                      mode='same',
                      boundary='symm')


def ssd(patch1, patch2):
    """
    Sum of Squared Differences
    Smaller SSD = better match
    """

    patch1 = patch1.astype(np.float32)
    patch2 = patch2.astype(np.float32)

    return np.sum((patch1 - patch2) ** 2)


def template_matching_ssd(image, template):
    """
    Slide template across image.
    Compute SSD everywhere.
    """

    h, w = template.shape
    H, W = image.shape

    result = np.zeros((H - h + 1, W - w + 1),
                      dtype=np.float32)

    for i in range(H - h + 1):
        for j in range(W - w + 1):

            patch = image[i:i+h, j:j+w]
            result[i, j] = ssd(patch, template)

    best_location = np.unravel_index(
        np.argmin(result),
        result.shape
    )

    return result, best_location


# -----------------------------------------------------------
# Example
# -----------------------------------------------------------

# Read image
image = cv2.imread("./Images/white_bg.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Image not found.")

# Select template manually
template = image[80:130, 120:170]

# -----------------------------------------------------------
# Cross Correlation
# -----------------------------------------------------------

corr = cross_correlation(image, template)

# -----------------------------------------------------------
# Auto Correlation
# -----------------------------------------------------------

auto = auto_correlation(image)

# -----------------------------------------------------------
# SSD Matching
# -----------------------------------------------------------

ssd_map, best = template_matching_ssd(image, template)

top_left = best
bottom_right = (
    best[1] + template.shape[1],
    best[0] + template.shape[0]
)

result = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

cv2.rectangle(
    result,
    (top_left[1], top_left[0]),
    bottom_right,
    (0, 255, 0),
    2
)

print("Best Match Location:", best)
print("Minimum SSD:", ssd_map.min())

# -----------------------------------------------------------
# Display Results
# -----------------------------------------------------------

plt.figure(figsize=(15,8))

plt.subplot(231)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(232)
plt.imshow(template, cmap='gray')
plt.title("Template")
plt.axis("off")

plt.subplot(233)
plt.imshow(corr, cmap='jet')
plt.title("Cross Correlation")
plt.colorbar()

plt.subplot(234)
plt.imshow(auto, cmap='jet')
plt.title("Auto Correlation")
plt.colorbar()

plt.subplot(235)
plt.imshow(ssd_map, cmap='jet')
plt.title("SSD Map")
plt.colorbar()

plt.subplot(236)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Best SSD Match")
plt.axis("off")

plt.tight_layout()
plt.show()