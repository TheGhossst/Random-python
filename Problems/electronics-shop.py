#!/bin/python3
'''
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. 
Given price lists for keyboards and USB drives and a budget, find the cost to buy them. 
If it is not possible to buy both items, return -1.
'''
def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()

    max_spend = -1
    i, j = 0, len(drives) - 1

    while i < len(keyboards) and j >= 0:
        total_cost = keyboards[i] + drives[j]
        if total_cost <= b:
            max_spend = max(max_spend, total_cost)
            i += 1
        else:
            j -= 1

    return max_spend

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))
    
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    moneySpent = getMoneySpent(keyboards, drives, b)
    
    print(moneySpent)

  