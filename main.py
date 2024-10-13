import random

#Definitions
move = "iefvhubefvbhudsvdhu"
winner = "no one"
board = []
for i in range(9):
    board += str(i + 1)

#Creating a way to show the current board
def showBoard():
    global board
    for k in range(0, 7, 3):
        for i in range(3):
            print(board[i + k], end = " ")
        print("")

#Letting the player play a move and recording it on the board
def playerMove():
    global board, move
    if winner == "no one":
        move = input("It's your turn. Please make your move: ")
        while len(move) != 1 or int(move) < 1 or int(move) > 9 or board[int(move) - 1] == "O" or board[int(move) - 1] == "X":
            move = input("please make a valid move: ")
        board[int(move) - 1] = "X"

#Letting the computer generate a random move and recording it on the board
def computerMove():
    global board, move
    if winner == "no one":
        move = random.randint(0, 8)
        while board[move] == "X" or board[move] == "O":
            move = random.randint(0, 8)
        board[move] = "O"
        print("I play:", move + 1)

#Checking if the player has won
def checkForWinX():
    global winner
    if board[4] == "X":
        if board[3] == "X":
            if board[5] == "X":
                winner = "X"

        if board[1] == "X":
            if board[7] == "X":
                winner = "X"

        if board[0] == "X":
            if board[8] == "X":
                winner = "X"

        if board[2] == "X":
            if board[6] == "X":
                winner = "X"
                
    if board[0] == "X":
        if board[1] == "X":
            if board[2] == "X":
                winner = "X"
                
        if board[3] == "X":
            if board[6] == "X":
                winner = "X"
                
    if board[6] == "X":
        if board[7] == "X":
            if board[8] == "X":
                winner = "X"
                        
    if board[2] == "X":
        if board[5] == "X":
            if board[8] == "X":
                winner = "X"

#Checking if the computer has won
def checkForWinO():
    global winner
    if board[4] == "O":
        if board[3] == "O":
            if board[5] == "O":
                winner = "O"

        if board[1] == "O":
            if board[7] == "O":
                winner = "O"

        if board[0] == "O":
            if board[8] == "O":
                winner = "O"

        if board[2] == "O":
            if board[6] == "O":
                winner = "O"
                
    if board[0] == "O":
        if board[1] == "O":
            if board[2] == "O":
                winner = "O"
                
        if board[3] == "O":
            if board[6] == "O":
                winner = "O"
                
    if board[6] == "O":
        if board[7] == "O":
            if board[8] == "O":
                winner = "O"
                        
    if board[2] == "O":
        if board[5] == "O":
            if board[8] == "O":
                winner = "O"

#Checking if it's a draw
def checkForDraw():
    global board, winner
    xmoves = 0
    for i in range(len(board)):
        if board[i] == "X":
            xmoves += 1
    if xmoves == 5 and winner == "no one":
        winner = "Draw"

#main loop
print("Welcome to Tic-Tac-Toe!")
showBoard()
playerMove()
showBoard()
while winner == "no one":
    computerMove()
    showBoard()
    checkForWinO()
    move = "iefvhubefvbhudsvdhu"
    playerMove()
    showBoard()
    checkForWinX()
    checkForDraw()

#game end message
if winner == "O":
    print("Oh no. You lost")
elif winner == "X":
    print("Great job. You won!")
else:
    print("It's a draw")