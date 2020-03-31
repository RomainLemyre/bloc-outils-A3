import numpy as np

import check
from Euler2Quaternion import Euler2Quaternion
from norme import norme


class pqr2Quaternion():
    def __init__(self, euler0=np.array([0, 0, 0]), time_step=0.1):
        '''
        euler0 : Angles d'Euler initiaux (deg)
        '''
        self.euler0 = euler0 * np.pi / 180
        self.time_step = time_step
        self.time = -1

        self.int_xdot = []
        self.int_x = Euler2Quaternion(self.euler0)

        self.input = []
        self.output = []

    def __str__(self):
        print("=== bloc pqr2Quaternion ===")
        print("Time : {}\nInput :\n{}\nOutput :\n{}".format(self.time, self.input, self.output))
        return "=====================\n"

    def __pqr2eidot(self):
        e_i = self.output
        u = np.empty(8)
        u[:3] = self.input
        u[3:-1] = e_i
        u[-1] = (1 - (e_i[0]**2 + e_i[1]**2 + e_i[2]**2 + e_i[3]**2)) * 100

        eidot = np.empty(4)
        eidot[0] = -0.5 * (u[4] * u[0] + u[5] * u[1] + u[6] * u[2])
        eidot[1] = 0.5 * (u[3] * u[0] + u[5] * u[2] - u[6] * u[1])
        eidot[2] = 0.5 * (u[3] * u[1] + u[6] * u[0] - u[4] * u[2])
        eidot[3] = 0.5 * (u[3] * u[2] + u[4] * u[1] - u[5] * u[0])
        return eidot

    def __integrator(self, eidot):
        self.int_x += self.int_xdot * self.time_step
        self.int_xdot = eidot
        return self.int_x

    def execute(self, euler):
        '''
        Calcul du quaternion à partir des vitesses de rotation du missile et de 
        l'attidude initiale du missile.
        '''
        self.input = euler
        check.vecteur_n(3, euler, "bloc outils/pqr2Quaternion")

        if self.time != -1:
            eidot = self.__pqr2eidot()
            y = self.__integrator(eidot)
            self.output = y / norme(y)

            eidot = self.__pqr2eidot()
            self.int_xdot = eidot

            self.time += self.time_step
        else:
            self.output = self.int_x / norme(self.int_x)
            eidot = self.__pqr2eidot()
            self.int_xdot = eidot
            self.time = 0


# DEBUG
if __name__ == '__main__':
    # print(help(pqr2Quaternion))
    pqr = np.array([10, 20, 30])

    pqr2quaternion = pqr2Quaternion()

    temps = 100
    for i in range(temps + 1):

        pqr2quaternion.execute(pqr)
        print(pqr2quaternion)

    quaternion = pqr2quaternion.output
