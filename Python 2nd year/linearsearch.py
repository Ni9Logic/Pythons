list = input('Enter but with spaces: ')
listarr = list.split()

for i in range(len(listarr)):
    listarr[i] = int(listarr[i])

search = input("Enter the number you want to search for in an array: ")
search = int(search)

imatch = 0
value = False
for i in range(len(listarr)):
    if search == listarr[i]:
            imatch = i
            value = True
            
if value == True:
    print("Your Value is found at index", imatch)
else:
    print("Your value is not found at any index")
    print(listarr)