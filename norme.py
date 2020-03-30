import numpy as np
import check


def norme(u):
    '''
    Calcul la norme quadratique d'un vecteur.
    '''
    check.vecteur(u, "bloc_outils/norme")

    norm = np.linalg.norm(u)
    return norm


# DEBUG
if __name__ == '__main__':
    # print(help(norme))
    u = np.array([1, 3, 1])
    norm = norme(u)
    print(norm)
