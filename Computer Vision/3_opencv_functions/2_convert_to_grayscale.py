import cv2
# Load colour image
img_color = cv2.imread('./Images/fruit.png', cv2.IMREAD_COLOR)
# ── Convert to Grayscale ─────────────────────────────────
# Formula used internally: Gray = 0.114*B + 0.587*G + 0.299*R
# (green gets most weight because human eyes are most sensitive to green)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
print('Color shape:', img_color.shape) # (H, W, 3)
print('Gray shape:', img_gray.shape) # (H, W) ← only 2D!
cv2.imshow('Color', img_color)
cv2.imshow('Grayscale', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()