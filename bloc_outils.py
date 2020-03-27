import numpy as np

from vectoriel import vectoriel
from norme import norme
from ECEF2LLA import ECEF2LLA


# DEBUG
if __name__ == '__main__':
    u = np.array([1, 2, 3])
    v = np.array([4, 5, 6])

    w = vectoriel(u, v)
    print(w)

    norm_u = norme(u)
    print(norm_u)
