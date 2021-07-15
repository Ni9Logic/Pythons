def sorting(sort_list):
    sort = input('Enter Integers but using space: ')
    print("\n")
    sort_list = sort.split()
    for i in range(len(sort_list)):
        sort_list[i] = int(sort_list[i])

    for i in range(len(sort_list)):
        temp = 0
        for j in range(i+1, len(sort_list)):
            if sort_list[i] > sort_list[j]:
                temp = sort_list[i]
                sort_list[i] = sort_list[j]
                sort_list[j] = temp 

    print("Sorted list is: ", sort_list)
    return sort_list

sort_list = 0
sorting(sort_list)