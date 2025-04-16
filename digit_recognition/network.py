import random
import numpy as np

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes) #number of layers
        self.sizes = sizes #layer sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]] #random initial offsets
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])] #random initial link weights

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
            return a

def sigmoid(z): #sigmoid activation function
    return 1.0 / (1.0 + np.exp(-z))



net = Network([2, 3, 1]) #creation a neural network of three layers

print('Number of layers:', net.num_layers)
for i in range(net.num_layers):
    print('Number of neurons in the layer', i,':',net.sizes[i])
for i in range(net.num_layers-1):
    print('W_',i+1,':')
    print(np.round(net.weights[i],2))
    print('b_',i+1,':')
    print(np.round(net.biases[i],2))