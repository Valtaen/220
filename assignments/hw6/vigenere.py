"""
Name: Matt Stewart
vigenere.py

Problem: Design a GUI Vigenere cipher program.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *

def code(message, key):
    message = message.replace(" ", "")
    message = message.upper()
    key = key.replace(" ", "")
    key = key.upper()
    acc = ""
    for i in range(len(message)):
        m = ord(message[i])
        k = ord(key[i % len(key)])
        c = (m + k) % 26
        c = str(chr(ord('A') + c))
        acc = acc + c
    return("".join(acc))

def main():
    win = GraphWin("Vigenere (But Really Bellaso) Cipher", 800, 400)
    win.setBackground("white")

    message_text = Text(Point(200, 40), "Enter Message")
    message_text.draw(win)
    key_text = Text(Point(200, 70), "Enter Key")
    key_text.draw(win)

    message_box = Entry(Point(490, 40), 40)
    key_box = Entry(Point(400, 70), 20)
    message_box.draw(win)
    key_box.draw(win)

    encode_button = Text(Point(400, 120), "Encode")
    button_outline = Rectangle(Point(360, 100), Point(440, 140))
    encode_button.draw(win)
    button_outline.draw(win)
    win.getMouse()

    acc = ""
    message = str(message_box.getText())
    key = str(key_box.getText())
    code(message, key)

    encode_button.undraw()
    button_outline.undraw()
    code_prep = Text(Point(400, 160), "The encoded message is:")
    code_prep.draw(win)

    code_display = Text(Point(400, 180), acc)
    code_display.draw(win)

    close = Text(Point(400, 380), "Click anywhere to close")
    close.draw(win)
    win.getMouse()
    win.close()

# design GUI
# set letters to numbers 0-25 (use a list -- how?)
# use a modelo and add it to A? x = (ord(1) +/- ord(2)) % 26 . x = x + ord('A')
#yay discrete structures helping out
#need a way to remove spaces: message.replace(" ","")

if __name__ == '__main__':
    main()
