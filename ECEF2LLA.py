import numpy as np
import math
import check

from norme import norme

A = 6378137  # 1/2 grand axe equatorial de l'ellipsoïde
B = 6356752.3142  # 1/2 grand axe polaire de l'ellipsoïde
E = 0.08181919092891  # Excentricité de l'ellipsoïde


def ECEF2LLA(ecef):
    '''
    Transforme les coordonnées dans le repère ECEF (Earth-Centered 
    Earth Fixed)  [m,m,m] en coordonnées géographiques LLA 
    [rad,rad,m] par rapport à l'ellipsoïde de référence)
    '''
    check.vecteur_3(ecef, "bloc outils", "ECEF2LLA")

    r = calcul_r(ecef)

    phi = calcul_latitude(ecef, r)
    lmbda = calcul_longitude(ecef)
    h = calcul_h(phi, r, ecef)

    return np.array([phi, lmbda, h])


def calcul_r(xyz_ecef):
    return norme(xyz_ecef[:2])


def calcul_longitude(xyz_ecef):
    return math.atan2(xyz_ecef[1], xyz_ecef[0])


def calcul_latitude(xyz_ecef, r):
    mu = calcul_mu(xyz_ecef, r)
    num_phi = calcul_numPhi(mu, xyz_ecef)
    den_phi = calcul_denPhi(mu, r)
    return math.atan2(num_phi, den_phi)


def calcul_mu(xyz_ecef, r):
    return math.atan2(xyz_ecef[2], r * (1 - f()))


def f():
    return 1 - np.sqrt(1 - np.absolute(E)**2)


def calcul_numPhi(mu, xyz_ecef):
    return np.sin(mu)**3 * B * np.absolute(E)**2 + xyz_ecef[2]


def calcul_denPhi(mu, r):
    return r - np.cos(mu)**3 * A * np.absolute(E)**2


def calcul_h(phi, r, xyz_ecef):
    a = r * np.cos(phi)
    b = xyz_ecef[2] * np.sin(phi)
    c = np.sqrt(1 - (np.absolute(np.sin(phi))**2 * np.absolute(E)**2)) * A
    return a + b - c


# DEBUG
if __name__ == '__main__':
    # print(help(ECEF2LLA))
    u = np.array([10, "a", 30])
    x = ECEF2LLA(u)
    print(x)
