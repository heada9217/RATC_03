import math

from numpy import round_



def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return ((math.floor(n*multiplier + 0.5)) / multiplier)



for item in range(0,4):

    angle = float(input("Angle: "))

    decimal = int(input("How many decimal places do you want?: "))
    
    rounded_value = round_half_up(angle, decimal)
    print("rounded angle: {}".format(rounded_value))

    print()

