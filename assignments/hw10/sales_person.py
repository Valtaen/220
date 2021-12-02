"""
Name: Matt Stewart
three_door_game.py

Problem: Make a class that takes in all of a salesperson's data.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:

    """
    My attempt at making the SalesPerson class. Functionality includes:

    -get_id(): Returns the employee's ID
    -get_name(): Returns the employee's name
    -set_name(name): Changes the employee's name to the new one
    -enter_sale(sale): Adds the listed value to a list of the employee's sales
    -total_sales(): Adds up all the employee's sales and returns the sum
    -get_sales(): Returns all of the employee's sales
    -met_quota(quota): Checks if the employee met the sale quota or not, True/False
    -compare_to(other): Compares an employee's total sales with another, returns 1 if
    theirs is higher, -1 if theirs is lower, and 0 if they are the same
    """
    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def total_sales(self):
        total = 0
        for item in self.sales:
            total += item
        return float(total)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return bool(self.total_sales() >= quota)

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() == other.total_sales():
            return 0
        return -1

    def __str__(self):
        return str(self.employee_id) + "-" + str(self.name) + ": " + str(self.total_sales())
