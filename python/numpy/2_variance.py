import numpy as np
from scipy import stats
import pandas as pd

data = np.array([5, 7, 8, 9, 10, 100])
print(f"Data: {data}")
print()

df = pd.Series(data)
df.sort_values()
print(f"Sorted Data: {data}")
print()

median = df.median()
mean_numpy = np.mean(df)
mean_pandas = df.mean()

print(f"mean with numpy: {mean_numpy}")
print(f"mean with pandas: {mean_pandas}")
print()

q1 = df.quantile(0.25, interpolation='midpoint')
q2 = df.quantile(0.50, interpolation='midpoint')
q3 = df.quantile(0.75, interpolation='midpoint')

print(f"  Q1 (25th percentile): {q1}")
print(f"  Q2 (50th percentile): {q2} / median: {median}")
print(f"  Q3 (75th percentile): {q3}")
print()

iqr = q3 - q1
print(f"Inter-quantile range: {iqr}")
print()

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print(f"Lower-bound: {lower_bound} | Upper-bound: {upper_bound}")

outliers = df[(df < lower_bound) | (df > upper_bound)]
print(f"Outliers {outliers.values if len(outliers > 0) else 'None'}")
print()
var = df.var()
print(f"Variance: {var}")
print()

cleaned_data_from_outliers = df[(df >= lower_bound) & (df <= upper_bound)]
print(f"Cleaned Data: {cleaned_data_from_outliers.values}")
print()

cleaned_data_from_outliers.sort_values()
mean_clean = cleaned_data_from_outliers.mean()
median_clean = cleaned_data_from_outliers.median()
var_clean = cleaned_data_from_outliers.var()
print(f"Mean of cleaned data: {mean_clean}")
print(f"Median of cleaned data: {median_clean}")
print(f"Variance of cleaned data: {var_clean}")
print()

# Make a copy and convert to float to allow replacing with float
cleaned_data_with_replacing_outliers = df.astype(float).copy()

# Replace outliers
cleaned_data_with_replacing_outliers.loc[cleaned_data_with_replacing_outliers > upper_bound] = upper_bound

print(f"Cleaned Data by replacing Outliers: {cleaned_data_with_replacing_outliers.values}")
print()

# Optional: recompute statistics
mean_replaced = cleaned_data_with_replacing_outliers.mean()
median_replaced = cleaned_data_with_replacing_outliers.median()
var_replaced = cleaned_data_with_replacing_outliers.var()

print(f"Mean after replacing outlier: {mean_replaced}")
print(f"Median after replacing outlier: {median_replaced}")
print(f"Variance after replacing outlier: {var_replaced}")
print()