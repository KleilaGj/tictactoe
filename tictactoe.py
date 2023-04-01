import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"

winner = None

gameRunning = True

# game board
def printBoard (board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# player input
def playerInput(board):
    inp = int(input("Choose a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("This spot is taken!")


# check for result
def checkHorizontal(board):
    global winner 
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkVertical(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    

def checkDiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    


def checkWin(board):
    global gameRunning
    if checkHorizontal(board):
        printBoard(board)
        print(f"Player {winner} wins!")
        gameRunning = False

    elif checkVertical(board):
        printBoard(board)
        print(f"Player {winner} wins!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"Player {winner} wins!")
        gameRunning = False



def checkTie(board):
    global gameRunning 
    if "-" not in board:
         printBoard(board)
         print("It's a tie!") 
         gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer 
    if currentPlayer== "X":
        currentPlayer = "O"
    else:
        currentPlayer== "X"


#computerPlayer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()


# check for result
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)