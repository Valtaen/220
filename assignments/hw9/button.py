"""
Yup, here's the button file. Use, don't abuse.
"""

from graphics import Text


class Button:

    """
    Doc strings for everyone! Possible functions:
    get_label(self), draw(self, win), undraw(self), is_clicked(self, point), color_button(self),
    and set_label(self)
    """

    def __init__(self, shape, label):
        self.shape = shape
        self.shape.label = label
        self.text = Text(self.shape.getCenter(), label)

    def get_label(self):
        return self.shape.label

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        x_coord = int(point.getX())
        y_coord = int(point.getY())
        point1 = self.shape.getP1()
        point1x = point1.getX()
        point1y = point1.getY()
        point2 = self.shape.getP2()
        point2x = point2.getX()
        point2y = point2.getY()
        return (int(point1x)) <= x_coord <= (int(point2x)) and \
            (int(point1y)) <= y_coord <= (int(point2y))

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text = Text(self.shape.getCenter(), label)
