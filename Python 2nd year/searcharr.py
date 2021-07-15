import random

def searcharr(arr):
    isFound = False
    arr = []
    for i in range(10):
        arr = random.randint(1, 40)

    print("\n")
    search = int(input("Enter The Integer you want to search: "))
    for i in range(10):
        if search == arr[i]:
            isFound = True
        else:
            isFound = False
    if isFound:
        print("The integer you searched for is present in the array\n")
    else:
        print("The integer you searched for is not present in the array\n")
    return isFound

arr = 0
searcharr(arr)