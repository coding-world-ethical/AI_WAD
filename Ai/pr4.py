import nltk
import pandas as pd

# PART 4 :- TIC-TAC-TOE GAME SIMULATION

def print_board(board):
    print('-----------')
    print(f' {board[0]} | {board[1]} | {board[2]}')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5]}')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]}')
    print('-----------')

def check_win(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def tic_tac_toe():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    players = ['x', '0']
    turn = 0
    current_player = players[turn]
    print_board(board)
    
    while True:
        position = input(f"Player {current_player}, enter a position (1-9): ")
        if position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Invalid position. Please try again.")
            continue
            
        index = int(position) - 1
        
        if board[index] in players:
            print("Position already taken. Please try again.")
            continue
            
        board[index] = current_player
        print_board(board)
        
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
            
        if all(symbol in players for symbol in board):
            print("Tie game!")
            break
            
        turn = (turn + 1) % 2
        current_player = players[turn]

tic_tac_toe()