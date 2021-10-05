"""
Name: Matt Stewart
greeting.py

Problem: Create a greeting card w/a heart and shooting arrow

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import time
from graphics import GraphWin, Circle, Point, Polygon, Rectangle, Text, color_rgb

# modified import because linting was yelling at me for unused imports >_>
# make heart shape with...two small circles and inverted triangle?
# arrow as right-facing triangle with rectangles for shaft/fletching


def main():
    win = GraphWin("Happy Valentine's Day!", 1200, 800)
    win.setBackground("white")

    #two circles and a triangle to make the heart shape
    left_arch = Circle(Point(820, 400), 100)
    right_arch = Circle(Point(980, 400), 100)
    bottom = Polygon(Point(900, 625), Point(740, 460), Point(1060, 460))
    left_arch.setFill("pink")
    left_arch.setOutline("pink")

    right_arch.setFill("pink")
    right_arch.setOutline("pink")

    bottom.setFill("pink")
    bottom.setOutline("pink")

    left_arch.draw(win)
    right_arch.draw(win)
    bottom.draw(win)

    arrow_head = Polygon(Point(295, 440), Point(260, 460), Point(260, 420))
    arrow_head.setFill("silver")
    arrow_head.setOutline("silver")
    arrow_head.draw(win)

    arrow_shaft = Rectangle(Point(10, 435), Point(260, 445))
    arrow_shaft.setFill(color_rgb(150, 75, 0))
    arrow_shaft.setOutline(color_rgb(150, 75, 0))
    arrow_shaft.draw(win)
    #three rows of leaning-back parallelograms on top and bottom
    fletch1 = Polygon(Point(10, 435), Point(2, 415), Point(10, 415), Point(18, 435))
    fletch2 = Polygon(Point(18, 435), Point(10, 415), Point(18, 415), Point(26, 435))
    fletch3 = Polygon(Point(26, 435), Point(18, 415), Point(26, 415), Point(34, 435))
    fletch4 = Polygon(Point(10, 445), Point(2, 465), Point(10, 465), Point(18, 445))
    fletch5 = Polygon(Point(18, 445), Point(10, 465), Point(18, 465), Point(26, 445))
    fletch6 = Polygon(Point(26, 445), Point(18, 465), Point(26, 465), Point(34, 445))
    #adding more fletchings because it looks funny otherwise
    fletch7 = Polygon(Point(34, 435), Point(26, 415), Point(34, 415), Point(42, 435))
    fletch8 = Polygon(Point(42, 435), Point(34, 415), Point(42, 415), Point(50, 435))
    fletch9 = Polygon(Point(34, 445), Point(26, 465), Point(34, 465), Point(42, 445))
    fletch10 = Polygon(Point(42, 445), Point(34, 465), Point(42, 465), Point(50, 445))

    #alternating red/pink fletching!
    fletch1.setFill(color_rgb(255, 0, 0))
    fletch1.setOutline(color_rgb(255, 0, 0))
    fletch1.draw(win)

    fletch2.setFill("pink")
    fletch2.setOutline("pink")
    fletch2.draw(win)

    fletch3.setFill(color_rgb(255, 0, 0))
    fletch3.setOutline(color_rgb(255, 0, 0))
    fletch3.draw(win)

    fletch4.setFill(color_rgb(255, 0, 0))
    fletch4.setOutline(color_rgb(255, 0, 0))
    fletch4.draw(win)

    fletch5.setFill("pink")
    fletch5.setOutline("pink")
    fletch5.draw(win)

    fletch6.setFill(color_rgb(255, 0, 0))
    fletch6.setOutline(color_rgb(255, 0, 0))
    fletch6.draw(win)

    fletch7.setFill("pink")
    fletch7.setOutline("pink")
    fletch7.draw(win)

    fletch8.setFill(color_rgb(255, 0, 0))
    fletch8.setOutline(color_rgb(255, 0, 0))
    fletch8.draw(win)

    fletch9.setFill("pink")
    fletch9.setOutline("pink")
    fletch9.draw(win)

    fletch10.setFill(color_rgb(255, 0, 0))
    fletch10.setOutline(color_rgb(255, 0, 0))
    fletch10.draw(win)

    #So I can have the arrow drawn at the start and have it reveal around the hider
    hider = Rectangle(Point(1, 410), Point(300, 470))
    hider.setFill("white")
    hider.setOutline("white")
    hider.draw(win)

    #Make a frame to make the "card" and make it look like the arrow's being shot in
    frame_top = Rectangle(Point(300, 20), Point(1100, 30))
    frame_bottom = Rectangle(Point(300, 770), Point(1100, 780))
    frame_left = Rectangle(Point(300, 20), Point(310, 780))
    frame_right = Rectangle(Point(1090, 20), Point(1100, 780))
    frame_top.setFill("black")
    frame_bottom.setFill("black")
    frame_left.setFill("black")
    frame_right.setFill("black")
    frame_top.draw(win)
    frame_bottom.draw(win)
    frame_left.draw(win)
    frame_right.draw(win)

    #and another hider inside the heart so it can be "shot"
    heart_hider = Rectangle(Point(910, 465), Point(1000, 415))
    heart_hider.setFill("pink")
    heart_hider.setOutline("pink")
    heart_hider.draw(win)

    #What's a greeting card without a greeting?
    greet = Text(Point(700, 60), "Happy Valentine's Day!")
    greet.setFill("red")
    greet.setOutline("red")
    greet.setSize(30)
    greet.draw(win)

    #Now to 'shoot' the arrow...
    win.getMouse()
    for _ in range(55):
        arrow_head.move(12, 0)
        arrow_shaft.move(12, 0)
        fletch1.move(12, 0)
        fletch2.move(12, 0)
        fletch3.move(12, 0)
        fletch4.move(12, 0)
        fletch5.move(12, 0)
        fletch6.move(12, 0)
        fletch7.move(12, 0)
        fletch8.move(12, 0)
        fletch9.move(12, 0)
        fletch10.move(12, 0)
        time.sleep(0.005)

    close = Text(Point(700, 740), "Click anywhere to close")
    close.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
