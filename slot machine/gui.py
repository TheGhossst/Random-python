import random as ran
import time
from tkinter import *
import tkinter.messagebox 

amount = 0

def checkBalance():
    global amount
    print("\nYour balance is : \033[32m$", amount, "\033[0m") 
    if amount == 0:
        print("You have no money in your account.")
        amount += 20
        print("Devs credited $20 in your account")
        balanceLabel.config(text = f"Balance is : {amount}",font = ("Calibri", 25))
        checkBalance()
    
def deposit():
    global amount
    
    def processDeposit():
        global amount
        depositedAmount = int(depositText.get("1.0", "end-1c"))
        if depositedAmount <= 0:
            tkinter.messagebox.showwarning(title="Error", message="Enter a value greater than 0")
            depositWindow.destroy()
            deposit()
        else:
            amount += int(depositedAmount)  
            balanceLabel.config(text = f"Balance is : {amount}",font = ("Calibri", 25))
            print("Deposit amount:", depositedAmount) 
            depositWindow.destroy()

    depositWindow = Tk()
    depositWindow.title("Deposit Money")
    depositWindow.geometry('700x400')
    
    depositLabel = Label(depositWindow, text="How much do you want to deposit", font=('Arial', 18, 'bold'))
    depositLabel.pack(side = "top")
    
    depositText = Text(depositWindow, font=('Arial', 16), height=1, width=20)
    depositText.pack(side = "top")
    
    depositAmount = Button(depositWindow, text="Deposit", width=10, font=("Calibri", 30), command=processDeposit)
    depositAmount.pack(side = "top")
   
    depositWindow.mainloop()
        
def withdraw():
    global amount
    
    def processWithdraw():
        global amount
        withdrawnAmount = int(withdrawText.get("1.0", "end-1c"))
        
        if withdrawnAmount <= 0:
            tkinter.messagebox.showwarning(title="Error", message="Enter a value greater than 0")
            withdrawWindow.destroy()
            withdraw()
            
        elif withdrawnAmount > amount:
            tkinter.messagebox.showwarning(title="Error", message="The amount is greater than balance")
            withdrawWindow.destroy()
            withdraw()
            
        else:
            amount -= int(withdrawnAmount)  
            balanceLabel.config(text = f"Balance is : {amount}",font = ("Calibri", 25))
            print("Withdrawn amount:", withdrawnAmount) 
            withdrawWindow.destroy()
    
    withdrawWindow = Tk()
    withdrawWindow.title("Deposit Money")
    withdrawWindow.geometry('700x400')
    
    withdrawLabel = Label(withdrawWindow, text="How much do you want to withdraw", font=('Arial', 18, 'bold'))
    withdrawLabel.pack(side = "top")
    
    withdrawText = Text(withdrawWindow, font=('Arial', 16), height=1, width=20)
    withdrawText.pack(side = "top")
    
    withdrawAmount = Button(withdrawWindow, text="Withdraw", width=10, font=("Calibri", 30), command=processWithdraw)
    withdrawAmount.pack(side = "top")
   
    withdrawWindow.mainloop()
            
def slot():
    global amount
    
    def setupItems():
        for i in range(3):
            x0 = 50 + i * 50
            y0 = 50
            x1 = x0 + 50
            y1 = y0 + 100
            rectangle = slotCanvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
            slotRectangles.append(rectangle)
            print(slotRectangles)
            
    def checkResult():
        #print(slotRectangles)
        global amount
        if slotRectangles[0] == slotRectangles[1] == slotRectangles[2]:
            tkinter.messagebox.showinfo("Result", "Jackpot!!!")
            amount *= 10
            balanceLabel1.config(text = f"Balance is : {amount}",font = ("Calibri", 25))
            balanceLabel.config(text = f"Balance is : {amount}",font = ("Calibri", 25))
        else:
            #tkinter.messagebox.showinfo("Result", "Try Again!")
            resultLabel.config(text = "Try Again",font = ("Calibri", 35))
            
    def animate(count):
        if count < 20:
            for rectangle in slotRectangles:
                temp = ran.choice(slotItems)
                print(temp)
                slotCanvas.itemconfig(rectangle,fill =temp)
            slotWindow.after(100,animate, count + 1)
            print(slot)
        else:
            checkResult()
            #spinButton.config(state = NORMAL)
        
    def spin():
        global amount
        if amount > 0:
           # spinButton.config(state = DISABLED)
            amount -= 10
            balanceLabel1.config(text = f"Balance is : {amount}",font = ("Calibri", 25))
            balanceLabel.config(text = f"Balance is : {amount}",font = ("Calibri", 25))
            animate(0)
        else:
            tkinter.messagebox.showwarning(title="Error", message="You dont have enough money to spin")
            
            
    slotWindow = Tk()
    slotWindow.title("Slot Machine")
    slotWindow.geometry('700x400')
    
    balanceLabel1 = Label(slotWindow,text = f"The balance is : {amount}",font = ("Calibri", 25) )
    balanceLabel1.pack(side = "top")
    
    slotCanvas = Canvas(slotWindow,width = 200,height = 200)
    slotCanvas.pack(side = "top")
    
    slotItems = ["red", "green", "blue", "yellow", "purple"]
    slotRectangles = []
    setupItems()
    
    spinButton = Button(slotWindow,text = "Spin!",command = spin)
    spinButton.pack(side = "top")
    
    resultLabel = Label(slotWindow,text = "")
    resultLabel.pack(side = "top")
    
    slotWindow.mainloop()
   
mainWindow = Tk()
mainWindow.geometry("800x800")
mainWindow.title("Slot Machine main page")

nameLabel = Label(mainWindow, text="Ghost Slots",font = ("Calibri", 45))
nameLabel.pack(side ="top")

balanceLabel = Label(mainWindow,text = f"Balance is : {amount}",font = ("Calibri", 25))
balanceLabel.pack(side="top", anchor="nw")

depositButton = Button(mainWindow,text = "Deposit",width = 10,font = ("Calibri", 30), command = deposit)
depositButton.pack(side = "top",anchor = "center")

withdrawButton = Button(mainWindow,text = "Withdraw",width = 10,font = ("Calibri", 30), command = withdraw)
withdrawButton.pack(side = "top",anchor = "center")

slotButton = Button(mainWindow,text = "Play slots",width = 10,font = ("Calibri", 30), command = slot)
slotButton.pack(side = "top",anchor = "center")

mainWindow.mainloop()