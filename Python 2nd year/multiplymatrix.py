import numpy as np

def multiplymatrix(mat1, mat2):
        mat1 = [[12,13,15],
                [44,55,16],
                [37,68,89]]

        mat2 = [[10,11,12],
                [13,14,15],
                [16,17,18]]

        matresult = np.dot(mat1, mat2)

        print(matresult)
        return matresult

mat1 = mat2 = 0
multiplymatrix(mat1, mat2)
