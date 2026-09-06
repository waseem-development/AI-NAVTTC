import numpy as np
from skimage import data

image = data.camera()
# These five numbers are the fastest possible health-check for any image — before you even look at it, you already know its size, its numeric type, and its rough brightness range.

print(f"image.shape: {image.shape}")
print(f"image.dtype: {image.dtype}")
print(f"image.min(): {image.min()}")
print(f"image.max(): {image.max()}")
print(f"image.mean(): {image.mean()}")

# Run this on every image (or a sample) when you first receive a dataset — it instantly flags images that are pure black, pure white, or oddly narrow-range.

