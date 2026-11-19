import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X = np.asarray(X)
    y = np.asarray(y)
    A = X.T @ X
    b = X.T @ y
    theta = np.round(np.linalg.solve(A,b), 4)
    return theta