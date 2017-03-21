import numpy as np

class Perceptron(object):

    """
    eta - learning rate [0.0; 1.0]
    n_iters - number of iterations
    """
    def __init__(self, eta=0.01, n_iters=10):
        self.eta = eta # learning rate