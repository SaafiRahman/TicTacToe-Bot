import copy

board = [" " for x in range(10)]


def insert(spot, letter):
    board[spot] = letter


def isFree(spot):
    return board[spot] == " "


def showBoard():
    print(" " + board[1] + "|" + board[2] + "|" + board[3])
    print("-------")
    print(" " + board[4] + "|" + board[5] + "|" + board[6])
    print("-------")
    print(" " + board[7] + "|" + board[8] + "|" + board[9])


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


def playerMove():
    pmove = True
    while pmove:
        place = input("Enter a number to place your X (1-9): ")
        try:
            place = int(place)
            if place > 0 and place < 10:
                if isFree(place):
                    pmove = False
                    insert(place, "X")
                else:
                    print("sorry, this place is occupied")
            else:
                print("sorry, invalid number, please ender a number between 1 and 9")
        except:
            print("please enter a number between 1 and 9")


def comMove():
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
            print("BestMove", bestmove)

    insert(bestmove, "O")
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
    print("welcome to TicTacToe")
    showBoard()

    while not isBoardfull(board):
        if not (isWinner(board, "O")):
            playerMove()
            showBoard()
        else:
            print("sorry, computer wins")
            break
        print("---------------")
        if not (isWinner(board, "X")):
            comMove()
            showBoard()
        else:
            print("congrats, you win!")
            break
        print("---------------")

    if isBoardfull(board):
        print("tie game")


main()
