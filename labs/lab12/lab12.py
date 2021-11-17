"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[1] = "Matt Stewart"
    except:
        pass


def read_data(filename):
    f = open(filename, "r")
    d = f.readline()
    d = d.split(" ")
    i = 0
    while i < len(d):
        d[i] = int(d[i])
        i += 1
    return d


def is_in_linear(search_val, values):
    i = 0
    while i <= len(values):
        if search_val == True:
            return True
        else:
            i += 1
    if i >= len(values):
        return False


def good_input():
    x = eval(input("Enter a number between 1 and 10: "))
    while x < 0 or x > 10:
        x = eval(input("Enter a number between 1 and 10: "))
    return x


def num_digits():
    x = eval(input("Enter a positive integer: "))
    acc = 0
    while x <= 0:
        x = eval(input("Enter a positive integer: "))
    while x > 0:
        acc += 1
        x //= 10
    print("There are " + str(acc) + " digits in the number")



def hi_low_game():
    number = randint(1,100)
    guess = 1
    x = eval(input("Enter your number for your guess: "))
    while number != x and guess < 7:
        if x > number:
            print("Your number was too high.")
            x = eval(input("Enter your number for your guess: "))
        elif x < number:
            print("Your number was too low.")
            x = eval(input("Enter your number for your guess: "))
        guess += 1
    if guess >= 7 and x != number:
        print("You've used 7 guesses. You lose!")
    elif x == number:
        print("You've won in " + str(guess) + " guesses")


def main():
    find_and_remove_first(lst, value)
    values = read_data("dataSorted.txt")
    is_in_linear(50, values)
    good_input()
    num_digits()
    hi_low_game()
    pass


main()
