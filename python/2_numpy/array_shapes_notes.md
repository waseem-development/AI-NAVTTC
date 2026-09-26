# Understanding NumPy Arrays: Shape, Axes, Features & Images

## Before Anything Else: How to Read a Shape

A shape is just a tuple of numbers. Each number tells you  **how many things exist in that direction** .

```python
shape = (3, 4)
#        │  └── 4 things in direction 1
#        └───── 3 things in direction 0
```

You always read left to right. The leftmost number is always the **outermost** container.

Think of it like Russian dolls:

* The first number = how many big dolls you have
* The second number = how many medium dolls inside each big one
* The third number = how many small dolls inside each medium one
* ...and so on

---

## 0D Array — A Single Number (Scalar)

```python
x = np.array(7)
x.shape  # ()
x.ndim   # 0
```

No brackets, no dimensions. Just a bare number. That's it.

```
7
```

**Real examples:** a loss value like `0.52`, a temperature like `38`, an age like `25`.

---

## 1D Array — A List of Numbers (Vector)

```python
x = np.array([10, 20, 30, 40])
x.shape  # (4,)
x.ndim   # 1
```

Shape is `(4,)` — the comma is just Python's way of saying "this is a tuple with one number".

It means: **4 values in one direction.**

```
[10  20  30  40]
 ↑
 axis 0 (the only axis, length = 4)
```

**Real examples:** a row of marks, a list of prices, values over time.

---

## 2D Array — A Table (Matrix)

```python
x = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
x.shape  # (2, 3)
x.ndim   # 2
```

Shape `(2, 3)` means:

* **2** rows (axis 0)
* **3** columns (axis 1)

```
         axis 1 →  (columns)
                col0  col1  col2
axis 0 ↓  row0  [ 1    2    3 ]
(rows)    row1  [ 4    5    6 ]
```

```python
x.sum(axis=0)  # collapse rows → adds DOWN each column  → [5, 7, 9]
x.sum(axis=1)  # collapse cols → adds ACROSS each row   → [6, 15]
```

**Real examples:** an Excel spreadsheet, a dataset, a grayscale image.

---

## 3D Array — A Stack of Tables

```python
x.shape = (5, 4, 3)
```

Read this as nested dolls:

* **5** tables (outermost)
  * each table has **4** rows
    * each row has **3** values

```
Layer 0:        Layer 1:        ...     Layer 4:
[· · ·]         [· · ·]                 [· · ·]
[· · ·]         [· · ·]                 [· · ·]
[· · ·]         [· · ·]                 [· · ·]
[· · ·]         [· · ·]                 [· · ·]
```

Now here's the part the original document skipped explaining:

---

### ⚠️ Why do 3D examples look different from each other?

Because shape has **no fixed meaning** — it depends on what you're storing.

#### Example A: A single RGB image → `(64, 64, 3)`

```
shape = (64, 64, 3)
         │    │   └── 3 channels: [Red, Green, Blue]
         │    └─────── 64 pixels wide (columns)
         └──────────── 64 pixels tall (rows)
```

So for each of the 64×64 = 4096 pixels, you store 3 numbers (R, G, B).

One pixel looks like: `[255, 0, 0]` = pure red.

The axis meaning here:

* axis 0 = height (row of pixels)
* axis 1 = width (column of pixels)
* axis 2 = color channel

#### Example B: 10 grayscale images → `(10, 28, 28)`

```
shape = (10, 28, 28)
          │    │    └── 28 columns (width)
          │    └─────── 28 rows (height)
          └──────────── 10 images
```

Here the **outermost** dimension is "which image". Each image is 28×28 pixels, and since it's  **grayscale** , there are no color channels — each pixel is just one number (0–255).

The axis meaning here:

* axis 0 = image index (which of the 10 images)
* axis 1 = height
* axis 2 = width

---

### So why does `(64, 64, 3)` put channels last, but `(10, 28, 28)` doesn't have channels at all?

Because:

* `(64, 64, 3)` is **one RGB image** — channels go at the end
* `(10, 28, 28)` is **10 grayscale images** — no channel dimension needed, the "10" is the count of images

They're just storing different things. The shape tells you what's inside, but **you** decide what each axis means based on your data.

---

## 4D Array — A Batch of Images (Used in Deep Learning)

```python
x.shape = (8, 64, 64, 3)
```

```
shape = (8,  64,  64,  3)
         │    │    │    └── channels (RGB)
         │    │    └─────── width
         │    └──────────── height
         └───────────────── batch size (how many images)
```

This is the standard format for feeding images into a neural network:
`(batch_size, height, width, channels)`

You train on 8 images at the same time — one "batch".

---

## 5D Array — A Batch of Videos

```python
x.shape = (32, 10, 64, 64, 3)
```

```
shape = (32,  10,  64,  64,  3)
          │    │    │    │    └── channels
          │    │    │    └─────── width
          │    │    └──────────── height
          │    └───────────────── frames (time steps)
          └────────────────────── batch size
```

Standard format: `(batch, time, height, width, channels)`

32 videos, each 10 frames long, each frame is a 64×64 RGB image.

---

## 6D Array — Even Higher (Advanced Use)

```python
x.shape = (4, 8, 10, 64, 64, 3)
```

```
shape = (4,   8,   10,  64,  64,  3)
          │    │    │    │    │    └── channels
          │    │    │    │    └─────── width
          │    │    │    └──────────── height
          │    │    └───────────────── frames
          │    └────────────────────── batches
          └─────────────────────────── experiments (or cameras, or subjects...)
```

Used in research settings — e.g., 4 camera angles, each recording 8 batches of 10-frame videos.

---

## Summary Table (With Explanations This Time)

| Dimensions | Example Shape             | What Each Number Means                          |
| ---------- | ------------------------- | ----------------------------------------------- |
| 0D         | `()`                    | Just a number                                   |
| 1D         | `(5,)`                  | 5 values in a line                              |
| 2D         | `(3, 4)`                | 3 rows, 4 columns                               |
| 3D         | `(10, 28, 28)`          | 10 images, each 28 tall, 28 wide (grayscale)    |
| 3D         | `(64, 64, 3)`           | One image: 64 tall, 64 wide, 3 color channels   |
| 4D         | `(8, 64, 64, 3)`        | 8 images, 64×64, RGB                           |
| 5D         | `(32, 10, 64, 64, 3)`   | 32 videos, 10 frames each, 64×64 RGB           |
| 6D         | `(4, 8, 10, 64, 64, 3)` | 4 experiments, 8 batches, 10 frames, 64×64 RGB |

---

## What is Axis?

Axis = dimension index. The first dimension is axis 0, second is axis 1, etc.

```python
x.shape = (2, 3)

x.sum(axis=0)  # sum along axis 0 (collapse rows, result has shape (3,))
# → [5, 7, 9]

x.sum(axis=1)  # sum along axis 1 (collapse columns, result has shape (2,))
# → [6, 15]
```

A helpful mental model: **summing along an axis removes that axis.**
`(2, 3)` with `axis=0` removed → shape `(3,)`
`(2, 3)` with `axis=1` removed → shape `(2,)`

---

## What are Features?

In machine learning, features are the **input columns** of your dataset.

| Age | Salary | Experience | Bought? |
| --- | ------ | ---------- | ------- |
| 22  | 30000  | 1          | No      |
| 35  | 70000  | 10         | Yes     |

* **Features (X):** Age, Salary, Experience → shape `(2, 3)` = 2 samples, 3 features
* **Target (y):** Bought → shape `(2,)` = 2 labels

```python
X = np.array([
    [22, 30000, 1],
    [35, 70000, 10]
])
X.shape  # (2, 3) → (samples, features)
```

The rule in ML: **rows = samples, columns = features.**

---

## Images in NumPy — Full Picture

### Grayscale image

```
shape = (28, 28)
```

Each pixel is one number from 0 (black) to 255 (white). No channel dimension needed.

### RGB image

```
shape = (64, 64, 3)
```

Each pixel is three numbers: `[Red, Green, Blue]`.

* `[255, 0, 0]` = red
* `[0, 255, 0]` = green
* `[0, 0, 0]` = black
* `[255, 255, 255]` = white

### Batch of grayscale images

```
shape = (100, 28, 28)
```

100 images, each 28×28, no color.

### Batch of RGB images

```
shape = (64, 224, 224, 3)
```

64 images, each 224×224, with RGB color. This is a standard CNN input.

---

## Common ML Shape Cheatsheet

| What You Have        | Shape Format                          | Example                |
| -------------------- | ------------------------------------- | ---------------------- |
| Tabular dataset      | `(samples, features)`               | `(1000, 10)`         |
| Grayscale image      | `(height, width)`                   | `(28, 28)`           |
| RGB image            | `(height, width, 3)`                | `(224, 224, 3)`      |
| Batch of gray images | `(batch, height, width)`            | `(32, 28, 28)`       |
| Batch of RGB images  | `(batch, height, width, 3)`         | `(64, 224, 224, 3)`  |
| Sequence data (RNN)  | `(batch, timesteps, features)`      | `(32, 100, 20)`      |
| Video batch          | `(batch, frames, height, width, 3)` | `(8, 30, 64, 64, 3)` |

---

## The One Rule That Ties Everything Together

> **Shape has no fixed meaning. You assign meaning to each axis based on what you're storing.**

The same 3-number shape `(10, 28, 28)` could mean:

* 10 grayscale images of size 28×28, OR
* 10 time steps, each with a 28×28 measurement, OR
* anything else with those dimensions

The shape tells you  **sizes** . Context (and you) tell you  **what those sizes represent** .

When you see a shape you don't understand, just ask:

> *"What does each axis represent in this specific problem?"*

That's how professionals read tensors.
