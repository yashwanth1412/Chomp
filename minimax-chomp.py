import numpy as np
import math
import sys

board = np.array([['0']*5]*5)

def output_board():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

def check_win():
    if board[3][0] == '0' or board[4][1] == '0':
        return False
    return True

def change_state(m, n):
    for i in range(m+1):
        for j in range(n, 5):
            board[i][j] = '.'

def revert(b):
    for i, j in enumerate(b):
        board[i] = j

def minimax(is_max, alpha, beta, steps):
    steps += 1
    if check_win():
        if is_max:
            return -1000 + steps
        else:
            return 1000 - steps

    b = board.copy()
    if is_max:
        best_score = -1000000
        for i in range(5):
            for j in range(5):
                if (i!=4 or j!=0) and board[i][j] =='0':
                    change_state(i, j)
                    best_score = max(best_score, minimax(False, alpha, beta, steps))
                    alpha = max(alpha, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

    else:
        best_score = 1000000
        for i in range(5):
            for j in range(5):
                if (i!=4 or j!=0) and board[i][j] =='0':
                    change_state(i, j)
                    best_score = min(best_score, minimax(True, alpha, beta, steps))
                    beta = min(beta, best_score)
                    revert(b)
                    if(alpha >= beta):
                        return best_score
        return best_score

def ai_move():
    print("AI turn")
    bi = 0
    bj = 0
    b = board.copy()
    
    best_score = 1000000
    for i in range(5):
        for j in range(5):
            if (i!=4 or j!=0) and board[i][j] =='0':
                change_state(i, j)
                s = minimax(True, -1000000, 1000000, 0)
                if best_score > s:
                    best_score = s
                    bi = i
                    bj = j

                revert(b)

    change_state(bi, bj)
    print(f"AI chose {bi+1} row, {bj+1} column")

def player():
    print("Your turn")
    m = int(input("Enter row no: "))-1
    n = int(input("Enter column no: "))-1

    if m == 4 and n == 0:
        print("You selected poison block")
        print("You lost!")
        sys.exit(0)

    while board[m][n] != '0':
        print("Invalid move.... Please enter a valid move")
        m = int(input("Enter row no: "))-1
        n = int(input("Enter column no: "))-1
    change_state(m, n)

# main function
    
a = 0
board[4][0] = 'X'
output_board()

while True:
    if a%2 == 0:
        if check_win():
            print("AI won")
            sys.exit(0)
        
        player()
        a += 1
        output_board()

    else:
        if check_win():
            print("Congratulations, you won")
            sys.exit(0)

        ai_move()
        a += 1
        output_board()