"""
Name: Matt Stewart
sales_force.py

Problem: Make a class that'll take in all of the SalesPerson's data

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:

    """
    My attempt at making the SalesForce class. Functionality includes:

    -add_data(filename): Adding in data from a text file, formatted
    "Employee ID, Name, Sale1 Sale2 Sale3 etc."
    -quota_report(quota): Creating a list with data from each SalesPerson,
    to include ID, Name, Total sales data, and if they met the quota
    -top_seller(): Determine the top seller(s) among the SalesPerson
    -individual_sales(employee_id): Determine if there is a SalesPerson with a given id
    """

    def __init__(self):
        self.sales_people = []

    def add_data(self, filename):
        with open(filename, 'r') as infile:
            # linter suggested using with instead of infile = *** // infile.close()
            for line in infile:
                line = line.replace("\n", "")
                line = line.split(", ")
                person = SalesPerson(line[0].replace(",", ""), line[1].replace(",", ""))
                self.sales_people = self.sales_people + [person]
                line2 = line[2].split(" ")
                for i in range(len(line2)):
                    person.enter_sale(float(line2[i]))

    def quota_report(self, quota):
        new_list = []
        for person in self.sales_people:
            emp = person.get_id()
            name = person.get_name()
            total = person.total_sales()
            temp = [emp] + [name] + [total]
            if total >= quota:
                temp = temp + [True]
            else:
                temp = temp + [False]
            new_list = new_list + [temp]
        return new_list

    def top_seller(self):
        top_seller_goal = 0
        top_sellers = []
        for person in self.sales_people:
            if person.total_sales() > top_seller_goal:
                top_sellers = [person]
                top_seller_goal = person.total_sales()
            elif person.total_sales() == top_seller_goal:
                top_sellers = top_sellers + [person]
        return top_sellers

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.employee_id == employee_id:
                return person
        return None
