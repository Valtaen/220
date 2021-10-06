"""
Name: Matt Stewart
lab6.py
"""


def name_reverse():
    full_name = input('Enter your full name: ')
    full_name = full_name.split(" ")
    name_reordered = (full_name[1] + ", " + full_name[0])
    print(name_reordered)

def company_name():
    website = input('Enter the website URL: ')
    website = website.split(".")
    cap = website[1][0]
    print(cap.upper() + website[1][1:])

def initials():
    n = eval(input('Enter the number of names to be entered: '))
    for i in range(n):
        first = input('Enter the first name of Student ' + str(i+1) + ': ')
        second = input('Enter their second name: ')
        print(first + "'s initials are " + first[0]+second[0])


def names():
    name_list = input('Enter a list of names, separated by commas: ')
    name_split = name_list.split(", ")
    initials_list = 'The initials are '
    for word in name_split:
        split_name = word.split(" ")
        initials_list = initials_list + str(split_name[0][0]) + str(split_name[1][0] + " ")
    print(initials_list)


def thirds():
    n = eval(input('Enter the number of sentences you will input: '))
    for i in range(n):
        x = input('Enter the sentence: ')
        x = x[::3]
        print(x)

def word_average():
    x = input('Enter a sentence: ')
    acc = 0
    words = x.split(" ")
    word_count = len(words)
    for word in words:
        acc = acc + len(word)
    print(acc/word_count)


def pig_latin():
    words = input('Enter the sentence to be translated here: ')
    words = words.lower()
    pig_base = words.split(" ")
    pig_latin_output = ""
    for word in pig_base:
        pig_latin = word[1:] + word[0] + "ay"
        pig_latin_output = pig_latin_output + pig_latin + " "
    print(pig_latin_output)


def main():
    #name_reverse()
    #company_name()
    #initials()
    #names()
    #thirds()
    word_average()
    #pig_latin()


main()


#x = hello world
#x[2:4] = llo
#x.split(" ")
#x[0] = hello
#x[0][0] = h















