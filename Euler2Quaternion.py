import numpy as np
import check


def Euler2Quaternion(euler):
    '''
    Calcul du quaternion q à partir des angles d'Euler (phi,theta,psi)

    q = q0 + q1 i + q2 j + q3 k
    avec :

    q0 = cos(0.5*psi)cos(0.5*theta)cos(0.5*phi) + sin(0.5*psi)sin(0.5*theta)sin(0.5*phi)
    q1 =  sin(0.5*psi)cos(0.5*theta)cos(0.5*phi) - cos(0.5*psi)sin(0.5*theta)sin(0.5*phi)
    q2 =  cos(0.5*psi)sin(0.5*theta)cos(0.5*phi) + sin(0.5*psi)cos(0.5*theta)sin(0.5*phi)
    q3 =  cos(0.5*psi)cos(0.5*theta)sin(0.5*phi) - sin(0.5*psi)sin(0.5*theta)cos(0.5*phi)
    '''
    check.vecteur_n(3, euler, "bloc outils/Euler2Quaternion")

    phi = euler[0]
    theta = euler[1]
    psi = euler[2]

    u = np.empty(6)
    u[0] = np.sin(phi / 2)
    u[1] = np.cos(phi / 2)
    u[2] = np.sin(theta / 2)
    u[3] = np.cos(theta / 2)
    u[4] = np.sin(psi / 2)
    u[5] = np.cos(psi / 2)

    quaternion = np.empty(4)
    quaternion[0] = u[1] * u[3] * u[5] + u[0] * u[2] * u[4]
    quaternion[1] = u[0] * u[3] * u[5] - u[1] * u[2] * u[4]
    quaternion[2] = u[1] * u[2] * u[5] + u[0] * u[3] * u[4]
    quaternion[3] = u[1] * u[3] * u[4] - u[0] * u[2] * u[5]

    return quaternion


# DEBUG
if __name__ == '__main__':
    # print(help(Euler2Quaternion))
    e = np.array([0.4, -0.3, 1.3])

    quaternion = Euler2Quaternion(e)
    print(quaternion)
