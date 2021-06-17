import numpy as np


def dist(vec)->float:
    x = 0.
    for i in vec:
        x = x + np.power(i,2)
    x = np.sqrt(x)
    return x

dist([1,2,3])


