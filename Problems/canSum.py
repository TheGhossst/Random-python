dp = {0: True}
def canSum(target, numbers):
    if target in dp.keys(): return dp[target]
    if target < 0: return False
    
    for num in numbers:
        if canSum(target - num, numbers):
            dp[target] = True
            return True
        
    dp[target] = False    
    return False

print(canSum(300, [2, 3])) # True