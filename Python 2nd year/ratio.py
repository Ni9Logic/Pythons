variables = input('Enter Two Variables by space: ')
print("\n")
variables_list = variables.split()

print('Two Variables are', variables_list)

for i in range(len(variables_list)):
    variables_list[i] = int(variables_list[i])

ratio = variables_list[0]/variables_list[1]
print("Ratio = ", ratio)