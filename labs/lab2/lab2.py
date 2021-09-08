"""
Name: Matt Stewart
lab2.py

Problems: Various multiplication/area/etc. equations

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def sum_of_threes():
    bound = eval(input("Enter the upper bound: "))
    acc = 0
    for i in range(0,bound+1,3):
        acc=acc+i
    print(acc)

#sum_of_threes()


def multiplication_table():
    for h in range(1,11):
        for l in range(1,11):
            total=h*l
            print(total,end=" ")
        print()


#multiplication_table()


def triangle_area():
    import math
    a = eval(input("Enter the a side length: "))
    b = eval(input("Enter the b side length: "))
    c = eval(input("Enter the c side length: "))
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)

#triangle_area()

def sumSquares():
    l= eval(input("Enter the lower range: "))
    u= eval(input("Enter the upper range: "))
    acc=0
    for i in range(l,u+1):
        acc=acc+i**2
    print(acc)

#sumSquares()

def power():
    base= eval(input("Enter the base: "))
    exp= eval(input("Enter the exponent: "))
    acc=1
    for i in range(exp):
        acc=acc*base
    print(base, "^" ,exp, "=",acc)

power()

