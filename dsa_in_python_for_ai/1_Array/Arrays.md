# 🧮 Arrays — The Foundation of Everything

> *"An array is the simplest, most powerful data structure in existence. Every other structure is built on top of it."*

---

## 🧠 What Is an Array?

An **array** is a collection of elements stored in  **contiguous (side-by-side) memory locations** , all of the  **same data type** , accessible via an  **index** .

```
Index:    0      1      2      3      4
       ┌──────┬──────┬──────┬──────┬──────┐
       │  10  │  20  │  30  │  40  │  50  │
       └──────┴──────┴──────┴──────┴──────┘
       ↑
    Base address (e.g., memory address 1000)
    arr[0] = address 1000
    arr[1] = address 1004  (each int = 4 bytes)
    arr[i] = base + i × element_size  → O(1) access!
```

**Why O(1) access?** Because the computer uses math, not searching. It doesn't loop — it directly computes the address.

---

## 🏗️ Types of Arrays

There are **3 main types** you'll work with in Python:

---

## 1️⃣ Python `array` Module (Typed Array)

Python's built-in `array` module gives you a **typed, memory-efficient** array — unlike Python's flexible `list`, every element must be the  **same type** .

```python
from array import array

# Create: array(typecode, initializer)
myArray = array("i", [1, 2, 3, 4, 5])
#                ↑
#            typecode: "i" = signed integer
```

### Typecodes (Data Types)

| Typecode | C Type        | Python Type | Size     |
| -------- | ------------- | ----------- | -------- |
| `'b'`  | signed char   | int         | 1 byte   |
| `'B'`  | unsigned char | int         | 1 byte   |
| `'i'`  | signed int    | int         | 2+ bytes |
| `'I'`  | unsigned int  | int         | 2+ bytes |
| `'l'`  | signed long   | int         | 4+ bytes |
| `'f'`  | float         | float       | 4 bytes  |
| `'d'`  | double        | float       | 8 bytes  |

### Core Operations

```python
from array import array

myArray = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# ── Access ──────────────────────────────────
print(myArray[0])    # 1    → O(1)
print(myArray[4])    # 5    → O(1)
print(myArray[-1])   # 10   → O(1) last element

# ── Append (add to end) ──────────────────────
myArray.append(11)   # [1,2,...,10,11]  → O(1)
myArray.append(12)
myArray.append(13)

# ── Insert (at specific index) ───────────────
myArray.insert(0, 0)          # insert 0 at index 0 → O(n) shifts
myArray.insert(len(myArray), 14)  # insert at end    → O(1)

# ── Remove ───────────────────────────────────
myArray.pop(3)       # remove by INDEX 3           → O(n) shifts
myArray.remove(5)    # remove by VALUE 5 (first)   → O(n) search + shift

# ── Metadata ─────────────────────────────────
print(myArray.typecode)   # 'i'
print(myArray.itemsize)   # 4 (bytes per element)

# ── Convert ──────────────────────────────────
as_list = myArray.tolist()   # convert to Python list

# ── Extend (combine arrays) ──────────────────
arr1 = array("i", [1, 2, 3, 4, 5])
arr2 = array("i", [6, 7, 8, 9, 10])
arr1.extend(arr2)    # arr1 is now [1,2,3,4,5,6,7,8,9,10]

# ── Copy ─────────────────────────────────────
copyArray = array(myArray.typecode, (val for val in myArray))  # generator copy
```

### Slicing

```python
myArray = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Syntax: array[start:stop:step]
sliced       = myArray[0:5]      # [1, 2, 3, 4, 5]     → indices 0 to 4
with_steps   = myArray[0:5:2]    # [1, 3, 5]            → every 2nd element
reversed_arr = myArray[::-1]     # [10,9,8,7,6,5,4,3,2,1] → reversed
every_other  = myArray[::2]      # [1, 3, 5, 7, 9]      → all odd indices
last_three   = myArray[-3:]      # [8, 9, 10]            → last 3
```

### Custom Print (Like a Set)

```python
print("{", end="")
for i in range(len(myArray)):
    if i == len(myArray) - 1:
        print(f"{myArray[i]}", end="")
    else:
        print(f"{myArray[i]}", end=", ")
print("}")
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

### Time & Space Complexity

| Operation         | Time                        | Space |
| ----------------- | --------------------------- | ----- |
| Access `arr[i]` | O(1)                        | O(1)  |
| Append at end     | O(1) amortized              | O(1)  |
| Insert at index i | O(n)                        | O(1)  |
| Remove by index   | O(n)                        | O(1)  |
| Search by value   | O(n)                        | O(1)  |
| Slicing `[i:j]` | O(k) where k = slice size   | O(k)  |
| Extend            | O(m) where m = new elements | O(m)  |

### 🏭 Python `array` — Production Use & Companies

**Scientific Computing Buffers**
When memory efficiency matters (embedded systems, microcontrollers), typed arrays use far less memory than Python lists since each element has a fixed byte size.

| Company                           | How They Use It                                               |
| --------------------------------- | ------------------------------------------------------------- |
| **NASA / JPL**              | Embedded Python on spacecraft — typed arrays for sensor data |
| **Raspberry Pi Foundation** | GPIO pin data buffers — typed array of bytes                 |
| **Arduino-Python bridges**  | Serial data from sensors —`array('B')`for byte streams     |

**Audio Processing**
Raw audio is a stream of integer samples. The `array` module stores these efficiently before passing to hardware.

| Company                          | How They Use It                                                     |
| -------------------------------- | ------------------------------------------------------------------- |
| **PyAudio**                | Audio input/output buffers —`array('h')`for 16-bit audio samples |
| **SoundCloud**             | Audio processing pipeline — typed arrays for waveform data         |
| **Audacity (open source)** | Audio sample storage — typed integer arrays                        |

---

## 2️⃣ NumPy Arrays — The ML Workhorse

**NumPy** (`numpy`) is the backbone of all scientific computing and ML in Python. NumPy arrays are:

* Stored in **contiguous C memory** (much faster than Python lists)
* **Homogeneous** — all elements same type
* **Multi-dimensional** — 1D, 2D, 3D, nD
* Vectorized — operations apply to **all elements at once** without loops

```python
import numpy as np
```

---

### 🔢 Creating NumPy Arrays

```python
import numpy as np

# ── From a list ───────────────────────────────
arr = np.array([1, 2, 3, 4, 5])              # 1D integer array
arr_float = np.array([1, 2, 3], float)       # force float type

# ── Special creators ──────────────────────────
zeros   = np.zeros(10)                        # [0. 0. 0. ... 0.]  (10 zeros)
ones    = np.ones(10)                         # [1. 1. 1. ... 1.]  (10 ones)
full    = np.full(50, 5)                      # [5 5 5 5 ... 5]   (50 fives)
eye     = np.eye(3)                           # 3×3 identity matrix

# ── Range-based ───────────────────────────────
arange  = np.arange(10, 20)                  # [10,11,12,...,19]  (20 excluded)
linspace = np.linspace(10, 20, 5)            # [10, 12.5, 15, 17.5, 20] (5 points, both inclusive)

print(arange)    # [10 11 12 13 14 15 16 17 18 19]
print(linspace)  # [10.  12.5 15.  17.5 20. ]
```

**`arange` vs `linspace`:**

```
np.arange(10, 20)       → steps by 1, stop is EXCLUSIVE: [10, 11, ..., 19]
np.linspace(10, 20, 5)  → gives exactly 5 evenly spaced points, stop INCLUSIVE: [10, 12.5, 15, 17.5, 20]
```

---

### 📐 Dimensions (The Most Important Concept)

```python
import numpy as np

# ── 0D: Scalar ────────────────────────────────
zero = np.array(10)
print(zero)          # 10
print(zero.ndim)     # 0
print(zero.shape)    # ()

# ── 1D: Vector ────────────────────────────────
one = np.array([10, 20, 30, 40, 50, 60])
print(one)           # [10 20 30 40 50 60]
print(one.ndim)      # 1
print(one.shape)     # (6,) — 6 elements

# ── 2D: Matrix (rows × columns) ──────────────
two = np.array([
    [10,  20,  30,  40,  50,  60],
    [110, 120, 130, 140, 150, 160]
])
print(two)
# [[ 10  20  30  40  50  60]
#  [110 120 130 140 150 160]]
print(two.ndim)      # 2
print(two.shape)     # (2, 6) — 2 rows, 6 columns

# ── 3D: Collection of 2D arrays ───────────────
three = np.array([
    [                                       # ← first 2D block
        [10,  20,  30,  40,  50,  60],
        [110, 120, 130, 140, 150, 160]
    ],
    [                                       # ← second 2D block
        [210, 220, 230, 240, 250, 260],
        [310, 320, 330, 340, 350, 360]
    ]
])
print(three.ndim)    # 3
print(three.shape)   # (2, 2, 6) — 2 blocks, 2 rows each, 6 cols each
```

**Visualizing Dimensions:**

```
0D: a single number          →  10
1D: a line of numbers        →  [1, 2, 3, 4, 5]
2D: a grid (table/matrix)    →  [[1, 2, 3],
                                  [4, 5, 6]]
3D: a stack of grids         →  [[[1,2,3],[4,5,6]],
                                  [[7,8,9],[10,11,12]]]
4D: sequence of 3D blocks    →  (think: video = frames × height × width × RGB)
```

---

### ⚡ NumPy Operations

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# ── Element-wise operations (NO LOOP NEEDED!) ─
print(a + b)      # [11 22 33 44 55]
print(a * b)      # [10 40 90 160 250]
print(a ** 2)     # [1  4  9  16  25]
print(b / a)      # [10.  10.  10.  10.  10.]

# ── Aggregation ───────────────────────────────
print(a.sum())    # 15
print(a.mean())   # 3.0
print(a.max())    # 5
print(a.min())    # 1
print(a.std())    # standard deviation

# ── Reshape ───────────────────────────────────
matrix = np.arange(1, 13).reshape(3, 4)   # 1D → 3×4 matrix
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# ── Boolean masking ───────────────────────────
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[arr > 4])    # [5 6 7 8] — filter without a loop!
print(arr[arr % 2 == 0])  # [2 4 6 8] — even numbers only

# ── Dot product / Matrix multiplication ───────
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))
# [[19 22]
#  [43 50]]
```

---

### 📊 NumPy Array Attributes

```python
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)

print(arr.ndim)     # 2      — number of dimensions
print(arr.shape)    # (2, 3) — rows × columns
print(arr.size)     # 6      — total number of elements
print(arr.dtype)    # float64 — data type of elements
print(arr.itemsize) # 8      — bytes per element
print(arr.nbytes)   # 48     — total bytes (6 × 8)
```

---

### Time & Space Complexity (NumPy)

| Operation                 | Time          | Space  | Notes                             |
| ------------------------- | ------------- | ------ | --------------------------------- |
| Access `arr[i]`         | O(1)          | O(1)   | Direct memory address             |
| Vectorized op `arr * 2` | O(n)          | O(n)   | But ~100x faster than Python loop |
| `np.dot(A, B)`          | O(n³) naïve | O(n²) | BLAS-optimized internally         |
| `reshape`               | O(1)          | O(1)   | Just changes view, no copy        |
| Slicing                   | O(1)          | O(1)   | Returns a view, not copy          |
| `arr.sum()`             | O(n)          | O(1)   | SIMD-vectorized in C              |
| Boolean mask              | O(n)          | O(k)   | k = matching elements             |
| `np.sort()`             | O(n log n)    | O(n)   | Introsort algorithm               |

---

### 🏭 NumPy — Production Use & Companies

**Machine Learning / Deep Learning**
Every ML framework (TensorFlow, PyTorch, scikit-learn) uses NumPy arrays as the fundamental data type. Model weights, gradients, activations — all NumPy or NumPy-compatible tensors.

| Company                | How They Use NumPy                                                                 |
| ---------------------- | ---------------------------------------------------------------------------------- |
| **Google**       | TensorFlow's `tf.Tensor`is NumPy-compatible; Google Brain research runs on NumPy |
| **Meta**         | PyTorch is built on NumPy-style arrays; all research at FAIR uses NumPy            |
| **OpenAI**       | GPT model training data preprocessing — NumPy arrays for tokenized text           |
| **Anthropic**    | Claude model research — NumPy arrays for embedding analysis                       |
| **Hugging Face** | Transformers library — all model inputs/outputs are NumPy arrays                  |

**Scientific Research**
NASA, CERN, pharmaceutical companies — all run simulations using NumPy.

| Company                    | How They Use NumPy                                                                  |
| -------------------------- | ----------------------------------------------------------------------------------- |
| **NASA**             | Telescope image processing — Hubble/James Webb images processed as NumPy 2D arrays |
| **CERN**             | Particle physics simulations — collision data stored as NumPy arrays               |
| **SpaceX**           | Telemetry data analysis — sensor readings as NumPy arrays                          |
| **Pfizer / Moderna** | Drug discovery simulations — molecular data in NumPy arrays                        |

**Finance & Trading**
Stock prices, portfolio weights, risk matrices — all 2D NumPy arrays.

| Company                 | How They Use NumPy                                            |
| ----------------------- | ------------------------------------------------------------- |
| **Goldman Sachs** | Quantitative trading — price time series as NumPy arrays     |
| **JPMorgan**      | Risk modeling — Monte Carlo simulations with NumPy           |
| **Bloomberg**     | Financial data processing — tick data stored as NumPy arrays |
| **Citadel**       | High-frequency trading signals — vectorized NumPy operations |

**Computer Vision**
Every image is a NumPy array: `shape = (height, width, 3)` where 3 = RGB channels.

| Company                   | How They Use NumPy                                                     |
| ------------------------- | ---------------------------------------------------------------------- |
| **Google**          | Google Photos — image classification, each image is a NumPy 3D array  |
| **Tesla**           | Autopilot camera frames — each frame is `(720, 1280, 3)`NumPy array |
| **Medical imaging** | MRI/CT scans — 3D NumPy arrays `(depth, height, width)`             |
| **Snapchat**        | AR filters — face detection on NumPy image arrays                     |

---

## 3️⃣ Python `list` vs `array` vs NumPy

```python
import sys
import numpy as np
from array import array

n = 1_000_000

# Memory comparison
py_list   = list(range(n))
py_array  = array('i', range(n))
np_array  = np.arange(n)

print(sys.getsizeof(py_list))    # ~8,697,456 bytes  (~8.7 MB)
print(py_array.buffer_info()[1] * py_array.itemsize)  # ~4,000,000 bytes (~4 MB)
print(np_array.nbytes)           # ~4,000,000 bytes  (~4 MB)
```

| Feature           | Python `list` | `array`module             | NumPy array            |
| ----------------- | --------------- | --------------------------- | ---------------------- |
| Type              | Any mix         | Single type                 | Single type            |
| Memory            | High            | Low                         | Low                    |
| Speed             | Slow            | Medium                      | Very fast              |
| Multi-dimensional | ❌              | ❌                          | ✅                     |
| Math operations   | Manual loops    | Manual loops                | Vectorized (no loops!) |
| Use case          | General purpose | Typed buffers               | Math, ML, science      |
| Import            | Built-in        | `from array import array` | `import numpy as np` |

---

## 🔢 Dimensions in ML Context

Understanding array dimensions is critical for ML:

```python
import numpy as np

# Single image (height × width × RGB channels)
image = np.zeros((224, 224, 3))       # shape: (224, 224, 3)

# Batch of images (batch_size × height × width × channels)
batch = np.zeros((32, 224, 224, 3))   # shape: (32, 224, 224, 3)
#                  ↑
#              32 images at once (batch_size)

# Text (sequence_length × embedding_dim)
embedding = np.zeros((512, 768))      # shape: (512, 768)
#                      ↑       ↑
#               512 tokens  768-dim vector per token

# Neural network weights (input_features × output_features)
weights = np.random.randn(784, 128)   # shape: (784, 128)
#                           ↑    ↑
#                       MNIST pixel  hidden layer size
```

---

## 🤖 Arrays in AI & ML Pipeline

```
Raw Data → NumPy Arrays → Preprocessing → Model Input → Output
   ↓              ↓              ↓              ↓           ↓
CSV file    np.array()    normalize()    tensor()    np.argmax()
Images      imread()      reshape()      batch()     softmax()
Text        tokenize()    embed()        pad()       decode()
```

**Why NumPy is the Lingua Franca of ML:**

```python
import numpy as np

# 1. Load data
X = np.loadtxt('data.csv', delimiter=',')   # shape: (1000, 10)

# 2. Normalize (zero mean, unit variance)
X = (X - X.mean(axis=0)) / X.std(axis=0)

# 3. Train/test split
X_train, X_test = X[:800], X[800:]

# 4. Dot product (forward pass of a neural layer)
weights = np.random.randn(10, 5)
output = np.dot(X_train, weights)            # shape: (800, 5)

# 5. Activation
activated = np.maximum(0, output)            # ReLU: max(0, x)
```

---

## 💡 Key Takeaway

> Arrays are not just a data structure — they are the  **language of computation** . Every image you see, every song you hear, every ML model prediction, every game frame rendered — all of it is arrays being sliced, multiplied, summed, and transformed at blistering speed. NumPy makes this possible in Python. Without NumPy arrays, there is no TensorFlow, no PyTorch, no scikit-learn, no modern AI.

---

*Arrays are the atoms of data science. Everything else is made of them.* ⚛️
