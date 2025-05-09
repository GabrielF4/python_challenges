#Challenge 10: Tic Tac Toe with AI

"""
Input is a number representing one of the following squares:

-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------

Keep entering numbers until either you or the computer wins or it's a draw
"""

import random

ROW_SIZE = COL_SIZE= 3
BOARD_SIZE = 9
PLAYER_1_MARKER = 'X'
PLAYER_2_MARKER = 'O'

#Convert a number 1-9 to position on board with row and column (0-2, 0-2)
def get_position(value):
    return (value - 1) // ROW_SIZE, (value - 1) % ROW_SIZE

#Check if 3 positions on board are equal and not empty
def check_3_in_row(pos1, pos2, pos3):
    return pos1 == pos2 == pos3 != 0

#Check for winning positions
def check_winner(board):
    if check_3_in_row(board[0][0], board[0][1], board[0][2]):
        return board[0][0]
    if check_3_in_row(board[1][0], board[1][1], board[1][2]):
        return board[1][0]
    if check_3_in_row(board[2][0], board[2][1], board[2][2]):
        return board[2][0]
    if check_3_in_row(board[0][0], board[1][0], board[2][0]):
        return board[0][0]
    if check_3_in_row(board[0][1], board[1][1], board[2][1]):
        return board[0][1]
    if check_3_in_row(board[0][2], board[1][2], board[2][2]):
        return board[0][2]
    if check_3_in_row(board[0][0], board[1][1], board[2][2]):
        return board[0][0]
    if check_3_in_row(board[0][2], board[1][1], board[2][0]):
        return board[0][2]
    return -1

#Controls board status and choose action dependent on if a player has won or if it is a draw
def game_check(board, valid_input):
    #Check if user won
    if check_winner(board) == PLAYER_1_MARKER:
        print_board(board)
        print("YOU WON! CONGRATULATIONS")
        return True
    
    #Check if computer won
    if check_winner(board) == PLAYER_2_MARKER:
        print_board(board)
        print("GAME OVER! COMPUTER WON!")
        return True
    
    #Check if the game is full without a win
    if not valid_input:
        print("GAME OVER. IT'S A DRAW")
        return True
    
    return False

def player_turn(board, valid_input):
    #Get user input with a valid value
    while(True):
        user_input = input("Enter your square (1-9): ")
        if not user_input.isdigit() or not int(user_input) in valid_input:
            print("Not valid input!")
        else:
            break

    #Update board with user input
    row, col = get_position(int(user_input))
    board[row][col] = PLAYER_1_MARKER
    valid_input.remove(int(user_input))

def get_computer_move(board, valid_input):
    #Get computer input
    computer_input = random.choice(valid_input) #Default input

    #Check for winning moves
    for test_move in valid_input:

        test_board = [row[:] for row in board]
        test_input = valid_input[:]

        row, col = get_position(test_move)
        test_board[row][col] = PLAYER_2_MARKER

        if check_winner(test_board) == PLAYER_2_MARKER:
            print("Computer found winning move!")
            return test_move

        #Check for blocking move
        test_input.remove(test_move)
        for test_move_2 in test_input:
            test_board_2 = [row[:] for row in test_board]
            
            row, col = get_position(test_move_2)
            test_board_2[row][col] = PLAYER_1_MARKER
            if check_winner(test_board_2) == PLAYER_1_MARKER:
                print("Computer found blocking move!")
                return test_move_2
            
    return computer_input

def computer_turn(board, valid_input):
    computer_input = get_computer_move(board, valid_input)
    #Update board with computer input
    row, col = get_position(computer_input)
    board[row][col] = PLAYER_2_MARKER
    valid_input.remove(computer_input)

#Print the board
def print_board(board):
    for i in range(ROW_SIZE):
        print("----------")
        for j in range(COL_SIZE):
            print("|", end="")
            print(" " if board[i][j] == 0 else board[i][j], end=" ")
        print("|")
    print("----------")

#Setup board
board = [[0 for _ in range(ROW_SIZE)] for _ in range(COL_SIZE)]
valid_input = [i for i in range(1, BOARD_SIZE + 1)]

#Deciding if starting
while(True):
    user_input = input("Do you want to start? y/n: ")
    if user_input.lower() == 'y':
        playing = True
        break
    elif user_input.lower() == 'n':
        playing = False
        break
    elif user_input.lower() == 'exit':
        exit()
    else:
        print("Invalid input")

#Game Loop
while(True):
    
    #Jump this part first iteration if computer starts
    if(playing):
        player_turn(board, valid_input)
        if game_check(board, valid_input):
            break

    playing = True

    computer_turn(board, valid_input)
    if game_check(board, valid_input):
        break

    print_board(board)
    