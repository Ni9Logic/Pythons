char = input('Enter a character: ')

if char == char.lower():
    newchar = char.upper()
    print("Converted to Upper Case: ", newchar)
else:
    newchar = char.lower()
    print("Converted to Lower Case: ", newchar)