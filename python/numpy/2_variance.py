import numpy as np
from scipy import stats as st
import pandas as pd

data = np.array([5, 7, 8, 9, 10, 100])
print(f"Data: {data}")
print()

# ── Geometric & Harmonic Mean (original data) ──────────────────────────────
gmean = st.gmean(data)
hmean = st.hmean(data)
print(f"Geometric Mean (original): {gmean:.4f}")
print(f"Harmonic Mean  (original): {hmean:.4f}")
print()

# ── Core statistics ────────────────────────────────────────────────────────
df = pd.Series(data)

median      = df.median()
mean_numpy  = np.mean(df)
mean_pandas = df.mean()

print(f"Mean (numpy) : {mean_numpy:.4f}")
print(f"Mean (pandas): {mean_pandas:.4f}")
print(f"Geometric Mean (pandas series): {st.gmean(df):.4f}")
print(f"Harmonic Mean  (pandas series): {st.hmean(df):.4f}")
print()

# ── Quartiles ──────────────────────────────────────────────────────────────
q1 = df.quantile(0.25, interpolation='midpoint')
q2 = df.quantile(0.50, interpolation='midpoint')
q3 = df.quantile(0.75, interpolation='midpoint')

print(f"  Q1 (25th percentile): {q1}")
print(f"  Q2 (50th percentile): {q2}  |  Median: {median}")
print(f"  Q3 (75th percentile): {q3}")
print()

# ── IQR & Outlier Bounds ───────────────────────────────────────────────────
iqr         = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f"Inter-Quartile Range (IQR): {iqr}")
print(f"Lower Bound: {lower_bound}  |  Upper Bound: {upper_bound}")
print()

# ── Outliers ───────────────────────────────────────────────────────────────
outliers = df[(df < lower_bound) | (df > upper_bound)]
print(f"Outliers: {outliers.values if len(outliers) > 0 else 'None'}")
print()

# ── Variance & STD (original dirty data) ──────────────────────────────────
var_original = df.var()                        # pandas  → sample variance (ddof=1)
std_numpy    = np.std(df, ddof=1)             # numpy   → sample std     (ddof=1)
std_pandas   = df.std()                        # pandas  → sample std     (ddof=1)
# scipy does not have a standalone std, but we can use describe
desc         = st.describe(df)                  # scipy describe gives variance (ddof=1)
std_scipy    = np.sqrt(desc.variance)          # derive std from scipy variance

print("── Original Data Statistics ──────────────────────────────────────────────")
print(f"  Variance (pandas, ddof=1) : {var_original:.4f}")
print(f"  STD      (numpy,  ddof=1) : {std_numpy:.4f}")
print(f"  STD      (pandas, ddof=1) : {std_pandas:.4f}")
print(f"  STD      (scipy derived)  : {std_scipy:.4f}")
print()

# ══════════════════════════════════════════════════════════════════════════
# METHOD 1 — Remove Outliers
# ══════════════════════════════════════════════════════════════════════════
cleaned_removed = df[(df >= lower_bound) & (df <= upper_bound)].copy()
print(f"Cleaned Data (outliers removed): {cleaned_removed.values}")

mean_r    = cleaned_removed.mean()
median_r  = cleaned_removed.median()
gmean_r   = st.gmean(cleaned_removed)
hmean_r   = st.hmean(cleaned_removed)
var_r     = cleaned_removed.var()                      # pandas, ddof=1
std_r_np  = np.std(cleaned_removed, ddof=1)           # numpy
std_r_pd  = cleaned_removed.std()                      # pandas
std_r_sc  = np.sqrt(st.describe(cleaned_removed).variance)  # scipy

print("── After Removing Outliers ───────────────────────────────────────────────")
print(f"  Mean           : {mean_r:.4f}")
print(f"  Median         : {median_r:.4f}")
print(f"  Geometric Mean : {gmean_r:.4f}")
print(f"  Harmonic Mean  : {hmean_r:.4f}")
print(f"  Variance       : {var_r:.4f}")
print(f"  STD (numpy)    : {std_r_np:.4f}")
print(f"  STD (pandas)   : {std_r_pd:.4f}")
print(f"  STD (scipy)    : {std_r_sc:.4f}")
print()

# ══════════════════════════════════════════════════════════════════════════
# METHOD 2 — Replace Outliers with Upper Bound (Winsorization)
# ══════════════════════════════════════════════════════════════════════════
# Convert to float FIRST so pandas can assign 12.5 (a float) into the series
cleaned_replaced = df.astype(float).copy()
cleaned_replaced.loc[cleaned_replaced > upper_bound] = upper_bound   # cap high
cleaned_replaced.loc[cleaned_replaced < lower_bound] = lower_bound   # cap low

print(f"Cleaned Data (outliers replaced): {cleaned_replaced.values}")

mean_rp    = cleaned_replaced.mean()
median_rp  = cleaned_replaced.median()
gmean_rp   = st.gmean(cleaned_replaced)
hmean_rp   = st.hmean(cleaned_replaced)
var_rp     = cleaned_replaced.var()
std_rp_np  = np.std(cleaned_replaced, ddof=1)
std_rp_pd  = cleaned_replaced.std()
std_rp_sc  = np.sqrt(st.describe(cleaned_replaced).variance)

print("── After Replacing Outliers ──────────────────────────────────────────────")
print(f"  Mean           : {mean_rp:.4f}")
print(f"  Median         : {median_rp:.4f}")
print(f"  Geometric Mean : {gmean_rp:.4f}")
print(f"  Harmonic Mean  : {hmean_rp:.4f}")
print(f"  Variance       : {var_rp:.4f}")
print(f"  STD (numpy)    : {std_rp_np:.4f}")
print(f"  STD (pandas)   : {std_rp_pd:.4f}")
print(f"  STD (scipy)    : {std_rp_sc:.4f}")