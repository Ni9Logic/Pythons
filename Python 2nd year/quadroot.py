import cmath
def quadroot(a,b,c):
    a = float(input("Enter Variable A: "))
    b = float(input("Enter Variable B: "))
    c = float(input("Enter Variable C: "))
    quad = ((-b + cmath.sqrt(pow(-b,2)-4*(a*c))))/2*a
    print("Quadratic Formula is: ", quad)
    return quad


a = b = c = 0
quadroot(a,b,c)