import numpy as np

def shuffle_data(X, y, seed=None):
    # Your code here
    np.random.seed(seed)

    n = X.shape[0]

    value = np.random.permutation(n)

    return (X[value], y[value])
