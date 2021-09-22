"""
Name: Matt Stewart
mean.py

Problem: Given user input, output a set of three means (RMS, harmonic, and geometric)

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def main():
    num = eval(input("Enter the number of values to be entered: "))
    rms_temp = 0
    harm_temp = 0
    geo_temp = 1
    tmp = 0
    for i in range(num):
        tmp = eval(input("Enter value " + str(i+1) + ": "))
        rms_temp = rms_temp + (tmp**2)
        harm_temp = harm_temp + (1 / tmp)
        geo_temp = geo_temp * tmp
    rms_mean = math.sqrt(rms_temp / num)
    harm_mean = num / harm_temp
    geo_mean = geo_temp ** (1 / num)
    print(round(rms_mean, 3))
    print(round(harm_mean, 3))
    print(round(geo_mean, 3))

if __name__ == '__main__':
    main()
