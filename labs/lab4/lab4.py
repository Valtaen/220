"""
Name: Matt Stewart
lab4.py

Problem: Various area, radius, and pi functions

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to set a square, then click to add squares")
    instructions.draw(win)

    # builds a square
    cen = win.getMouse()
    shape = Rectangle(Point(cen.getX()-10, cen.getY()-10), Point(cen.getX()+10,cen.getY()+10))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to copy the square
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() -10), Point(p.getX() + 10, p.getY() +10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to close the window.")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p1, p2)
    r.setOutline("blue")
    r.setFill("blue")
    r.draw(win)
    l = abs(p1.getX() - p2.getX())
    w = abs(p1.getY() - p2.getY())
    area = l * w
    perimeter = 2*(l + w)

    inst_pt = Point(width / 2, 390)
    instructions = Text(inst_pt, "The area is: " + str(area))
    instructions.draw(win)

    inst_pt = Point(width / 2, 370)
    instructions = Text(inst_pt, "The perimeter is: " + str(perimeter))
    instructions.draw(win)

    win.getMouse()
    win.close()

    pass


def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    cen = win.getMouse()
    x = cen.getX()
    y = cen.getY()
    rad = win.getMouse()
    xx = rad.getX()
    yy = rad.getY()
    r = (abs(xx - x) ** 2) + (abs(yy - y)**2)
    r2 = math.sqrt(r)
    circ = Circle(Point(x, y), r2)
    circ.setFill("green")
    circ.draw(win)



    inst_pt = Point(width / 2, 370)
    instructions = Text(inst_pt, "The radius is: " + str(r2))
    instructions.draw(win)

    win.getMouse()
    win.close()


    pass

def pi2():
    n = eval(input("Enter the number of terms to sum: "))
    acc = 0
    for i in range(n):
        num = 4
        den = 1 + 2*i
        frac = (num/den)*((-1)**i)
        acc = acc + frac
    print(acc)
    print(math.pi - acc)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
