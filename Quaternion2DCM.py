import numpy as np
import check


def Quaternion2DCM(quaternion):
    '''
    Calcul la matrice de passage DCM (Direct Cosine Matrix) à partir du quaternion q.

    Si q = q0+ q1 i + q2 j + q3 k alors

    DCM =
    [
    1-2q2^2-2q3^2    2q1q2-2q0q3     2q1q3+2q0q2
    2q1q2+2q0q3      1-2q1^2-2q3^2   2q2q3-2q0q1
    2q1q3-2q0q2      2q2q3+2q0q1     1-2q1^2-2q2^2
    ]
    '''
    check.vecteur_n(4, quaternion, "bloc outils/Quaternion2DCM")

    q = quaternion

    dcm = np.empty([3, 3])
    dcm[0][0] = 1 - 2 * q[2]**2 - 2 * q[3]**2
    dcm[1][0] = 2 * q[1] * q[2] + 2 * q[0] * q[3]
    dcm[2][0] = 2 * q[1] * q[3] - 2 * q[0] * q[2]

    dcm[0][1] = 2 * q[1] * q[2] - 2 * q[0] * q[3]
    dcm[1][1] = 1 - 2 * q[1]**2 - 2 * q[3]**2
    dcm[2][1] = 2 * q[2] * q[3] + 2 * q[0] * q[1]

    dcm[0][2] = 2 * q[1] * q[3] + 2 * q[0] * q[2]
    dcm[1][2] = 2 * q[2] * q[3] - 2 * q[0] * q[1]
    dcm[2][2] = 1 - 2 * q[1]**2 - 2 * q[2]**2

    dcm = dcm.T
    return dcm


# DEBUG
if __name__ == '__main__':
    # print(help(Quaternion2DCM))
    e = np.array([0.4, -0.3, 1.3, 0.7])

    dcm = Quaternion2DCM(e)
    print(dcm)
