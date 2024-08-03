dp = {0: []}
def canSum(target, numbers):
    if target in dp.keys(): return dp[target]
    if target < 0: return None
    
    for num in numbers:
        res = canSum(target - num, numbers)
        if  res is not None:
            dp[target] = res + [num]
            return dp[target]
        
    dp[target] = None
    return None

print(canSum(300, [2, 3, 5]))