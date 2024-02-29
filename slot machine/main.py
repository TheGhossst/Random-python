import random as ran
import time

amount = 0

def checkBalance():
    global amount
    print("\nYour balance is : \033[32m$", amount, "\033[0m") 
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
            
def withdraw():
    global amount
    
    while True:
        checkBalance()
        withdrawAmount = int(input("Enter the amount to be withdrawn: "))
        
        if(withdrawAmount > 0):
            if(withdrawAmount <= amount):
                amount -= withdrawAmount
                print("\nYour new balance is : \033[32m$", amount, "\033[0m") 
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
        
def main():
    global amount
    print("Slot machine")
    
    while True:
        print("\n1. Deposit\n2. Check Balance\n3. Withdraw\n4. Play Slot\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            deposit()
        elif choice == '2':
            checkBalance()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            slot()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter again.")


if __name__ == "__main__":
    main()
