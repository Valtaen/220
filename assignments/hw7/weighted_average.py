"""
Name: Matt Stewart
weighted_average.py

Problem: Take input from a text file to determine weighted average and save output to another file

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
# Every time I run this, randomly a different average will be off by 0.1,
# either too low or too high, with sometimes no errors.


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        weight = 0
        new_line = line.split(": ")
        name_split = new_line[0]
        number_split = new_line[1]
        num_split = number_split.split()
        total_grade = 0
        for i in range(0, len(num_split), 2):
            weight += int(num_split[i])
        if weight < 100:
            outfile.write(str(name_split) + "'s average: Error: The weights are less than 100." + "\n")
        elif weight > 100:
            outfile.write(str(name_split) + "'s average: Error: The weights are more than 100." + "\n")
        else:
            for j in range(0, len(num_split), 2):
                weight_temp = int(num_split[j]) * 0.01
                num_temp = int(num_split[j+1])
                weight_grade = weight_temp * num_temp
                total_grade += weight_grade
            outfile.write(str(name_split) + "'s average: " + str(round(total_grade, 1)) + "\n")

weighted_average("grades.txt", "weighted_grades.txt")

