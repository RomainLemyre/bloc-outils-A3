import numpy as np
import math

import check
from norme import norme


class ECEF2LLA():
    def __init__(self, a=6378137, b=6356752.3142, e=0.08181919092891):
        '''
        a : 1/2 grand axe equatorial de l'ellipsoïde
        b : 1/2 grand axe polaire de l'ellipsoïde
        e : Excentricité de l'ellipsoïde
        '''
        self.a = a
        self.b = b
        self.e = e

        self.input = []  # ecef
        self.output = []  # lla

    def __str__(self):
        print("=== bloc ECEF2LLA ===")
        print("Input :\n{}\nOutput :\n{}".format(self.input, self.output))
        return "=====================\n"

    def __calcul_r(self):
        return norme(self.input[:2])

    def __calcul_longitude(self):
        return math.atan2(self.input[1], self.input[0])

    def __calcul_latitude(self, r):
        mu = self.__calcul_mu(r)
        num_phi = self.__calcul_numPhi(mu)
        den_phi = self.__calcul_denPhi(mu, r)
        return math.atan2(num_phi, den_phi)

    def __calcul_mu(self, r):
        return math.atan2(self.input[2], r * (1 - self.__f()))

    def __f(self):
        return 1 - np.sqrt(1 - np.absolute(self.e)**2)

    def __calcul_numPhi(self, mu):
        return np.sin(mu)**3 * self.b * np.absolute(self.e)**2 + self.input[2]

    def __calcul_denPhi(self, mu, r):
        return r - np.cos(mu)**3 * self.a * np.absolute(self.e)**2

    def __calcul_h(self, phi, r):
        a = r * np.cos(phi)
        b = self.input[2] * np.sin(phi)
        c = np.sqrt(1 - (np.absolute(np.sin(phi))**2 * np.absolute(self.e)**2)) * self.a
        return a + b - c

    def execute(self, ecef):
        '''
        Transforme les coordonnées dans le repère ECEF (Earth-Centered
        Earth Fixed)  [m,m,m] en coordonnées géographiques LLA
        [rad,rad,m] par rapport à l'ellipsoïde de référence)
        '''
        self.input = ecef

        check.vecteur_n(3, self.input, "bloc outils/ECEF2LLA")

        r = self.__calcul_r()
        phi = self.__calcul_latitude(r)
        lmbda = self.__calcul_longitude()
        h = self.__calcul_h(phi, r)

        self.output = np.array([phi, lmbda, h])


# DEBUG
if __name__ == '__main__':
    # print(help(ECEF2LLA))

    ecef = np.array([100, -200, 300])

    ecef2lla = ECEF2LLA()
    ecef2lla.execute(ecef)

    print(ecef2lla)

    lla = ecef2lla.output
