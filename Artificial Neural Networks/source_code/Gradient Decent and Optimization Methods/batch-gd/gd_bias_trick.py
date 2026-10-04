import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([1, 2, 3, 4])  # Feature (x)
y = np.array([2, 2.8, 3.6, 4.5])  # Target (y)

# Add an intercept term (column of ones) to X for theta_0
X = np.c_[np.ones(X.shape[0]), X]  # X becomes [[1, 1], [1, 2], [1, 3], [1, 4]]

# Initial parameters (theta_0 and theta_1)
W = np.zeros(2)

# Hyperparameters learning rate and epochs
alpha = 0.01
epochs = 1000

# Cost function: Mean Squared Error
def compute_loss(X, y, W):
    m = len(y)
    predictions = X.dot(W)
    loss = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return loss

# Gradient Descent algorithm
def gradient_descent(X, y, W, alpha, epochs):
    m = len(y)
    loss_history = np.zeros(epochs)

    for i in range(epochs):
        predictions = X.dot(W)
        errors = predictions - y
        W = W - (alpha / m) * X.T.dot(errors)
        loss_history[i] = compute_loss(X, y, W)

    return W, loss_history

# Run gradient descent
W, loss = gradient_descent(X, y, W, alpha, epochs)

# Output the learned parameters
print(f"Learned parameters: theta_0 = {W[0]:.2f}, theta_1 = {W[1]:.2f}")

# Plotting the cost function over iterations
plt.plot(range(epochs), loss)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Cost Function Over Time")
plt.show()

# Plot the data and the linear regression line
plt.scatter(X[:, 1], y, color='red', marker='x', label='Training Data')
plt.plot(X[:, 1], X.dot(W), label='Linear Regression')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
