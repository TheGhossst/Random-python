from tkinter import *
import random as rand

players = ["X","O"]

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

turn = rand.choice(players)

def nextGame():
    global turn

    turn = rand.choice(players)
    turnLabel.config(text = f"{turn}'s turn")

    for row in range(3):
        for col in range(3):
            board[row][col].config(text = "",bg = "#F0F0F0")
    
def isEmptySpaces():
    totalSpace = 9
    
    for row in range(3):
        for col in range(3):
            if board[row][col]['text'] != "":
                totalSpace -= 1
                
    if totalSpace == 0:
        return False
    return True
    
def checkWinner():
    
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text']  == board[i][2]['text'] !=""  : #row check
            board[i][0].config(bg = "green")
            board[i][1].config(bg = "green")
            board[i][2].config(bg = "green")
            return True
    for i in range(3):
        if  board[0][i]['text'] == board[1][i]['text'] ==  board[2][i]['text'] !="" :  #coloumn check
            board[0][i].config(bg = "green")
            board[1][i].config(bg = "green")
            board[2][i].config(bg = "green")
            return True
    for i in range(1):
        if board[i][i]['text'] == board[i+1][i+1]['text']== board[i+2][i+2]['text']!="": #diagonal check :(
            board[i][i].config(bg = "green")
            board[i+1][i+1].config(bg = "green")
            board[i+2][i+2].config(bg = "green")
            return True
        if board[i][i+2]['text'] == board[i+1][i+1]['text']== board[i+2][i]['text']!="": #anti-diagonal check :(
            board[i][i+2].config(bg = "green")
            board[i+1][i+1].config(bg = "green")
            board[i+2][i].config(bg = "green")
            return True
    
    if isEmptySpaces() is False:
        return "Tie"
       
    return False
    
def nextTurn(row,column):
    global turn
    
    if board[row][column]['text'] == "" and checkWinner() is False:
        if turn == players[0]:
            board[row][column]['text'] = turn
            if checkWinner() is False:
                turn = players[1]
                turnLabel.config(text = f"{players[1]}'s turn")
            elif checkWinner() is True:
                turnLabel.config(text = f"{turn} won")
            elif checkWinner() == "Tie":
                turnLabel.config(text = "Tie")
                
        elif turn == players[1]:
            board[row][column]['text'] = turn
            if checkWinner() is False:
                turn = players[0]
                turnLabel.config(text = f"{players[0]}'s turn")
            elif checkWinner() is True:
                turnLabel.config(text = f"{turn} won")
            elif checkWinner() == "Tie":
                turnLabel.config(text = "Tie")
    
window = Tk()
window.title("Tic-Tac-Toe")

gameLabel = Label(window,text = "Tic-Tac-Toe", font=('Arial', 20))
gameLabel.pack(side = "top" )

nextGameButton = Button(window,text= 'Next Game', font=('Helvetica',16), command= nextGame)
nextGameButton.pack(side = "top")

turnLabel = Label(window,text = f"{turn}'s turn", font=('Arial', 20))
turnLabel.pack(side = "top" )


cellFrame = Frame(window)
cellFrame.pack()

for i in range(3):
    for j in range(3):
        board[i][j] = Button(cellFrame, text="", font=('Helvetica', 16), width=5, height=2)
        board[i][j].config(command=lambda row=i, column=j: nextTurn(row, column))
        board[i][j].grid(row = i, column = j)

window.mainloop()