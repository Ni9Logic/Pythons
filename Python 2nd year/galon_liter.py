def inputgalon(galon):
    galon = (float(input('Enter amount of Galons: ')))
    liter = galon * 3.78541
    liter = float(liter)
    print(galon, "are counted as", liter, "many liters")
    return liter


galon = 0.0
inputgalon(galon)