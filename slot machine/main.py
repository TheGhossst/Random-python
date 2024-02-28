import random as ran

amount = 0

def checkBalance():
    global amount
    print("\nYour balance is : $", amount)
    if amount == 0:
        print("You have no money in your account.")
        amount += 20
        print("Devs credited $20 in your account")
        checkBalance()
    
