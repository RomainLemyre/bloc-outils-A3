import numpy as np

from ECEF2LLA import ECEF2LLA
from ENU2ECEF import ENU2ECEF
from Euler2DCM import Euler2DCM
from Euler2Quaternion import Euler2Quaternion
from Inert2Miss import Inert2Miss
from NED2LLA import NED2LLA
from norme import norme
from Quaternion2DCM import Quaternion2DCM
from Quaternion2Euler import Quaternion2Euler
from vectoriel import vectoriel


# DEBUG
if __name__ == '__main__':
    u = np.array([1, 2, 3])
    v = np.array([4, 5, 6])
    print("u : {}\nv : {}".format(u, v))

    vect = vectoriel(u, v)
    print("u vect v : {}".format(vect))

    norm_u = norme(u)
    print("norm(u) : {}".format(norm_u))

    print("\n===\n")

    euler = np.array([2.8, -1.5, 0.7])
    print("Euler : {}".format(euler))

    quaternion = Euler2Quaternion(euler)
    print("to quaternion : {}".format(quaternion))

    euler = Quaternion2Euler(quaternion)
    print("to euler : {}".format(euler))

    dcm = Euler2DCM(euler)
    print("to dcm :\n{}".format(dcm))

    dcm = Quaternion2DCM(quaternion)
    print("quaternion to dcm :\n{}".format(dcm))

    print("\n===\n")

    inert = np.array([100, -200, 600])
    print("inert : {}\neuler : {}\n".format(inert, euler))

    miss = Inert2Miss(euler, inert)
    print("inert to miss : {}\n".format(miss))

    ned = np.array([-400, 100, 800])
    print("NED : {}".format(ned))

    ned2lla = NED2LLA()
    ned2lla.execute(ned)
    lla = ned2lla.output
    print("NED to LLA : {}\n".format(lla))

    enu = np.array([600, -300, 700])
    print("ENU : {}".format(enu))

    enu2ecef = ENU2ECEF()
    enu2ecef.execute(enu)
    ecef = enu2ecef.output
    print("to ECEF : {}".format(ecef))

    ecef2lla = ECEF2LLA()
    ecef2lla.execute(ecef)
    lla = ecef2lla.output
    print("to LLA : {}".format(lla))
