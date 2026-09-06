import numpy as np
import cv2
import os

from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

dataset_path = "./dataset/cats"
size = 64

X, y = [], []
classes = sorted(os.listdir(dataset_path))

for label, d_class in enumerate(classes):
    directory = os.path.join(dataset_path, d_class)

    for image in os.listdir(directory):
        img = cv2.imread(os.path.join(directory, image))

        if img is not None:
            img = cv2.resize(img, (size, size))
            X.append(img.flatten() / 255.0)
            y.append(label)

X = np.array(X)
y = np.array(y)

print("Classes:", classes)
print("Images:", len(X))
print("Features:", X.shape[1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

knn = KNeighborsClassifier(n_neighbors=5, metric="euclidean")
knn.fit(X_train, y_train)

y_prediction = knn.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_prediction))
print("\nClassification Report:")
print(classification_report(y_test, y_prediction, target_names=classes))