"""
Name: Matt Stewart
interest.py

Problem: Calculate interest accrued over a month on an outstanding balance when a payment has been made

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    rate = eval(input("Enter the annual interest rate: "))
    days = eval(input("Enter the number of days in billing cycle: "))
    previous_balance = eval(input("Enter the previous net balance: "))
    payment = eval(input("Enter the payment amount: "))
    payment_day = eval(input("Enter the day the payment was made: "))
    average_day_bal = ((previous_balance * days) - (payment * (days - payment_day)))/days
    monthly_rate = (rate/12 * .01)
    monthly_interest = round(average_day_bal * monthly_rate, 2)
    print("The monthly interest incurred is", monthly_interest)


main()
