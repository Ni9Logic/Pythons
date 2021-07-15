def swap(val1, val2):
    print("Before Swapping both values are:", val1, val2)
    temp = val2
    val2 = val1
    val1 = temp
    print("After Swapping both values are:", val1, val2)


val1 = 65
val2 = 75
swap(val1, val2)