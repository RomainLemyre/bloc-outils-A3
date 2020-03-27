import numpy as np
import sys
sys.tracebacklimit = 0  # Nombre de message lors d'une exception


def vecteur_n(v, module, fonction):
    check_ndarray(v, module, fonction)
    check_dim_1(v, module, fonction)
    check_str(v, module, fonction)


def vecteur_3(v, module, fonction):
    check_ndarray(v, module, fonction)
    check_shape_3(v, module, fonction)
    check_str(v, module, fonction)


def check_dim_1(v, module, fonction):
    if v.ndim != 1:
        raise SyntaxError("Le paramètre n'est pas de dimension (n,1) [{}][{}]".format(module, fonction))


def check_shape_3(v, module, fonction):
    if v.shape != (3,):
        raise SyntaxError("Le paramètre n'est pas de dimension (3,1) [{}][{}]".format(module, fonction))


def check_ndarray(v, module, fonction):
    if not isinstance(v, np.ndarray):
        raise TypeError("Le paramètre n'est pas de type numpy.ndarray [{}][{}]".format(module, fonction))


def check_str(v, module, fonction):
    for k in v:
        if isinstance(k, str):
            raise ValueError("Le paramètre ne doit contenir que des nombres [{}][{}]".format(module, fonction))
