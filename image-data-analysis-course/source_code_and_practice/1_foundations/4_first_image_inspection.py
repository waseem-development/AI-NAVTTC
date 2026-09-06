# import cv2

# # 1. Read the image
# img = cv2.imread("./images/panda.jpeg")

# # 2. Process the image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# small = cv2.resize(gray, (128, 128))

# # 3. Save the image
# cv2.imwrite("./images/panda_small_gray.png", small)

# # 4. Display the image (Pass the 'small' array, NOT the string path)
# cv2.imshow("Original Panda", img)
# cv2.imshow("Small Panda Grayscale", small)
# # 5. Keep the window open until a key is pressed, then clean up
# cv2.waitKey(0)
# cv2.destroyAllWindows()



from skimage import io, color, transform

# 1. Load, convert, and resize
img = io.imread("./images/panda.jpeg")          
gray = color.rgb2gray(img)                     
small = transform.resize(gray, (128, 128))

# 2. Display the image using skimage
io.imshow(small)

# 3. Block execution and keep the window open
io.show()
