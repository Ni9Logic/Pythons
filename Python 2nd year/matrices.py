def makematrix(*
o[u;ijh'9lg0i matrix):
    n_rows = int(input("Number of rows:"))
    n_columns = int(input("Number of columns:"))
    #Define the matrix
    matrix = []
    print("Enter the entries row-wise:")
    #for user input
    for i in range(n_rows):          # A for loop for row entries
        a =[]
        for j in range(n_columns):      # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)
    #To print the matrix
    for i in range(n_rows):
        for j in range(n_columns):
            print(matrix[i][j], end = " ")
        print()