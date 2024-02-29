import random as ran
import time
from tkinter import *

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
    
    #mainWindow.destroy()
    
    def process_deposit():
        global amount
        depositedAmount = depositText.get("1.0", "end-1c")
        amount += int(depositedAmount)  
        balanceLabel.config(text = f"Balance is : {amount}",font = ("Calibri", 25))
        print("Deposit amount:", depositedAmount) 
        depositWindow.destroy()

    depositWindow = Tk()
    depositWindow.title("Deposit Money")
    depositWindow.geometry('700x400')
    
    depositLabel = Label(depositWindow, text="How much do you want to deposit", font=('Arial', 18, 'bold'))
    depositLabel.pack(side="top")
    
    depositText = Text(depositWindow, font=('Arial', 16), height=1, width=20)
    depositText.pack(side="top")
    
    depositAmount = Button(depositWindow, text="Deposit", width=10, font=("Calibri", 30), command=process_deposit)
    depositAmount.pack(side="top")
   
    depositWindow.mainloop()
        
def withdraw():
    global amount
    
    while True:
        checkBalance()
        withdrawAmount = int(input("Enter the amount to be withdrawn: "))
        
        if(withdrawAmount > 0):
            if(withdrawAmount <= amount):
                amount -= withdrawAmount
                balanceLabel.config(text = f"Balance is : {amount}",font = ("Calibri", 25))
                break
            else:
                print("Withdraw request is greater than balance try again!")
        else:
            print("Invalid input, please enter a positive integer.")
            
def slot():
    global amount
   
    while True :
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
        print("\nYou Lose\n")
        

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