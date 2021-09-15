"""
Name: Matt Stewart
lab3.py

Problem: Find average of inputs, total donations, sequences, and
approximations of the value of pi

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    hw = eval(input("Enter the number of homeworks you're entering: "))
    hw_total = 0
    for i in range(hw):
        tmp = eval(input("Enter your grade on HW " + str(i+1) + ": "))
        hw_total = tmp + hw_total
    avg = hw_total / hw
    print("Your average grade is ", avg)

#average()


def tip_jar():
    total_tip = 0
    for i in range(0, 5):
        tip = eval(input("Enter your tip amount: "))
        total_tip = total_tip + tip
    print("The total tip amount is", total_tip)

#tip_jar()


def newton():
    root = eval(input("Enter the number you wish to approximate the square root of: "))
    approx = eval(input("How many times do you want to improve the approximation? "))
    acc = root/2
    for i in range(0, approx):
        acc = (acc + (root/acc)) / 2
    print("With", root, "as the base, the approximation is", acc)

#newton()


def sequence():
    terms = eval(input("Enter the number of terms in the series: "))
    for i in range(1, terms+1):
        y = 1 + ((i//2) * 2)
        print(y, end=" ")

#sequence()


def pi():
    terms = eval(input("Enter the number of terms in the series: "))
    acc = 2
    for i in range(0, terms+1):
        numer = 2 + ((i//2) * 2)
        denom = 1 + (((i+1)//2) * 2)
        acc = acc * (numer / denom)
    print(acc)

pi()
