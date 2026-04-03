# 📊 The Ultimate Averages Guide

### *Mean · Median · Mode · Geometric · Harmonic*

> **For future Hafiz** — when you forget which average to use at 2am 🌙

---

## 🧠 Why So Many Averages?

Think of averages like  **knives in a kitchen** .

You wouldn't use a bread knife to fillet a fish. Same deal here — each average is built for a specific job. Use the wrong one → wrong answer → bad decisions.

```
Wrong average  =  Wrong answer  =  Bad decisions  =  😬
Right average  =  Right answer  =  Good decisions  =  ✅
```

---

---

# PART 1 — The Three Musketeers

### *Mean, Median, Mode — your everyday tools (90% of the time)*

---

## 1️⃣ MEAN — The "Fair Share" Average

> *"Add everything up, split it equally."*

### 🍕 The Analogy

You and 4 friends order pizzas. Total slices = 24.
**Mean = 24 ÷ 5 = 4.8 slices per person.**
Everyone gets the same share — in a perfect world.

### ✅ Use it when...

* Data has **no extreme values** (no crazy outliers)
* Numbers form a **bell curve** (balanced on both sides)
* You want the **mathematical center**

### ❌ Never use it when...

* One billionaire is in a room full of poor people
* Data is **skewed** (most earn $40k, one earns $10M)

### 🌍 Real-World Uses

| Situation                   | Why Mean Works                   |
| --------------------------- | -------------------------------- |
| Avg temperature in a city   | Hot & cold days balance out      |
| Avg test score in class     | No extreme outliers expected     |
| Avg height of students      | Heights are normally distributed |
| Avg time to complete a task | Fairly consistent timings        |

### 🐍 Python Code

```python
import numpy as np
import pandas as pd

coffee_spent = [3.50, 4.00, 3.75, 4.50, 3.25]

mean = np.mean(coffee_spent)
print(f"Mean coffee spend: ${mean:.2f}")
# Output: $3.80
```

---

## 2️⃣ MEDIAN — The "Middle Child" Average

> *"Line everyone up, pick the person in the middle."*

### 🏠 The Analogy

Houses on a street cost: `$200k, $220k, $240k, $250k, $5,000,000`

| Average          | Result     | Realistic?                |
| ---------------- | ---------- | ------------------------- |
| **Mean**   | $1,182,000 | ❌ Mansion destroyed it   |
| **Median** | $240,000   | ✅ The real typical price |

The mansion is an **outlier** — median simply ignores it.

### ✅ Use it when...

* Data has **outliers** (super high or super low values)
* Data is **skewed** (most earn low, a few earn insane)
* You want the **"typical" value** most people relate to

### 🌍 Real-World Uses

| Situation                | Why Median Works                |
| ------------------------ | ------------------------------- |
| House prices             | Mansions don't ruin the picture |
| Salaries                 | CEO's $10M doesn't skew it      |
| Website response time    | One slow request stays harmless |
| Age in a retirement home | Young visitors are outliers     |

### 🐍 Python Code

```python
prices = [350, 380, 340, 1200, 360, 390, 2500]  # in $1000s

print(f"Mean:   ${np.mean(prices):.0f}k")    # $789k — penthouse ruined it
print(f"Median: ${np.median(prices):.0f}k")  # $380k — the real story ✅
```

---

## 3️⃣ MODE — The "Popular Kid" Average

> *"Who shows up the most? That's the mode."*

### 👟 The Analogy

You survey 100 people on shoe size:

* Size 9 → 30 people
* Size 10 → 25 people
* Size 8 → 20 people

**Mode = Size 9** — it's the most common, so stock your store with 9s.

### ✅ Use it when...

* Data is **categories** (colors, brands, Yes/No)
* Numbers **repeat** (kids per family: 1, 2, 2, 2, 3)
* You want to know **"what's most popular?"**

### 🌍 Real-World Uses

| Situation                       | Why Mode Works           |
| ------------------------------- | ------------------------ |
| Most sold product in a store    | You want the top seller  |
| Most frequent server error code | Find what breaks most    |
| Most popular travel destination | Count of votes, not math |
| Common payment method           | Cash vs card vs PayPal   |

### 🐍 Python Code

```python
# Categorical data
colors = ['red', 'blue', 'red', 'green', 'red', 'blue', 'red']
print(pd.Series(colors).mode()[0])   # 'red' ✅

# Numeric data
kids = [2, 1, 3, 2, 2, 4, 2, 1, 2, 3]
print(pd.Series(kids).mode()[0])     # 2 ✅

# Multiple modes (bimodal)
scores = [85, 85, 90, 90, 95]
print(pd.Series(scores).mode().tolist())  # [85, 90] ✅
```

---

---

# PART 2 — The Special Forces

### *Geometric & Harmonic — rare but incredibly powerful*

---

## 4️⃣ GEOMETRIC MEAN — The "Growth Champion"

> *"Multiply instead of adding. Built for growth."*

### 🌱 The Analogy

Your investment:  **Year 1 → +100%** , **Year 2 → -50%**

| Average                   | Says             | Reality Check                                        |
| ------------------------- | ---------------- | ---------------------------------------------------- |
| **Arithmetic mean** | +25% per year 🎉 | ❌ Wrong — you didn't gain anything!                |
| **Geometric mean**  | 0% growth 😐     | ✅ Correct — you started with $100, ended with $100 |

**$100 × 2.0 × 0.5 = $100** — you're back to zero. Arithmetic lied to you.

### ✅ Use it when...

* Measuring **investment returns** over multiple years
* Calculating **population or bacteria growth**
* Working with **percentages that compound**
* Averaging **ratios** (P/E ratios, speedup factors)

### 📏 Golden Rule

```
Geometric Mean  ≤  Arithmetic Mean  (always smaller or equal)
```

### 🌍 Real-World Uses

| Situation                      | Why Geometric Works             |
| ------------------------------ | ------------------------------- |
| Stock portfolio CAGR           | Returns compound year-over-year |
| City/country population growth | Each year builds on last        |
| Inflation over 10 years        | Multiplicative, not additive    |
| Performance benchmark speedups | Ratios need geometric           |

### 🐍 Python Code

```python
from scipy.stats import gmean

# Investment: +50%, +100%, -50%
returns = [1.5, 2.0, 0.5]

print(f"Arithmetic: {np.mean(returns):.2f}x")  # 1.33x — misleading ❌
print(f"Geometric:  {gmean(returns):.2f}x")    # 1.14x — TRUE growth ✅

# Proof: $100 × 1.5 × 2.0 × 0.5 = $150 → 14% annual growth ✓

# Bacteria growth per day: 2x, 3x, 1.5x
growth = [2, 3, 1.5]
print(f"Avg daily growth: {gmean(growth):.2f}x")  # 2.08x
```

---

## 5️⃣ HARMONIC MEAN — The "Rate Master"

> *"When you're averaging speeds, prices per unit, or rates — this is your tool."*

### 🚗 The Analogy

You drive to work and back. **Same road (10 miles each way).**

* Going: **30 mph**
* Coming back: **60 mph**

| Average                   | Says   | Reality Check                                      |
| ------------------------- | ------ | -------------------------------------------------- |
| **Arithmetic mean** | 45 mph | ❌ Wrong — you spent more time going slow         |
| **Harmonic mean**   | 40 mph | ✅ Correct — total 20 miles in 0.5 hours = 40 mph |

**Proof:** 10/30 + 10/60 = 0.333 + 0.167 = 0.5 hrs → 20 miles ÷ 0.5 hrs = **40 mph** ✓

### ✅ Use it when...

* Averaging **speeds** (same distance, different speeds)
* **Dollar-cost averaging** in stocks (same $ invested, different prices)
* **Fuel efficiency** across multiple trips
* Any time you have **rates** with equal quantities

### 📏 Golden Rule

```
Harmonic Mean  ≤  Geometric Mean  ≤  Arithmetic Mean
(Harmonic is always the smallest of the three)
```

### 🌍 Real-World Uses

| Situation                   | Why Harmonic Works                |
| --------------------------- | --------------------------------- |
| Avg speed of delivery fleet | Same routes, different speeds     |
| Stock dollar-cost averaging | Same $ invested each month        |
| CPU parallel processing     | Equal workloads, different speeds |
| Avg P/E ratio in portfolio  | Rate-based financial metric       |

### 🐍 Python Code

```python
from scipy.stats import hmean

# Speed problem
speeds = [30, 60]
print(f"Wrong (arithmetic): {np.mean(speeds)} mph")  # 45 ❌
print(f"Right (harmonic):   {hmean(speeds):.1f} mph") # 40 ✅

# Dollar-cost averaging stocks
# Invest $1000/month at prices: $10, $20, $5
prices = [10, 20, 5]
print(f"True avg price paid: ${hmean(prices):.2f}")
# Total: 100 + 50 + 200 = 350 shares, $3000 spent
# Real avg = $3000/350 = $8.57 ✓
```

---

---

# 🎯 THE MASTER CHEAT SHEET

| Your Question                     | Use This                 | One-Line Rule       |
| --------------------------------- | ------------------------ | ------------------- |
| What's typical?*(no outliers)*  | **Mean**           | Add and divide      |
| What's typical?*(has outliers)* | **Median**         | Find the middle     |
| What's most common?               | **Mode**           | Count the repeats   |
| What's the avg growth rate?       | **Geometric Mean** | Multiply, then root |
| What's the avg speed/rate?        | **Harmonic Mean**  | Reciprocal magic    |

---

# 🌳 DECISION TREE — Which Average Do I Use?

```
START
  │
  ▼
Is your data CATEGORIES? (colors, brands, yes/no)
  ├── YES ──► 🟣 MODE
  └── NO
        │
        ▼
      Are you averaging RATES? (speed, price per unit)
        ├── YES ──► 🔴 HARMONIC MEAN
        └── NO
              │
              ▼
            Are you measuring GROWTH over time? (%, returns)
              ├── YES ──► 🟢 GEOMETRIC MEAN
              └── NO
                    │
                    ▼
                  Does data have EXTREME OUTLIERS?
                    ├── YES ──► 🔵 MEDIAN
                    └── NO ───► 🟠 MEAN
```

---

# 💣 COMMON MISTAKES — Don't Be This Person

### ❌ Mistake 1 — Using Mean for Salaries

```python
salaries = [45000, 48000, 52000, 50000, 2_000_000]  # CEO in the room

print(f"Mean:   ${np.mean(salaries):,.0f}")    # $439,000 — nobody earns this!
print(f"Median: ${np.median(salaries):,.0f}")  # $50,000  — the real story ✅
```

### ❌ Mistake 2 — Using Mean for Investment Returns

```python
# +100% one year, -50% the next
returns_percent = [100, -50]

print(np.mean(returns_percent))      # 25%  — you think you're rich ❌
print(gmean([2.0, 0.5]) - 1)        # 0.0  — you broke even ✅
```

### ❌ Mistake 3 — Using Mean for Speed

```python
speeds = [30, 60]

print(f"Mean:    {np.mean(speeds)} mph")   # 45 — WRONG ❌
print(f"Harmonic:{hmean(speeds):.0f} mph") # 40 — RIGHT ✅
```

---

# 📦 FULL COPY-PASTE EXAMPLE

```python
import pandas as pd
import numpy as np
from scipy.stats import gmean, hmean

data = {
    'price':        [350000, 380000, 340000, 1200000, 360000, 390000, 2500000],
    'sqft':         [800,    850,    780,    2500,    820,    880,    3000],
    'neighborhood': ['downtown','downtown','downtown','luxury','downtown','downtown','luxury'],
    'price_growth': [1.05, 1.03, 1.06, 0.95, 1.04, 1.05, 0.98]
}
df = pd.DataFrame(data)
df['price_per_sqft'] = df['price'] / df['sqft']

print("── Price Analysis ──────────────────────")
print(f"  Mean:   ${df['price'].mean():>12,.0f}  ← skewed by penthouses")
print(f"  Median: ${df['price'].median():>12,.0f}  ← the real typical price ✅")

print("\n── Most Common Neighborhood ────────────")
print(f"  Mode: {df['neighborhood'].mode()[0]} ✅")

print("\n── Investment Growth ───────────────────")
avg_growth = gmean(df['price_growth'])
print(f"  Geometric avg growth: {(avg_growth-1)*100:.1f}% per year ✅")

print("\n── Price per Sqft (Rate) ───────────────")
print(f"  Harmonic mean: ${hmean(df['price_per_sqft']):.0f}/sqft ✅")
```

---

# 🧠 MEMORY TRICKS

```
MEAN     →  M for Math       → Sensitive to outliers
MEDIAN   →  M for Middle     → Immune to outliers
MODE     →  M for Most       → For categories & counts
GEOMETRIC → G for Growth     → Investments, percentages
HARMONIC  → H for How fast?  → Speed, rates, ratios
```

---

# 📚 BUSINESS EXAMPLES — Right vs Wrong

| Business Problem                   | ❌ Wrong | ✅ Right  | Why                          |
| ---------------------------------- | -------- | --------- | ---------------------------- |
| Customer satisfaction (1–5 stars) | Mean     | Median    | One 1-star won't kill median |
| Sales growth over 5 years          | Mean     | Geometric | Growth compounds             |
| Website response time              | Mean     | Median    | One slow req ruins mean      |
| Most common error type             | Mean     | Mode      | You want frequency           |
| Delivery fleet avg speed           | Mean     | Harmonic  | Same routes, diff speeds     |
| Typical customer age               | Median   | Mean      | Fine if no extreme ages      |

---

# 🎓 PRO TIPS

> **1. Visualize first** — a histogram instantly tells you if data is skewed

> **2. Report both** — show Mean AND Median together, let stakeholders judge

> **3. Check outliers** — use IQR or Z-scores before trusting the mean

> **4. Know your domain** — finance = geometric, real estate = median, retail = mode

> **5. Document why** — in code comments, always explain which average you picked and why

---

```
┌─────────────────────────────────────────────────────┐
│  If someone asks for "the average" —                │
│  always ask: "Which one?" 🤔                        │
│  Your analysis depends on the answer.               │
└─────────────────────────────────────────────────────┘
```

---

*Made for future Hafiz · Save this, you'll need it · Happy analyzing 🚀*
