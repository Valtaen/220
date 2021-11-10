"""
Name: Matt Stewart
lab11.py
"""

from random import randint

def get_words(filename):
    file_name = filename
    file = open(file_name, "r")
    wordbank = []
    for line in file:
        wordbank.append(line.strip())
    return wordbank

def pick_word(wordbank):
    ran_num = randint(0, len(wordbank)-1)
    secret_word = wordbank[ran_num]
    print(secret_word)
    return secret_word

def progress(guessed_word, turn_count, guessed_letters):
    printstring = " "
    for i in range(0, len(guessed_word)):
        printstring += str(guessed_word[i]) + " "
    print(printstring)
    print()
    print("Number of Guesses: " + str(turn_count))
    print("Guessed Letters: " + str(guessed_letters))
    print()

def guessWord(secret_word, guessed_letters, guessed_word, turn_count, letter):
    check = False
    for i in range(0, len(secret_word)):
        if letter == secret_word[i]:
            guessed_word[i] = letter
            check = True
    if check == True:
        return True
    guessed_letters.append(letter)
    return False

def wordSpelled(guessed_word, secret_word):
    if "".join(guessed_word) == secret_word:
        return True
    else:
        return False

def guessLetter(guessed_letters, turn_count, secret_word, guessed_word):
    letter = input("Enter a letter: ")
    letter = letter.lower()
    check = False
    while check == False:
        check = True
        for ch in guessed_letters:
            if letter == ch:
                print("You have already guessed that letter. Try again.")
                letter = input("Enter a letter: ")
                letter = letter.lower()
                check = False
    if guessWord(secret_word, guessed_letters, guessed_word, turn_count, letter):
        return True
    else:
        return False

def playGame():
    wordbank = get_words("wordlist.txt")
    secret_word = pick_word(wordbank)
    guessed_word = ["_"] * len(secret_word)
    guessed_letters = []
    turn_count = 0
    progress(guessed_word, turn_count, guessed_letters)
    while turn_count < 7 and not wordSpelled(guessed_word, secret_word):
        if guessLetter(guessed_letters, turn_count, secret_word, guessed_word) == False:
            turn_count += 1
        progress(guessed_word, turn_count, guessed_letters)
    if turn_count >= 7:
        print("You have run out of turns.")
    else:
        print("You've won!")

def main():
    playGame()


main()