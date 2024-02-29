from tkinter import *
import random as rand

def nextGame():
    print("New game")
    
def nextTurn(row,column):
    print(f"{i}{j}")
    
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

cellFrame = Frame(window)
cellFrame.pack()

for i in range(3):
    for j in range(3):
        board[i][j] = Button(cellFrame,text = "",font = ('Helvetica',16),width = 5,height = 2 ,command = nextTurn  )
        board[i][j].grid(row = i, column = j)

window.mainloop()