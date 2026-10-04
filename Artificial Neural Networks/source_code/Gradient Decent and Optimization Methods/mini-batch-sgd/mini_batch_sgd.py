# import the necessary packages
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
    preds[preds > 0] = 1

    # return the predictions
    return preds

def next_batch(X, y, batchSize):
    # loop over our dataset ‘X‘ in mini-batches, yielding a tuple of
    # the current batched data and labels
    for i in np.arange(0, X.shape[0], batchSize):
        yield (X[i:i + batchSize], y[i:i + batchSize])
        
epochs = 100
alpha = 0.01
batch_size = 32

#Generate Dataset
(X, y) = make_blobs(n_samples=1000, n_features=2, centers=2,
        cluster_std=1.5, random_state=1)
y = y.reshape((y.shape[0], 1))

#Add the column of 1's for the bias trick
X = np.c_[X, np.ones((X.shape[0]))]

# partition the data into training and testing splits using 50% of
# the data for training and the remaining 50% for testing
(trainX, testX, trainY, testY) = train_test_split(X, y,
        test_size=0.5, random_state=42)

# initialize our weight matrix and list of losses
print("[INFO] training...")
W = np.random.randn(X.shape[1], 1)
losses = []

## loop over the desired number of epochs
for epoch in np.arange(0, epochs):
    # initialize the total loss for the epoch
    epochLoss = []
#
#    # loop over our data in batches
    for (batchX, batchY) in next_batch(X, y, batch_size):
    #batchX = next_batch(X, y, batch_size)
    #print(batchX)
        #print(batchX)
        #break
        preds = sigmoid_activation(batchX.dot(W))
        # Find the error and sum the error and record 
        error = preds - batchY
        epochLoss.append(np.sum(error ** 2))
    
        #Calculate the gradient 
        gradient = batchX.T.dot(error)
        
        #Update the W 
        W += -alpha * gradient

    # update our loss history by taking the average loss across all
    # batches
    loss = np.average(epochLoss)
    losses.append(loss)

    # check to see if an update should be displayed
    if epoch == 0 or (epoch + 1) % 5 == 0:
        print("[INFO] epoch={}, loss={:.7f}".format(int(epoch + 1),
            loss))

# evaluate our model
print("[INFO] evaluating...")
preds = predict(testX, W)
print(classification_report(testY, preds))
