import numpy as np
from DeepLearningModules import ActivationFunc as AF

def init_newtwork():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = AF.Sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = AF.Sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = AF.IdentityFunc(a3)
    return y

network = init_newtwork()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
