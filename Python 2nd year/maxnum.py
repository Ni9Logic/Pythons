def max_num():
    variables_3 = input('Enter Three Variables using spaces: ')
    print("\n")
    variables_list = variables_3.split()
    print("Variables you have entered are: ", variables_list)
    for i in range(len(variables_list)):
       variables_list[i] = int(variables_list[i])
    maxi = variables_list[0]
    for i in range(len(variables_list)):
        if maxi < variables_list[i]:
            maxi = variables_list[i]
    print("Max Number is: ", maxi)
    return maxi

max_num()