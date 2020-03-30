import numpy as np
import check


def Euler2DCM(euler):
    '''
    Calcul la matrice de passage DCM (Direct Cosine Matrix) à partir des angles d'Euler.

    DCM =
    [
    c(theta)c(psi)    -c(phi)s(psi)+s(phi)s(theta)c(psi)    s(phi)s(psi)+c(phi)s(theta)c(psi)

    c(theta)s(psi)    c(phi)c(psi)+s(phi)s(theta)s(psi)     -s(phi)c(psi)+c(phi)s(theta)s(psi)

    -s(theta)         s(phi)c(theta)                        c(phi)c(theta)
    ]^T
    où c correspond à cos,  et s correspond à sin
    '''
    check.vecteur_n(3, euler, "bloc outils/Euler2DCM")

    phi = euler[0]
    theta = euler[1]
    psi = euler[2]

    u = np.empty(6)
    u[0] = np.sin(phi)
    u[1] = np.cos(phi)
    u[2] = np.sin(theta)
    u[3] = np.cos(theta)
    u[4] = np.sin(psi)
    u[5] = np.cos(psi)

    dcm = np.empty([3, 3])
    dcm[0][0] = u[3] * u[5]
    dcm[1][0] = u[3] * u[4]
    dcm[2][0] = -u[2]

    dcm[0][1] = -u[1] * u[4] + u[0] * u[2] * u[5]
    dcm[1][1] = u[1] * u[5] + u[0] * u[2] * u[4]
    dcm[2][1] = u[0] * u[3]

    dcm[0][2] = u[0] * u[4] + u[1] * u[2] * u[5]
    dcm[1][2] = -u[0] * u[5] + u[1] * u[2] * u[4]
    dcm[2][2] = u[1] * u[3]

    dcm = dcm.T
    return dcm


# DEBUG
if __name__ == '__main__':
    # print(help(Euler2DCM))
    e = np.array([0.4, -0.3, 1.3])

    dcm = Euler2DCM(e)
    print(dcm)
