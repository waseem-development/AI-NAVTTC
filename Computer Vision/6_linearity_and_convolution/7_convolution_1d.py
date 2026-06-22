import numpy as np

# Input signal (time series)
f_1d = np.array([1, 2, 3, 4, 5])

# Kernel / filter
h_1d = np.array([1, 1, 1])

# True convolution (kernel is flipped internally)
G_1d = np.convolve(f_1d, h_1d, mode='same')

print("Input signal:", f_1d)
print("Kernel:", h_1d)
print("Output:", G_1d)