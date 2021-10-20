"""
Name: Matt Stewart
lab8.py
"""

def encode(message, key):
    acc = " "
    for r in message:
        x = ord(r)
        x = x + key
        acc = acc + chr(x)
    return(acc)

def encode_better(message, key):
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
    return"".join(acc)

def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    i = 1
    for line in infile:
        new_line = line.split()
        for word in new_line:
            outfile.write(str(i) + " " + word + "\n")
            i += 1

def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        new_line = line.split()
        new_line[2] = str(round(float(new_line[2]) + 1.65, 2))
        outfile.write(" ".join(new_line) + "\n")

def calc_check_sum(ISBN):
    ISBN = str(ISBN)
    sum = 0
    for i in range(len(ISBN)):
        num = int(ISBN[i] * (10 - i))
        sum += num
    return(sum%11)

def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        outfile.write(line + "\n")

def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        new_line = encode(line, key)
        outfile.write(new_line + "\n")

def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    pad = open(pad, "r")
    key = pad.read()
    for line in infile:
        new_line = encode_better(line, key)
        outfile.write(new_line + "\n")

def main():
    number_words("cthulhu.txt", "numbers.txt")
    hourly_wages("hourly_wages.txt", "new_wages.txt")
    calc_check_sum(1515151515)
    send_message("message.txt", "fred")
    send_safe_message("message.txt", "bob", 3)
    send_uncrackable_message("message.txt", "dale", "pad.txt")
    pass


main()

