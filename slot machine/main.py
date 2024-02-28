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
    

def deposit():
    global amount
    while True:
        deposit_amount = int(input("Enter the amount: "))
        if deposit_amount > 0:
            amount += deposit_amount
            print("Deposited ", deposit_amount)
            checkBalance()
            break
        else:
            print("Enter a number greater than 0")