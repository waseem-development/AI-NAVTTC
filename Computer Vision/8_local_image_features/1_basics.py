import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.signal import convolve2d

# -----------------------------------------------------------
# A. CORRELATION, AUTO-CORRELATION, AND SSD
# -----------------------------------------------------------

def cross_correlation(f, h):
    """
    Cross-correlation: how similar is template h to image f at each position?
    (f ⊗ h)(i,j) = Σ_kl  f(k,l) * h(i+k, j+l)
    
    In practice, cross-correlation = convolution with h flipped 180°.
    scipy / OpenCV implement this directly.
    """
    # Flip h to convert correlation to convolution
    h_flipped = h[::-1, ::-1]
    return convolve2d(f, h_flipped, mode='same', boundary='symm')


def auto_correlation(f, window_size=5):
    """
    Auto-correlation: compares patch to a shifted version of itself.
    (f ⊗ f)(i,j) = Σ_kl  f(k,l) * f(i+k, j+l)
    
    Returns the auto-correlation at each pixel location.
    """
    f_flipped = f[::-1, ::-1]
    return convolve2d(f, f_flipped, mode='same', boundary='symm')


def ssd(patch1, patch2):
    """
    Sum of Squared Differences between two patches.
    SSD = Σ (f(k,l) - h(i+k, j+l))²
    Returns 0 for identical patches; larger = more different.
    """
    return np.sum((patch1.astype(np.float32) - patch2.astype(np.float32))**2)


def template_matching_ssd(image, template):
    """
    Slide template over image, compute SSD at each position.
    Minimum SSD = best match location.
    """
    h, w = template.shape
    H, W = image.shape
    result = np.zeros((H - h + 1, W - w + 1))

    for i in range(H - h + 1):
        for j in range(W - w + 1):
            patch = image[i:i+h, j:j+w]
            result[i, j] = ssd(patch, template)

    # Best match at minimum SSD
    best_loc = np.unravel_index(result.argmin(), result.shape)
    return result, best_loc

# -----------------------------------------------------------
# B. HARRIS ERROR FUNCTION E(u,v) AND STRUCTURE MATRIX M
# -----------------------------------------------------------

def compute_structure_matrix(img, sigma_grad=1.0, sigma_window=1.5):
    """
    Compute the Harris Structure Matrix M at every pixel.
    
    M = Σ w(x,y) * [[Ix², IxIy], [IxIy, Iy²]]
      = [[Σ w*Ix²,   Σ w*IxIy],
         [Σ w*IxIy,  Σ w*Iy² ]]
    
    Parameters:
        img          : float grayscale image [0,1]
        sigma_grad   : σ for gradient computation (image smoothing before derivatives)
        sigma_window : σ for the Gaussian window function w(x,y)
    Returns:
        M11, M12, M22 : the three unique entries of M at each pixel
        Ix, Iy        : gradient images
    """
    # Step 1: Smooth the image slightly before computing gradients
    img_smooth = gaussian_filter(img, sigma=sigma_grad)

    # Step 2: Compute image gradients Ix and Iy using Sobel kernels
    Kx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)
    Ky = Kx.T   # Sobel in y = transposed Sobel in x

    Ix = convolve2d(img_smooth, Kx, mode='same', boundary='symm')
    Iy = convolve2d(img_smooth, Ky, mode='same', boundary='symm')

    # Step 3: Compute the three entries of M (gradient products)
    Ix2  = Ix * Ix   # Ix²  → M[0,0]
    Iy2  = Iy * Iy   # Iy²  → M[1,1]
    IxIy = Ix * Iy   # IxIy → M[0,1] = M[1,0]

    # Step 4: Apply Gaussian window w(x,y) to each entry
    #         This computes Σ w(x,y)*Ix² etc. over the neighbourhood
    M11 = gaussian_filter(Ix2,  sigma=sigma_window)  # Σ w·Ix²
    M22 = gaussian_filter(Iy2,  sigma=sigma_window)  # Σ w·Iy²
    M12 = gaussian_filter(IxIy, sigma=sigma_window)  # Σ w·IxIy

    return M11, M12, M22, Ix, Iy


def harris_response(M11, M12, M22, k=0.05):
    """
    Compute the Harris corner response R at every pixel.
    
    R = det(M) - k * trace(M)²
      = (M11*M22 - M12²) - k*(M11 + M22)²
      = λ₁λ₂ - k(λ₁+λ₂)²
    
    R > 0   (large) → CORNER
    R < 0   (large magnitude) → EDGE
    |R| ≈ 0         → FLAT REGION
    
    k is empirically chosen in range [0.04, 0.06].
    """
    det_M   = M11 * M22 - M12**2     # det(M) = λ₁λ₂
    trace_M = M11 + M22               # trace(M) = λ₁+λ₂
    R       = det_M - k * trace_M**2  # Harris score
    return R
