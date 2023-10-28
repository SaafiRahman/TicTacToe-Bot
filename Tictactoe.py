import copy
from tkinter import *
import tkinter.font as font

board = [" " for x in range(10)]
PMove = True


root = Tk()
myFont = font.Font(size='36', weight=font.BOLD)
main_label = Label(root, text="Welcome to TicTacToe", font=myFont).grid(row=1, column=0, columnspan=3, sticky="ew")
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)


def insert(spot, letter):
    global PMove

    r = find_row(spot)
    c = find_col(spot)
    board[spot] = letter
    if not PMove:
        new_button = Button(root, text=board[spot], font=myFont).grid(row=r, column=c, sticky="nesw")   
    
def isFree(spot):
    return board[spot] == " "

def find_row(spot):
    if 1<=spot<=3:
        r=2
    elif 4<=spot<=6:
        r=3
    else:
        r=4
    return r

def find_col(spot):
    if spot == 1 or spot == 4 or spot == 7:
        c=0
    elif spot == 2 or spot == 5 or spot == 8:
        c=1
    else:
        c=2
    return c

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
    

def player_update(spot):
    global Turn
    global PMove

    r = find_row(spot)
    c = find_col(spot)

    if PMove:
        if isFree(spot):
            insert (spot, "X")
            PMove = False
            new_button = Button(root, text=board[spot], font=myFont).grid(row=r, column=c, sticky="nesw")
            if isWinner(board, "X") or isBoardfull(board):
                endgame()
            else:
                comMove()

def endgame():
    global PMove

    if isWinner(board, "X"):
        t_l = Button(root, text="X", font=myFont).grid(row=2, column=0, sticky="nesw")
        t_m = Button(root, text="X", font=myFont).grid(row=2, column=1, sticky="nesw")
        t_r = Button(root, text="X", font=myFont).grid(row=2, column=2, sticky="nesw")
        m_l = Button(root, text="X", font=myFont).grid(row=3, column=0, sticky="nesw")
        m_m = Button(root, text="X", font=myFont).grid(row=3, column=1, sticky="nesw")
        m_r = Button(root, text="X", font=myFont).grid(row=3, column=2, sticky="nesw")
        b_l = Button(root, text="X", font=myFont).grid(row=4, column=0, sticky="nesw")
        b_m = Button(root, text="X", font=myFont).grid(row=4, column=1, sticky="nesw")
        b_r = Button(root, text="X", font=myFont).grid(row=4, column=2, sticky="nesw")
        win_label = Label(root, text="congrats, X wins", font=myFont).grid(row=5, column=0, columnspan=3, sticky="ew")
        root.mainloop()
    elif isWinner(board, "O"):
        t_l = Button(root, text="O", font=myFont).grid(row=2, column=0, sticky="nesw")
        t_m = Button(root, text="O", font=myFont).grid(row=2, column=1, sticky="nesw")
        t_r = Button(root, text="O", font=myFont).grid(row=2, column=2, sticky="nesw")
        m_l = Button(root, text="O", font=myFont).grid(row=3, column=0, sticky="nesw")
        m_m = Button(root, text="O", font=myFont).grid(row=3, column=1, sticky="nesw")
        m_r = Button(root, text="O", font=myFont).grid(row=3, column=2, sticky="nesw")
        b_l = Button(root, text="O", font=myFont).grid(row=4, column=0, sticky="nesw")
        b_m = Button(root, text="O", font=myFont).grid(row=4, column=1, sticky="nesw")
        b_r = Button(root, text="O", font=myFont).grid(row=4, column=2, sticky="nesw")
        win_label = Label(root, text="Sorry, O wins", font=myFont).grid(row=5, column=0, columnspan=3, sticky="ew")
        root.mainloop()
    else:
        t_l = Button(root, text="O", font=myFont).grid(row=2, column=0, sticky="nesw")
        t_m = Button(root, text="X", font=myFont).grid(row=2, column=1, sticky="nesw")
        t_r = Button(root, text="O", font=myFont).grid(row=2, column=2, sticky="nesw")
        m_l = Button(root, text="X", font=myFont).grid(row=3, column=0, sticky="nesw")
        m_m = Button(root, text="O", font=myFont).grid(row=3, column=1, sticky="nesw")
        m_r = Button(root, text="X", font=myFont).grid(row=3, column=2, sticky="nesw")
        b_l = Button(root, text="O", font=myFont).grid(row=4, column=0, sticky="nesw")
        b_m = Button(root, text="X", font=myFont).grid(row=4, column=1, sticky="nesw")
        b_r = Button(root, text="O", font=myFont).grid(row=4, column=2, sticky="nesw")
        win_label = Label(root, text="Tie game", font=myFont).grid(row=5, column=0, columnspan=3, sticky="ew")



def isWinner(b, l):
    return (
        (b[1] == l and b[2] == l and b[3] == l)
        or (b[4] == l and b[5] == l and b[6] == l)
        or (b[7] == l and b[8] == l and b[9] == l)
        or (b[1] == l and b[4] == l and b[7] == l)
        or (b[2] == l and b[5] == l and b[8] == l)
        or (b[3] == l and b[6] == l and b[9] == l)
        or (b[1] == l and b[5] == l and b[9] == l)
        or (b[3] == l and b[5] == l and b[7] == l)
    )

def comMove():
    global PMove
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    bestscore = -1000
    bestmove = 0

    for i in possibleMoves:
        copyboard = copy.deepcopy(board)
        copyboard[i] = "O"
        score = minimax(copyboard, False)
        if score > bestscore:
            bestscore = score
            bestmove = i
            

    insert(bestmove, "O")
    print("BestMove", bestmove)
    if isWinner(board, "O") or isBoardfull(board):
        endgame()
    else:
        PMove = True
    return


def minimax(thisboard, isMaxing):
    if isWinner(thisboard, "O"):
        return 1
    elif isWinner(thisboard, "X"):
        return -1
    elif isBoardfull(thisboard):
        return 0

    if isMaxing:
        possibleMoves = [
            x for x, letter in enumerate(thisboard) if letter == " " and x != 0
        ]
        bestscore = -1000
        for i in possibleMoves:
            copyboard = thisboard[:]
            copyboard[i] = "O"
            score = minimax(copyboard, False)
            if score > bestscore:
                bestscore = score
        return bestscore
    else:
        possibleMoves = [
            x for x, letter in enumerate(thisboard) if letter == " " and x != 0
        ]
        bestscore = 1000
        for i in possibleMoves:
            copyboard = thisboard[:]
            copyboard[i] = "X"
            score = minimax(copyboard, True)
            if score < bestscore:
                bestscore = score
        return bestscore


def isBoardfull(b):
    return (
        b[1] != " "
        and b[2] != " "
        and b[3] != " "
        and b[4] != " "
        and b[5] != " "
        and b[6] != " "
        and b[7] != " "
        and b[8] != " "
        and b[9] != " "
    )


def main():
    showBoard()
#     while not isBoardfull(board):
#         # if not (isWinner(board, "O")):
#         #     playerMove()
#         # else:
#         #     print("sorry, computer wins")
#         #     break
#         print("---------------")
#         if not (isWinner(board, "X")):
#             comMove()
#         else:
#             print("congrats, you win!")
#             break
#         print("---------------")

#     if isBoardfull(board):
#         print("tie game")


main()
