import numpy as np

def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.
    a = np.asarray(a)
    b = np.asarray(b)
    if a.shape == b.shape:
        return a + b
    else:
        return -1