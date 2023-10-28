# Import necessary libraries
import copy
from tkinter import *
import tkinter.font as font

# Initialize game variables
board = [" " for x in range(10)]  # Initialize game board with empty spaces
PMove = True  # Variable to track current player's move (True for player, False for computer)

# Create a Tkinter window
root = Tk()
myFont = font.Font(size='36', weight=font.BOLD)

# Set up GUI layout and display a welcome label
main_label = Label(root, text="Welcome to TicTacToe", font=myFont).grid(row=1, column=0, columnspan=3, sticky="ew")
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)

# Function to insert a move into the game board and update GUI
def insert(spot, letter):
    global PMove
    r = find_row(spot)
    c = find_col(spot)
    board[spot] = letter
    if not PMove:
        new_button = Button(root, text=board[spot], font=myFont).grid(row=r, column=c, sticky="nesw")   
    
# Function to check if a spot on the board is free
def isFree(spot):
    return board[spot] == " "

# Functions to determine row and column for a given spot on the board
def find_row(spot):
    if 1 <= spot <= 3:
        return 2
    elif 4 <= spot <= 6:
        return 3
    else:
        return 4

def find_col(spot):
    if spot == 1 or spot == 4 or spot == 7:
        return 0
    elif spot == 2 or spot == 5 or spot == 8:
        return 1
    else:
        return 2

# Function to display the Tic-Tac-Toe game board as buttons in the GUI
def showBoard():
    t_l = Button(root, text=board[1], command=lambda: player_update(1)).grid(row=2, column=0, sticky="nesw")
    t_m = Button(root, text=board[2], command=lambda: player_update(2)).grid(row=2, column=1, sticky="nesw")
    t_r = Button(root, text=board[3], command=lambda: player_update(3)).grid(row=2, column=2, sticky="nesw")
    m_l = Button(root, text=board[4], command=lambda: player_update(4)).grid(row=3, column=0, sticky="nesw")
    m_m = Button(root, text=board[5], command=lambda: player_update(5)).grid(row=3, column=1, sticky="nesw")
    m_r = Button(root, text=board[6], command=lambda: player_update(6)).grid(row=3, column=2, sticky="nesw")
    b_l = Button(root, text=board[7], command=lambda: player_update(7)).grid(row=4, column=0, sticky="nesw")
    b_m = Button(root, text=board[8], command=lambda: player_update(8)).grid(row=4, column=1, sticky="nesw")
    b_r = Button(root, text=board[9], command=lambda: player_update(9)).grid(row=4, column=2, sticky="nesw")
    root.mainloop()

# Function to handle player's move, update the board, and check for a win or draw
def player_update(spot):
    global Turn
    global PMove
    r = find_row(spot)
    c = find_col(spot)
    
    # Check if the selected spot is free
    if PMove and isFree(spot):
        insert(spot, "X")
        PMove = False
        new_button = Button(root, text=board[spot], font=myFont).grid(row=r, column=c, sticky="nesw")
        # Check if player has won or if the game is a draw
        if isWinner(board, "X") or isBoardfull(board):
            endgame()
        else:
            comMove()  # Computer makes a move

# Function to display endgame state (win, lose, or tie) and appropriate messages
def endgame():
    global PMove
    
    # Check if player X has won
    if isWinner(board, "X"):
        # Display X in winning positions and a congratulatory message
        display_winner("X", "congrats, X wins")
    # Check if player O has won
    elif isWinner(board, "O"):
        # Display O in winning positions and a message indicating O's victory
        display_winner("O", "Sorry, O wins")
    else:
        # Display the board with X and O in their respective positions and a message indicating a tie game
        display_winner("X", "Tie game")

# Function to check if a player with symbol l has won on the board b
def isWinner(b, l):
    return (
        (b[1] == l and b[2] == l and b[3] == l) or
        (b[4] == l and b[5] == l and b[6] == l) or
        (b[7] == l and b[8] == l and b[9] == l) or
        (b[1] == l and b[4] == l and b[7] == l) or
        (b[2] == l and b[5] == l and b[8] == l) or
        (b[3] == l and b[6] == l and b[9] == l) or
        (b[1] == l and b[5] == l and b[9] == l) or
        (b[3] == l and b[5] == l and b[7] == l)
    )

# Function for computer's move using the minimax algorithm
def comMove():
    global PMove
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    bestscore = -1000
    bestmove = 0

    # Find the best move for the computer using minimax algorithm
    for i in possibleMoves:
        copyboard = copy.deepcopy(board)
        copyboard[i] = "O"
        score = minimax(copyboard, False)
        if score > bestscore:
            bestscore = score
            bestmove = i

    # Insert the computer's move into the board and check for win or draw
    insert(bestmove, "O")
    if isWinner(board, "O") or isBoardfull(board):
        endgame()
    else:
        PMove = True

# Recursive minimax function for finding the best move for the computer
def minimax(thisboard, isMaxing):
    if isWinner(thisboard, "O"):
        return 1
    elif isWinner(thisboard, "X"):
        return -1
    elif isBoardfull(thisboard):
        return 0

    if isMaxing:
        possibleMoves = [x for x, letter in enumerate(thisboard) if letter == " " and x != 0]
        bestscore = -1000
        # Evaluate each possible move and choose the one with the highest score
        for i in possibleMoves:
            copyboard = thisboard[:]
            copyboard[i] = "O"
            score = minimax(copyboard, False)
            if score > bestscore:
                bestscore = score
        return bestscore
    else:
        possibleMoves = [x for x, letter in enumerate(thisboard) if letter == " " and x != 0]
        bestscore = 1000
        # Evaluate each possible move and choose the one with the lowest score
        for i in possibleMoves:
            copyboard = thisboard[:]
            copyboard[i] = "X"
            score = minimax(copyboard, True)
            if score < bestscore:
                bestscore = score
        return bestscore

# Function to check if the board is full
def isBoardfull(b):
    return all(cell != " " for cell in b[1:])

# Function to display the endgame state on the GUI
def display_winner(symbol, message):
    # Display X or O in winning positions
    for i in range(1, 10):
        if board[i] == symbol:
            r, c = find_row(i), find_col(i)
            Button(root, text=symbol, font=myFont).grid(row=r, column=c, sticky="nesw")
    # Display the endgame message
    win_label = Label(root, text=message, font=myFont).grid(row=5, column=0, columnspan=3, sticky="ew")

# Main function to start the game by displaying the game board
def main():
    showBoard()

# Call the main function to start the game
main()
