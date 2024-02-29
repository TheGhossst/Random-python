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
            withdraw()
            
        elif withdrawnAmount > amount:
            tkinter.messagebox.showwarning(title="Error", message="The amount is greater than balance")
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
            
    slotWindow = Tk()
    slotWindow.title("Slot Machine")
    slotWindow.geometry('700x400')
    
    slotCanvas = Canvas(slotWindow,width = 200,height = 200)
    slotCanvas.pack(side = "top")
    
    slotItems = ["red", "green", "blue", "yellow", "purple"]
    slotRectangles = []
    setupItems()
    
    slotWindow.mainloop()
   
    '''while True :
        bettingAmmount = int(input("Enter the amount you wish to bet for: "))
        if (bettingAmmount > amount):
            print("Not enough money to bet")
            checkBalance()
        elif bettingAmmount == 0:
            print("Betting amount cant be  zero. Please enter an amount greater than zero.")
        else:
            print(f"\n{bettingAmmount} is being placed on slots\n")
            amount -= bettingAmmount
            break
        
    symbols = ['Banana', 'Apple', 'Carrot', 'Guava']
    
    slot1 = ran.choice(symbols)
    slot2 = ran.choice(symbols)
    slot3 = ran.choice(symbols)
    
    print("Slot")
    print(slot1, "||", end=' ')
    print(slot2, "||", end=' ')
    time.sleep(1)  
    print(slot3)
    
    if slot1 == slot2 == slot3:
        print("\nJackpot!!!\n")
        amount +=bettingAmmount*10
        print("10x has been credited")
        
    elif slot1 == slot2 != slot3 or slot1 != slot2 == slot3 or slot1 == slot3 != slot2:
        print("\nPartial Win\n")
        amount += bettingAmmount + 10
        print("+10 has been credited")
        
    else:
        print("\nYou Lose\n")'''
        

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