"""
Name: Matt Stewart
bumper.py

Problem: Create two circles that move about a window and change direction on impact with
the wall or each other.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
import time
from random import randint
from graphics import GraphWin, Circle, Point, color_rgb


def get_random(move):
    return randint(-move, move)


def did_collide(circle1, circle2):
    cen = circle1.getCenter()
    cen2 = circle2.getCenter()
    distance = math.sqrt((cen2.getX() - cen.getX()) ** 2 + (cen2.getY() - cen.getY()) ** 2)
    return bool(distance <= (circle1.getRadius() + circle2.getRadius()))


def hit_vertical(circle, win):
    cen = circle.getCenter()
    ceny = float(cen.getY())
    return bool(ceny <= circle.getRadius() or ceny >= win.getHeight() - circle.getRadius())


def hit_horizontal(circle, win):
    cen = circle.getCenter()
    cenx = float(cen.getX())
    return bool(cenx <= circle.getRadius() or cenx >= win.getWidth() - circle.getRadius())


def get_random_color(circle):
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    circle.setFill(color_rgb(red, green, blue))


def main():
    win = GraphWin("Bumper Car Demo", 600, 400)

    rad1 = randint(40, 60)
    rad2 = randint(20, 40)

    circle1 = Circle(Point(200, 180), rad1)
    circle2 = Circle(Point(300, 340), rad2)
    get_random_color(circle1)
    get_random_color(circle2)
    circle1.draw(win)
    circle2.draw(win)

    movex = get_random(20)
    movey = get_random(20)
    move2x = get_random(20)
    move2y = get_random(20)

    g2g = 1
    while g2g == 1:
        circle1.move(movex, movey)
        circle2.move(move2x, move2y)
        time.sleep(0.02)
        if hit_horizontal(circle1, win):
            movex = -movex
        if hit_vertical(circle1, win):
            movey = -movey
        if hit_horizontal(circle2, win):
            move2x = -move2x
        if hit_vertical(circle2, win):
            move2y = -move2y
        if did_collide(circle1, circle2):
            movex, movey = -movex, -movey
            move2x, move2y = -move2x, -move2y


if __name__ == '__main__':
    main()
