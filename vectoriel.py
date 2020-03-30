import numpy as np
import check


def vectoriel(u, v):
    '''
    Calcul le produit vectoriel de deux vecteur 3x1
    '''
    params = [u, v]
    for i, p in enumerate(params):
        check.vecteur_n(3, p, "bloc outils/vectoriel")

    w = np.cross(u, v)
    return w


# DEBUG
if __name__ == '__main__':
    # print(help(vectoriel))
    u = np.array([1, 4, 5])
    v = np.array([0.1, 0.4, 6])
    w = vectoriel(u, v)
    print(w)
