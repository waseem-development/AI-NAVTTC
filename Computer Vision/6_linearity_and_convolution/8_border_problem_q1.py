from scipy import signal
import numpy as np

f = np.zeros((80, 80))        # 80x80 image patch
h = np.ones((9, 9)) / 81       # 9x9 box kernel

print("mode=\"full\":", signal.convolve2d(f, h, mode="full").shape)
print("mode=\"same\":", signal.convolve2d(f, h, mode="same").shape)
print("mode=\"valid\":", signal.convolve2d(f, h, mode="valid").shape)