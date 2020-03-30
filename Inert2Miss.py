import numpy as np
import check
from Euler2DCM import Euler2DCM


def Inert2Miss(euler, u):
    '''
    Calcul les composantes d'un vecteur du repère inertiel dans le repère missile.
    '''
    check.vecteur_n(3, euler, "bloc outils/Inert2Miss")
    check.vecteur_n(3, u, "bloc outils/Inert2Miss")

    dcm = Euler2DCM(euler)
    v = dcm.dot(u)
    return v


# DEBUG
if __name__ == '__main__':
    # print(help(Inert2Miss))
    e = np.array([0.4, -0.3, 1.3])
    u = np.array([200, 300, 600])

    v = Inert2Miss(e, u)
    print(v)
