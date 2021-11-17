"""
Name: Matt stewart

lab7.py
"""
import math

def cash_conversion():
    num = eval(input("Enter an integer: "))
    print("$" + '{:.2f}'.format(num))

def encode(message, key):
    message = input('Enter your message: ')
    key = eval(input('Enter your key: '))
    acc = " "
    for r in message:
        x = ord(r)
        x = x + key
        acc = acc + chr(x)
    return(acc)

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

def encode_better(message, key):
    message = message.replace(" ", "")
    message = message.upper()
    key = key.replace(" ", "")
    key = key.upper()
    acc = ""
    for i in range(len(message)):
        m = ord(message[i])
        k = ord(key[i % len(key)])
        c = (m + k) % 26
        c = str(chr(ord('A') + c))
        acc = acc + c
    return"".join(acc)

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
