MATRIX_A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

MATRIX_B = [[10,11,12],
     [13,14,15],
     [16,17,18]]

MATRIX_RESULT = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(MATRIX_A)):
    for j in range(len(MATRIX_A[0])):
        MATRIX_RESULT[i][j] = MATRIX_A[i][j] + MATRIX_B[i][j]

for r in MATRIX_RESULT:
    print(r)
