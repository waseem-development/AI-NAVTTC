import numpy as np
import cv2

SIZE =  32
labels = ["dog", "cat", "panda"]
np.random.seed(1)

wieght = np.random.randn(3, 3072)
bias = np.random.randn(3)

original_image = cv2.imread("panda.jpeg")
img = cv2.resize(original_image, (SIZE, SIZE)).flatten()  
scores = wieght.dot(img) + bias

print(scores)
for (label, score) in zip(labels, scores):
    print("[INFO] {}: {:.2f}".format(label, score))

cv2.putText(
    original_image,
    "Label: {}".format(labels[np.argmax(scores)]),
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.9,
    (0, 255, 0),
    2
)

cv2.imshow("img", original_image)





while True: 
    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break
cv2.destroyAllWindows()
    
