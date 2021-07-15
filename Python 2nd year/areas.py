def areasquare(length):
    length = float(input('Enter Length of any side in square: '))
    squarearea = 4 * length
    print("Area of Square is: ", squarearea)
    return squarearea
def area_rectange(length, width):
    length = float(input('Enter Length of Rectange: '))
    width = float(input('Enter width of Rectange: '))
    rectangearea = length * width
    print("Area of Rectange is: ", rectangearea)
    return rectangearea

length  = 0
areasquare(length)
width = 0
area_rectange(length, width)