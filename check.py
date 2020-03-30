import numpy as np
import sys
sys.tracebacklimit = 0  # Nombre de message lors d'une exception


def vecteur(v, path):
    check_ndarray(v, path)
    check_dim_1(v, path)
    check_str(v, path)


def vecteur_n(n, v, path):
    check_ndarray(v, path)
    check_shape_n(n, v, path)
    check_str(v, path)


def check_dim_1(v, path):
    if v.ndim != 1:
        raise SyntaxError("Le paramètre n'est pas de dimension (n,1) [{}]".format(path))


def check_shape_n(n, v, path):
    if v.shape != (n,):
        raise SyntaxError("Le paramètre n'est pas de dimension ({},1) [{}]".format(n, path))


def check_ndarray(v, path):
    if not isinstance(v, np.ndarray):
        raise TypeError("Le paramètre n'est pas de type numpy.ndarray [{}]".format(path))


def check_str(v, path):
    for k in v:
        if isinstance(k, str):
            raise ValueError("Le paramètre ne doit contenir que des nombres [{}]".format(path))
