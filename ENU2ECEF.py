import numpy as np
import check


class ENU2ECEF():
    def __init__(self, phi0=0, lmbda0=0, h0=0, a=6378137, b=6356752.3142, e=0.08181919092891):
        '''
        phi0 : Latitude de référence du repère TGL NED (deg)
        lmbda0 : Longitude de référence du repère TGL NED (deg)
        h0 : Altitude de référence du repère TGL NED (m)
        a : 1/2 grand axe equatorial de l'ellipsoïde
        b : 1/2 grand axe polaire de l'ellipsoïde
        e : Excentricité de l'ellipsoïde
        '''
        self.phi0 = phi0 * np.pi / 180
        self.lmbda0 = lmbda0 * np.pi / 180
        self.h0 = h0
        self.a = a
        self.b = b
        self.e = e

        self.input = []  # enu
        self.output = []  # ecef

    def __str__(self):
        print("=== bloc ENU2ECEF ===")
        print("Input :\n{}\nOutput :\n{}".format(self.input, self.output))
        return "=====================\n"

    def __calcul_xyz0(self):
        local_radius = self.a / np.sqrt(1 - np.absolute(self.e)**2 * np.absolute(np.sin(self.phi0))**2)
        _1_e2 = 1 - np.absolute(self.e)**2

        c1 = np.array([local_radius + self.h0,
                       local_radius + self.h0,
                       local_radius * _1_e2 + self.h0])

        c2 = np.array([np.cos(self.phi0) * np.cos(self.lmbda0),
                       np.cos(self.phi0) * np.sin(self.lmbda0),
                       np.sin(self.phi0)])

        return c1 * c2

    def __calcul_M_NED2ECEF(self):
        l1 = np.array([np.sin(self.phi0) * np.cos(self.lmbda0) * -1,
                       - np.sin(self.lmbda0),
                       np.cos(self.phi0) * np.cos(self.lmbda0) * -1])

        l2 = np.array([np.sin(self.phi0) * np.sin(self.lmbda0) * -1,
                       np.cos(self.lmbda0),
                       np.cos(self.phi0) * np.sin(self.lmbda0) * -1])

        l3 = np.array([np.cos(self.phi0),
                       0,
                       - np.sin(self.phi0)])

        return np.array([l1, l2, l3])

    def execute(self, enu):
        '''
        Transforme les coordonnées dans le repère ENU local 
        (East North Up) xyz= [m,m,m]  défini par le plan tangent 
        à l'ellipsoïde au point origine lla0 [rad,rad,m] et le 
        vecteur normal défini positivement suivant les altitudes 
        dans le repère ECEF (Earth Centered Earth Fixed).
        '''
        self.input = enu

        check.vecteur_n(3, enu, "bloc outils/xyz_ENU2ECEF")

        xyz0 = self.__calcul_xyz0()
        m_ned2ecef = self.__calcul_M_NED2ECEF()
        ned = np.array([self.input[1], self.input[0], -self.input[2]])

        self.output = xyz0 + m_ned2ecef.dot(ned)


# DEBUG
if __name__ == '__main__':
    # print(help(ENU2ECEF))

    enu = np.array([500, -600, 700])

    enu2ecef = ENU2ECEF(lmbda0=45)
    enu2ecef.execute(enu)

    print(enu2ecef)

    ecef = enu2ecef.output
