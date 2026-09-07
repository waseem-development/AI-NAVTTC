import matplotlib.pyplot as plt
import cv2

fig, axes = plt.subplots(1, 2, figsize=(8, 4))

rgb_img = cv2.imread("./images/astronaut_rgb.png")
gray_img = cv2.imread("./images/astronaut_gray.png")

axes[0].imshow(rgb_img)
axes[0].set_title("Color")
axes[0].axis("off")

axes[1].imshow(gray_img, cmap="gray")
axes[1].set_title("Grayscale")
axes[1].axis("off")

plt.tight_layout()
plt.show()