"""
Name: Matt Stewart
lab5.py
"""

from graphics import *
from math import *

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    z = win_width
    r = win_width/10
    yellow_circ = Circle(Point(z/2, z/2), r)
    red_circ = Circle(Point(z/2, z/2), 2*r)
    blue_circ = Circle(Point(z/2, z/2), 3*r)
    black_circ = Circle(Point(z/2, z/2), 4*r)
    white_circ = Circle(Point(z/2, z/2), 5*r)

    white_circ.draw(win)
    white_circ.setFill("white")
    black_circ.draw(win)
    black_circ.setFill("black")
    blue_circ.draw(win)
    blue_circ.setFill("blue")
    red_circ.draw(win)
    red_circ.setFill("red")
    yellow_circ.draw(win)
    yellow_circ.setFill("yellow")

    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    a = win.getMouse()
    ax = a.getX()
    ay = a.getY()
    b = win.getMouse()
    bx = b.getX()
    by = b.getY()
    c = win.getMouse()
    cx = c.getX()
    cy = c.getY()

    tri = Polygon(Point(ax, ay), Point(bx,by), Point(cx,cy))
    tri.setFill("blue")
    tri.setOutline("blue")
    tri.draw(win)
    p1 = sqrt((ax-bx)**2 + (ay-by)**2)
    p2 = sqrt((bx-cx)**2 + (by-cy)**2)
    p3 = sqrt((cx-ax)**2 + (cy-ay)**2)
    perimeter = p1 + p2 + p3
    s = perimeter / 2
    area = sqrt(s*(s-p1)*(s-p2)*(s-p3))

    perim = Point(win_width / 2, 390)
    perim_print = Text(perim, "The perimeter is: " + str(perimeter))
    perim_print.draw(win)

    area1 = Point(win_width / 2, 370)
    area_print = Text(area1, "The area is: " + str(area))
    area_print.draw(win)

    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    blue_box = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_box = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    red_box.draw(win)
    blue_box.draw(win)
    green_box.draw(win)
    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        blue = int(blue_box.getText())
        green = int(green_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s = str(input("Enter a string here: "))
    print(s[0])
    print(s[-1])
    print(s[1:6])
    print(s[0] + s[-1])
    print(s[0-3]*10)
    for ch in s:
        print(ch)
    print("Number of characters: " + str(len(s)))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = str(values[1])
    print(x*5)
    new_values = [values[2], values[3], values[4]]
    print(new_values[:])
    new_values = [values[2], values[3], values[1]]
    print(new_values[:])
    new_values = [values[2], values[1], float(values[5])]
    print(new_values[:])
    print((values[0]+values[2]+float(values[5])))
    print(len(values))


def another_series():
    inputs = eval(input("Enter a number of terms to display and add: "))
    acc = 0
    for i in range(inputs):
        y = 2 + 2*(i%3)
        print(y, end=" ")
        acc = acc + y
    print("sum = " + str(acc))


def main():
    target()
    # triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_series()
    pass


main()

