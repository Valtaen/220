"""
Name: Matt Stewart
threeDoorGame.py

Problem: Make a game that makes three buttons with one randomly being the "winning"
door for the user to select.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from button import Button
from graphics import GraphWin, Point, Rectangle, Text


def playgame():
    win = GraphWin("Three Door Game", 600, 400)

    button1 = Button(Rectangle, "Door 1")
    button2 = Button(Rectangle, "Door 2")
    button3 = Button(Rectangle, "Door 3")

    button1.color_button("green")
    button2.color_button("red")
    button3.color_button("purple")

    button1.draw(win)
    button2.draw(win)
    button3.draw(win)

    win.getMouse()
    win.close()

def main():
    playgame()


if __name__ == '__main__':
    main()
