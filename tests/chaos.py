"""
Name: Matt Stewart
chaos.py

Problem: This program illustrates a chaotic function

Certification of Authenticity
I certify that this assignment was done in class with the class.
"""

def main():
    print("This program illustrates a chaotic function")
    # this is where users enter a value
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        # assignment operator -- gives a value to x
        x = 3.9 * x * (1 - x)
        print(x)

main()