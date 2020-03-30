import numpy as np
import math
import check


def Quaternion2Euler(quaternion):
    '''
    Calcul des angles d'Euler (phi,theta,psi) à partir du quaternion q. 

    Si q = q0 + q1 i + q2 j + q3 k ,  alors

    phi = atan2( 2(q0q1+q2q3) , q0^2-q1^2 - q2^2+q3^2)
    theta = asin(2q0q2-2q1q3)
    psi = atan2( 2(q1q2+q0q3) , q0^2+q1^2 - q2^2-q3^2)
    '''
    check.vecteur_n(4, quaternion, "bloc outils/Quaternion2Euler")

    q = quaternion
    euler = np.empty(3)

    euler[0] = math.atan2(2 * (q[0] * q[1] + q[2] * q[3]), q[0]**2 - q[1]**2 - q[2]**2 + q[3]**2)
    euler[1] = math.asin(np.clip(2 * (q[0] * q[2] - q[1] * q[3]), -1, 1))
    euler[2] = math.atan2(2 * (q[1] * q[2] + q[0] * q[3]), q[0]**2 + q[1]**2 - q[2]**2 - q[3]**2)

    return euler


# DEBUG
if __name__ == '__main__':
    # print(help(Quaternion2Euler))
    e = np.array([0.4, -0.3, 1.3, 0.7])

    euler = Quaternion2Euler(e)
    print(euler)
