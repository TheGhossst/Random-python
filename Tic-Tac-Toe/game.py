from tkinter import *
import random as rand

def nextGame():
    print("New game")
    
def checkWinner():
    print("bah")
    
def nextTurn(row,column):
    #print(f"{row}{column}")
    global turn
    
    if board[row][column]['text'] == "":
        if turn == players[0]:
            board[row][column]['text'] = turn
    
players = ["X","O"]

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

turn = rand.choice(players)
print(turn)

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