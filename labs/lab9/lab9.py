"""
Name: Matt Stewart
lab9.py
"""

import math
from graphics import *

def addTen(x):
    for i in range(len(x)):
        x[i] = int(x[i]) + 10

def squareEach(x):
    for i in range(len(x)):
        x[i] = (x[i])**2

def sumList(x):
    acc = 0
    for i in range(len(x)):
        acc = acc + x[i]
    return acc

def toNumbers(x):
    for i in range(len(x)):
        x[i] = float(int(x[i]))

def writeSumOfSquares():
    inf = input("Enter the file name: ")
    infile = open(inf, "r")
    outfile = open("herpyderpy.txt", "w")
    for line in infile:
        intLine = line
        intLine = intLine.split(" ")
        toNumbers(intLine)
        squareEach(intLine)
        acc2 = sumList(intLine)
        outfile.write("sum = " + str(acc2) + "\n")

def starter():
    weight = eval(input("Enter the player's weight: "))
    numWins = eval(input("Enter the player's number of wins: "))
    if (weight >= 150 and weight <= 160) and numWins >= 5:
        print("This player should start.")
    elif weight >= 199 or numWins > 20:
        print("This player should start.")
    else:
        print("This player should not start.")

def leapYear(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " is not a leap year")

def circleOverlap():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    cen1 = win.getMouse()
    x = cen1.getX()
    y = cen1.getY()
    rad = win.getMouse()
    xx = rad.getX()
    yy = rad.getY()
    r = (abs(xx - x) ** 2) + (abs(yy - y)**2)
    r2 = math.sqrt(r)
    circ = Circle(Point(x, y), r2)
    circ.setFill("blue")
    circ.draw(win)

    cen2 = win.getMouse()
    x2 = cen2.getX()
    y2 = cen2.getY()
    rad2 = win.getMouse()
    xx2 = rad2.getX()
    yy2 = rad2.getY()
    r3 = (abs(xx2 - x2) ** 2) + (abs(yy2 - y2)**2)
    r4 = math.sqrt(r3)
    circ2 = Circle(Point(x2, y2), r4)
    circ2.setFill("red")
    circ2.draw(win)

    distance = math.sqrt((x2 - x)**2 + (y2 - y)**2)
    rTogether = r2 + r4

    if distance >= rTogether:
        print("The circles do not overlap.")
    else:
        print("The circles overlap.")

    win.getMouse()
    win.close()


def main():
    x = [1, 2, 3]
    #squareEach(x)
    #sumList(x)
    #toNumbers(x)
    #writeSumOfSquares()
    starter()
    #leapYear(2004)
    #circleOverlap()
    pass


main()