import numpy as np

import check
from ENU2ECEF import ENU2ECEF
from ECEF2LLA import ECEF2LLA


class NED2LLA():
    def __init__(self, lla_ref=np.array([0, 0, 0]), ellipsoide=np.array([6378137, 6356752.3142, 0.08181919092891])):
        self.lla_ref = lla_ref
        self.ellipsoide = ellipsoide

        self.input = []  # ned
        self.output = []  # lla

    def __str__(self):
        print("=== bloc NED2LLA ===")
        print("Input :\n{}\nOutput :\n{}".format(self.input, self.output))
        return "====================\n"

    def execute(self, ned):
        '''
        Calcul les coordonnées LLA (latitude, longitude, altitude) à 
        partir des coordonnées xyz exprimées dans le repère NED 
        (North, East, Down) dont l'origine du repère est définit par une 
        position LLA de référence.
        '''
        self.input = ned

        check.vecteur_n(3, self.input, "bloc outils/NED2LLA")

        enu = np.array([self.input[1], self.input[0], -self.input[2]])

        enu2ecef = ENU2ECEF(self.lla_ref[0], self.lla_ref[1], self.lla_ref[2], self.ellipsoide[0], self.ellipsoide[1], self.ellipsoide[2])
        enu2ecef.execute(enu)

        ecef2lla = ECEF2LLA(self.ellipsoide[0], self.ellipsoide[1], self.ellipsoide[2])
        ecef2lla.execute(enu2ecef.output)

        self.output = ecef2lla.output


# DEBUG
if __name__ == '__main__':
    # print(help(NED2LLA))

    ned = np.array([50, -123, 502])

    ned2lla = NED2LLA()
    ned2lla.execute(ned)

    print(ned2lla)

    lla = ned2lla.output
