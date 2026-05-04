import numpy as np
from scipy import stats
my_data = np.array([2.25, 0.25, 0.25, 2.25])
mean = np.mean(my_data)
median = np.median(my_data)
mode = stats.mode(my_data).mode
print(f"mean: {mean}")
print(f"median: {median}")
print(f"mode: {mode}")


print("My data =", my_data, mean, median, mode)
print(f"My data = {my_data} {mean}, {median} {mode}")
