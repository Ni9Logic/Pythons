with open("Testing.txt", "r") as file:
    data = file.read()
    print(data)
file.close()

with open("Testing.txt", "a") as file:
    data = input("Add more text: ")
    file.write("\n")
    file.write(data)
file.close()

with open("Testing.txt", "r") as file:
    data = file.read()
    print(data)
file.close()