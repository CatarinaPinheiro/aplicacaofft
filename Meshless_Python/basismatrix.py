import numpy as np
from scipy import linalg as la


def create_basis(basis, data, point=None, r=None):
    P = []
    for dat in data:
        row = []
        for b in basis:
            [x, y] = dat[0:2]
            if point is not None and la.norm(np.subtract(point, [x, y])) > r:
                row.append(0)
            else:
                row.append(eval(b))
        P.append(row)
    return P
