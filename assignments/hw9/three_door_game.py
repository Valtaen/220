"""
Name: Matt Stewart
three_door_game.py

Problem: Make a game that makes three buttons with one randomly being the "winning"
door for the user to select.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
from graphics import GraphWin, Point, Rectangle, Text
from button import Button


def playgame():
    win = GraphWin("Three Door Game", 600, 400)

    secret_door = randint(0, 2)

    door1 = Button(Rectangle(Point(60, 160), Point(200, 240)), "Door 1")
    door2 = Button(Rectangle(Point(230, 160), Point(370, 240)), "Door 2")
    door3 = Button(Rectangle(Point(400, 160), Point(540, 240)), "Door 3")
    doors = [door1, door2, door3]
    door = "Door " + str(secret_door + 1)

    door1.color_button("white")
    door2.color_button("white")
    door3.color_button("white")
    door1.draw(win)
    door2.draw(win)
    door3.draw(win)

    top = Text(Point(300, 40), "I have a secret door.")
    bottom = Text(Point(300, 360), "Click a button to choose a door.")
    top.draw(win)
    bottom.draw(win)

    check = 0
    while check == 0:
        user_click = win.getMouse()
        if door1.is_clicked(user_click):
            if door1 == doors[secret_door]:
                door1.color_button("green")
                win_text(top, bottom, win)
                check = 1
            else:
                door1.color_button("red")
                doors[secret_door].color_button("green")
                lose_text(top, bottom, win, door)
                check = 1
        elif door2.is_clicked(user_click):
            if door2 == doors[secret_door]:
                door2.color_button("green")
                win_text(top, bottom, win)
                check = 1
            else:
                door2.color_button("red")
                doors[secret_door].color_button("green")
                lose_text(top, bottom, win, door)
                check = 1
        elif door3.is_clicked(user_click):
            if door3 == doors[secret_door]:
                door3.color_button("green")
                win_text(top, bottom, win)
                check = 1
            else:
                door3.color_button("red")
                doors[secret_door].color_button("green")
                lose_text(top, bottom, win, door)
                check = 1


def win_text(top, bottom, win):
    top.undraw()
    top = Text(Point(300, 40), "You picked my door!")
    top.draw(win)
    bottom.undraw()
    bottom = Text(Point(300, 360), "Click to close.")
    bottom.draw(win)
    win.getMouse()
    win.close()


def lose_text(top, bottom, win, door):
    top.undraw()
    top = Text(Point(300, 40), "You lost!")
    top.draw(win)
    bottom.undraw()
    bottom = Text(Point(300, 360), str(door) + " was my secret door!")
    bottom.draw(win)
    win.getMouse()
    win.close()


def main():
    playgame()


if __name__ == '__main__':
    main()
