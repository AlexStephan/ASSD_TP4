import numpy as np


def dist(vec)->float:
    x = 0.
    for i in vec:
        x = x + np.power(i,2)
    x = np.sqrt(x)
    return x

dist([1,2,3])

###################################


from scipy import spatial
A=[[1,1],[0,1],[1,0]]
tree = spatial.KDTree(A)
tree.query([0,0])