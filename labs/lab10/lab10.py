"""
Name: Matt Stewart
lab10.py
"""

#method to build board(create list 1-9 and return list)
#void method to display board
#void method to fill a spot on board. Only allow letters X or 0
#boolean method to determine if spot is legal
#boolean to determine if game is won
#boolean to determine if game is over. Should call previous method plus check moves
#method to play game

def build():
    return list(range(1, 10))

def display(board):
    for i in range(3):
        n = i*3
        print(str(board[n]) + " | " + str(board[n+1]) + " | " + str(board[n+2]))
        print(10*"-")

def fill(board, position, piece):
    if piece == 'X' or piece == 'O':
        board[position] = piece

def legal(board, position):
    if board[position-1] == position:
        return True
    else:
        return False

def is_won(board, piece):
    for i in range(3):
        n = i*3
        if board[n] != piece:
            continue
        if board[n+1] != piece:
            continue
        if board[n+2] != piece:
            continue
        return True
    for i in range(3):
        if board[i] != piece:
            continue
        if board[i+3] != piece:
            continue
        if board[i+6] != piece:
            continue
        return True
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True
    return False

def over(board):
    if is_won(board, "X"):
        return True
    elif is_won(board, "O"):
        return True
    else:
        for i in range(9):
            if board[i] == i + 1:
                return False
    return True

def play():
    board = build()
    display(board)
    while True:
        play1 = eval(input("Player 1, where do you want to play an X? "))
        if legal(board, play1):
            fill(board, play1 - 1, "X")
        else:
            print("That is not a legal move!")
            continue
        display(board)
        if over(board):
            if is_won(board, "X"):
                print("Player 1 wins!")
                break
            elif is_won(board, "O"):
                print("Player 2 wins!")
                break
            else:
                print("It's a tie!")
                break
        play2 = eval(input("Player 2, where do you want to play a 0? "))
        if legal(board, play2):
            fill(board, play2 - 1, "O")
        else:
            print("That is not a legal move!")
            continue
        display(board)
        if over(board):
            if is_won(board, "X"):
                print("Player 1 wins!")
                break
            elif is_won(board, "O"):
                print("Player 2 wins!")
                break
            else:
                print("It's a tie!")
                break


def main():
    play()
    pass


main()