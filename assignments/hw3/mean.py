"""
Name: Matt Stewart
mean.py

Problem: Given user input, output a set of three means (RMS, harmonic, and geometric)

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def main():
    n = eval(input("Enter the number of values to be entered: "))
    rms_temp = 0
    harm_temp = 0
    geo_temp = 1
    tmp = 0
    for i in range(n):
        tmp = eval(input("Enter value " + str(i+1) + ": "))
        rms_temp = rms_temp + (tmp**2)
        harm_temp = harm_temp + (1 / tmp)
        geo_temp = geo_temp * tmp
    rms_mean = math.sqrt(rms_temp / n)
    harm_mean = n / harm_temp
    for i in range(1,n-1):
        geo_temp = math.sqrt(geo_temp)
"""
RMS= sqrt of arithmetic mean of squares of n inputs, should be 6.205
#harmonic mean = 1 divided by sum of 1/n1+1/n2+1/n3+etc, should be 4.0
#geometric mean = nth root of the sum product of n, should be 4.729
"""
    print(round(rms_mean, 3))
    print(round(harm_mean, 3))
    print(round(geo_temp, 3))

if __name__ == '__main__':
    main()
