import numpy as np
import matplotlib.pyplot as plt

# Create clean signal
true_signal = np.ones(100) * 90

# Add noise
noise = np.random.normal(0, 10, 100)
# 0 is the mean of normal distribution
# 10 is the standard deviation (width) of normal distribution
# 100 is the number of random values to be generated
print(f"noise: {noise}")

noisy_signal = true_signal + noise

# -----------------------------
# Simple Moving Average (NO WEIGHTS)
# -----------------------------
window_size = 5

# Kernel is a recipe of weights — it defines how much each neighbour contributes.
# np.ones(5) gives [1, 1, 1, 1, 1], dividing by 5 gives [0.2, 0.2, 0.2, 0.2, 0.2]
# All weights are equal (0.2 = 20%), so every neighbour matters the same amount.
# This is identical to taking a plain average of 5 values: (a+b+c+d+e) / 5
kernel = np.ones(window_size) / window_size

# Slide the kernel across the noisy signal.
# At each position: multiply 5 neighbours by their weights and sum them up.
# mode='same' keeps output the same length as the input (100 values in, 100 out)
smoothed_signal = np.convolve(
    noisy_signal,
    kernel,
    mode='same'
)

# Plot
plt.plot(true_signal, label="True Signal")
plt.plot(noisy_signal, label="Noisy Signal")
plt.plot(smoothed_signal, label="Smoothed (Average)")
plt.legend()
plt.title("Simple Moving Average Denoising")
plt.show()