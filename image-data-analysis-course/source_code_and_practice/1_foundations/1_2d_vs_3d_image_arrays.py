import numpy as np
from skimage import data

# data is a module inside skimage that provides built-in sample images. 
# data.camera()
# data.astronaut()
# data.coins()
# data.chelsea()

gray = data.camera()                 # a built-in grayscale sample image of a cameraman
rgb  = data.astronaut()              # a built-in color sample image of an astronaut

print(gray.shape)
print(rgb.shape)