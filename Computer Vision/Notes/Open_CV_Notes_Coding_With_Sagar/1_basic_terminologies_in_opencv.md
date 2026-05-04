# 🖼️ Image Fundamentals — Computer Vision

> *"An image is just numbers — understanding that is the first step in Computer Vision."*

---

## 1. Image — A 2D Grid

An image is represented as a **2-dimensional grid** of values, just like a matrix in mathematics.

```
[ [ 120, 85, 200, 34 ],
  [ 45,  67, 189, 90 ],
  [ 230, 12, 78,  56 ],
  [ 99, 145, 201, 33 ] ]
```

| Property | Description |
|----------|-------------|
| **Width** | Number of columns |
| **Height** | Number of rows |
| **Shape** | `(height, width)` for grayscale · `(height, width, channels)` for color |

```python
import cv2
img = cv2.imread("photo.jpg")
print(img.shape)   # → (480, 640, 3)  ← height × width × channels
```

---

## 2. Pixel — Smallest Unit of a Picture

A **pixel** (picture element) is the smallest individual unit in an image. It holds one or more numeric values depending on the image type.

```
         col 0   col 1   col 2
row 0  [  120     85     200  ]
row 1  [   45     67     189  ]   ← img[1][2] = 189
row 2  [  230     12      78  ]
```

| Image Type | Values per Pixel | Range |
|------------|-----------------|-------|
| Grayscale | 1 | `0` (black) → `255` (white) |
| Color (RGB/BGR) | 3 | `[R, G, B]` each `0–255` |
| Color + Alpha | 4 | `[R, G, B, A]` |

```python
pixel_value = img[100, 200]     # pixel at row=100, col=200
print(pixel_value)              # → [B G R] in OpenCV
```

---

## 3. Color Channels

A **color channel** stores one part of the color information for every pixel in the image. A color image is made of **multiple stacked channels**.

### RGB vs BGR

```
RGB Order (standard)     BGR Order (OpenCV default)
─────────────────────    ──────────────────────────
Channel 0 → Red          Channel 0 → Blue
Channel 1 → Green        Channel 1 → Green
Channel 2 → Blue         Channel 2 → Red
```

> ⚠️ **OpenCV loads images in BGR**, not RGB. Always convert when using matplotlib!
> ```python
> img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
> ```

### Accessing Individual Channels

```python
img = cv2.imread("photo.jpg")   # shape: (H, W, 3) — BGR

B = img[:, :, 0]    # Blue channel
G = img[:, :, 1]    # Green channel
R = img[:, :, 2]    # Red channel

# Or split all at once:
B, G, R = cv2.split(img)
```

### Visual Breakdown

```
Original Image (H × W × 3)
        │
   ┌────┴────┐
   ↓         ↓         ↓
 [Blue]    [Green]    [Red]
 H × W     H × W     H × W
(0–255)   (0–255)   (0–255)
```

---

## 4. Image Formats

Image formats define **how pixel data is encoded and stored on disk**.

| Format | Type | Transparency | Best For |
|--------|------|-------------|----------|
| `.jpg` / `.jpeg` | Lossy compression | ✗ | Photos, web images |
| `.png` | Lossless compression | ✓ | Screenshots, diagrams, icons |
| `.bmp` | Uncompressed (raw) | ✗ | Simple raw storage |
| `.tiff` | Lossless / HDR | ✓ | Medical, scientific imaging |
| `.webp` | Lossy + lossless | ✓ | Modern web images |

### Lossy vs Lossless

```
Original pixel data
       │
  ┌────┴─────────────────────────────────┐
  ↓                                      ↓
Lossy (.jpg)                     Lossless (.png)
Discards some data               Keeps every pixel
Smaller file size                Larger file size
Cannot fully recover             Perfect recovery
```

```python
cv2.imwrite("output.jpg", img)   # lossy — smaller file
cv2.imwrite("output.png", img)   # lossless — exact pixels
```

---

## Quick Reference

```
Image
 └── 2D grid of pixels (H × W for grayscale, H × W × C for color)
      └── Pixel
           └── Smallest unit — one value (grayscale) or [B, G, R] (color in OpenCV)
                └── Channel
                     └── One slice of color info per pixel
                          └── Stored on disk via Image Format (.jpg, .png, .bmp …)
```

---

*Notes for CS731: Deep Learning for Computer Vision*