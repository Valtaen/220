

def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        weight = 0
        new_line = line.split(": ")
        name_split = new_line[0]
        number_split = new_line[1]
        num_split = number_split.split()
        weight_grade = 0
        total_grade = 0
        for i in range(0, len(num_split), 2):
            weight += int(num_split[i])
        if weight < 100:
            outfile.write(str(name_split) + "'s average: Error: The weights are less than 100." + "\n")
        elif weight > 100:
            outfile.write(str(name_split) + "'s average: Error: The weights are more than 100." + "\n")
        else:
            for i in range(0, len(num_split), 2):
                weight_temp = int(num_split[i]) * 0.01
                num_temp = int(num_split[i+1])
                weight_grade = weight_temp * num_temp
                total_grade += weight_grade
            outfile.write(str(name_split) + "'s average: " + str(round(total_grade, 1)) + "\n")

#if __name__ == '__main__':
#    main()

weighted_average("grades.txt", "test.txt")

#There are so many issues that come up with running this. The multiplications end up
#with numbers that go 10+ digits past the decimal despite using round. If I remove
#lines 12 or 28-29 then every time I run the test program different averages come up
#with the wrong values each time, in no consistent pattern. If I leave those lines in,
#however, the test runs accurately.

