import numpy as np
from skimage import data

image = data.camera()

# (A) changes the CONTAINER only — values are still 0-255
as_float = image.astype(np.float32)

# (B) changes the VALUE RANGE — now scaled to 0.0-1.0
normalized = image / 255.0

# interpretation
# .astype() alone just relabels the numbers as floats — 255 stays 255.0, still "bright white" on a 0-255 scale. Dividing by 255 actually rescales every value into the 0–1 range that most ML models expect.

# common mistake
# Calling .astype(np.float32) and assuming the image is now "normalized" for a neural network. It isn't — the values are still 0–255, just in a different container. This one mix-up quietly wrecks model training more often than almost any other preprocessing bug.
