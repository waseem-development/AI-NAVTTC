import cv2
img_gray = cv2.imread('./Images/lena.png', cv2.IMREAD_GRAYSCALE)
# ── Simple Threshold ─────────────────────────────────────
# Arguments: (source, threshold_value, max_value, type)
# threshold_value = 120 → pixels > 120 become max_value (255)
# pixels <= 120 become 0 (black)
ret, img_binary = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)
print('Threshold used:', ret) # returns the actual threshold value
# ── Otsu's Method (automatic threshold selection) ────────
# Otsu's algorithm automatically finds the BEST threshold value
# by minimising within-class variance (no manual guessing needed!)
ret_otsu, img_otsu = cv2.threshold(
img_gray, 0, 255,
cv2.THRESH_BINARY + cv2.THRESH_OTSU # combine flags with +
)
print('Otsu threshold found:', ret_otsu)

cv2.imshow('Grayscale', img_gray)
cv2.imshow('Binary T=120', img_binary)
cv2.imshow('Otsu Binary', img_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()