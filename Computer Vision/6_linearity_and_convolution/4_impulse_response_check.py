import numpy as np
from scipy import signal

F = np.zeros((7, 7)); F[3, 3] = 1.0     # single impulse, dead centre
H = np.arange(1, 10).reshape(3, 3)       # 1..9 standing in for a..i

G_correlation = signal.correlate2d(F,H,mode="same")
G_convolution = signal.convolve2d(F,H,mode="same")
print("F:\n", F)
print("H:\n", H)
print("G_correlation:\n", G_correlation)
print("G_convolution:\n", G_convolution)
print("correlation around the impulse (flipped):\n", G_correlation[2:5, 2:5])
print("convolution around the impulse (unflipped):\n", G_convolution[2:5, 2:5])