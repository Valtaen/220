"""
Name: Matt Stewart
mean.py

Problem: Take and analyze traffic data

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    roads_survey = eval(input("How many roads were surveyed? "))
    car_temp = 0
    car_day_total = 0
    car_total = 0
    days_survey = 0
    for i in range(0, roads_survey):
        days_survey = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        for j in range(0, days_survey):
            car_temp = eval(input("How many cars traveled on day " + str(j + 1) + "? "))
            car_day_total = car_day_total + car_temp
        avg = car_day_total/days_survey
        print("Road" + str(i+1) + "average vehicles per day: " + str(round(avg, 2)))
        car_total = car_total + car_day_total
        car_day_total = 0
    print("Total number of vehicles traveled on all roads: " + str(car_total))
    total_avg = car_total / roads_survey
    print("Road" + str(i + 1) + "average vehicles per day:" + str(round(total_avg, 2)))

if __name__ == '__main__':
    main()
