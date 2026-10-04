import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([1, 2, 3, 4]).reshape(4,1) # Feature (x)
y = np.array([2, 2.8, 3.6, 4.5])  # Target (y)

#print(X.shape)

# Add an intercept term (column of ones) to X for theta_0
#X = np.c_[np.ones(X.shape[0]), X]  # X becomes [[1, 1], [1, 2], [1, 3], [1, 4]]

# Initial parameters (theta_0 and theta_1)
W = np.zeros(1)
#print(theta.shape)

def compute_loss(X, y, W):
    m = len(y)
    predictions = X.dot(W)
    loss = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return loss

def gradient_descent(X, y, W, alpha, epochs):
    m = len(y)
    loss_history = np.zeros(epochs)

    for i in range(epochs):
        predictions = X.dot(W)
        errors = predictions - y
        W = W - (alpha / m) * X.T.dot(errors)
        loss_history[i] = compute_loss(X, y, W)

    return W, loss_history

#preds = X.dot(W)
#errors = preds - y
epochs=100
W, loss = gradient_descent(X, y, W, 0.01, epochs)

print(f"Learned parameter: W = {W[0]:.2f}")
plt.plot(range(epochs), loss)
plt.show()



