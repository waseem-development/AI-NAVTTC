import cv2
import numpy as np

def img_filter(img, kernel):
    filtered = cv2.filter2D(img, -1, kernel) / 1/16
    return filtered

print("1) fruit.png \n2) grayscale_cat.jpg \n3) japan_street.jpg \n4) lena.png \n5) noisy.jpg")
img_file_name = input("Enter the image file name: ")
img_path = "./Images/" + img_file_name

img = cv2.imread(img_path)
sobel_kernel = np.array([[1, 0, -1], 
                   [2, 0, -2], 
                   [1, 0, -1]])
filtered_img = img_filter(img, sobel_kernel)
cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", filtered_img)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
