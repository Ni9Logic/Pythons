str = "Hello World I love you 123"
digits = []
for i in range(len(str)):
    if str[i] >= 'a' and str[i] <= 'z':
        continue
    elif str[i] >= 'A' and str[i] <= 'Z':
        continue
    else:
        for i in range(len(str)):
            if str[i] >= '0' and str[i] <= '10':
                digits = i
        str[i].replace(digits, " ")