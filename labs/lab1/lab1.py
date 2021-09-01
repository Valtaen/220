"""
Name: Natt Stewart
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

#calc_rec_area()

#Problem: This function calculates the volume of an object.

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

#calc_volume()

def shooting_percentage():
    total_shots = eval(input("Enter the total number of shots taken: "))
    shots_made = eval(input("Enter the number of shots made: "))
    shot_percentage = shots_made / total_shots * 100
    print("Shooting Percentage =", shot_percentage)

#shooting_percentage()

def coffee():
    coffee_cost = 10.50
    shipping = 0.86
    coffee_total = 11.36
    fixed_cost = 1.5
    units = eval(input("Enter number of pounds of coffee ordered: "))
    total_coffee_cost = coffee_total * units + fixed_cost
    print("Total order cost =", total_coffee_cost)

#coffee()

def kilometers_to_miles():
    kilos_traveled = eval(input("Enter number of kilometers traveled: "))
    miles_ratio = 1.61
    conversion = kilos_traveled/miles_ratio
    print("Total miles traveled= ", conversion)

kilometers_to_miles()