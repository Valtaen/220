"""
Name: Matt stewart

lab7.py
"""
import math

def cash_conversion():
    num = eval(input("Enter an integer: "))
    print("$" + '{:.2f}'.format(num))

def encode():
    s = input('Enter your message: ')
    key = eval(input('Enter your key: '))
    acc = " "
    for r in s:
        x = ord(r)
        x = x + key
        acc = acc + chr(x)
    print(acc)

def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    print(area)

def sphere_volume(radius):
    volume = 4/3 * math.pi * (radius ** 3)
    print(volume)

def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    print(acc)
    return (acc)

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + i**3
    print(acc)
    return(acc)

def encode_better():
    s = input("Enter your message: ")
    k = input("Enter your key: ")
    acc= " "
    for i in range(len(s)):
        c = s[i]
        c = ord(c)
        key = k[i%len(k)]
        key = ord(key)-97
        c = c + key
        c = chr(c)
        acc = acc + c
    print(acc)

def main():
    cash_conversion()
    encode()
    sphere_area(n)
    sphere_volume(n)
    sum_n(n)
    sum_n_cubes(n)
    encode_better()
    pass


main()
