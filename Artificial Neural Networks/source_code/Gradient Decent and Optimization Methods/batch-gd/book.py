from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import argparse

def sigmoid_activation(x):
    # compute the sigmoid activation value for a given input
    return 1.0 / (1 + np.exp(-x))

def predict(X, W):
    # take the dot product between our features and weight matrix
    preds = sigmoid_activation(X.dot(W))
    # apply a step function to threshold the outputs to binary
    # class labels
    preds[preds <= 0.5] = 0
    preds[preds > 0.5] = 1

    # return the predictions
    return preds

# generate a 2-class classification problem with 1,000 data points,
# where each data point is a 2D feature vector
# Generate the dataset X, 1000 samples and lables y
(X, y) = make_blobs(n_samples=1000, n_features=2, centers=2,
        cluster_std=1.5, random_state=1)

#print(y)
y = y.reshape((y.shape[0], 1))
#print(y)
#print(y[0:9])
# insert a column of 1’s as the last entry in the feature
# matrix -- this little trick allows us to treat the bias
# as a trainable parameter within the weight matrix
X = np.c_[X, np.ones((X.shape[0]))]
#print(X)

# partition the data into training and testing splits using 50% of
# the data for training and the remaining 50% for testing
(trainX, testX, trainY, testY) = train_test_split(X, y,
        test_size=0.5, random_state=42)

# initialize our weight matrix and list of losses
print("[INFO] training...")
W = np.random.randn(X.shape[1], 1)
losses = []
print(W)

epochs = 100
# loop over the desired number of epochs
#for epoch in np.arange(0, epochs):
#    #dot product the X and W and pass it to the sigmoid function
#    #print(W.shape) 
#    preds = sigmoid_activation(trainX.dot(W))
#    error = preds - trainY
#    loss = np.sum(error ** 2)
#    losses.append(loss)
#    
#    #Calculate the new value of the gradient descent
#    gradient = trainX.T.dot(error)
#
#    #The update stage, in the negative direction 
#    W += -0.01 * gradient
#    # check to see if an update should be displayed
#    if epoch == 0 or (epoch + 1) % 5 == 0:
#        print("[INFO] epoch={}, loss={:.7f}".format(int(epoch + 1),
#            loss))
#        #print(loss)
#
#k# evaluate the model
#print("[INFO] evaluating...")
#preds = predict(testX, W)
#print(classification_report(testY, preds))
#
## plot the (testing) classification data
#plt.style.use("ggplot")
#plt.figure()
#plt.title("Data")
#plt.scatter(testX[:, 0], testX[:, 1], marker="o", c=testY, s=30)
#
## construct a figure that plots the loss over time
#plt.style.use("ggplot")
#plt.figure()
#plt.plot(np.arange(0, epochs), losses)
#plt.title("Training Loss")
#plt.xlabel("Epoch #")
#plt.ylabel("Loss")
#plt.show()


