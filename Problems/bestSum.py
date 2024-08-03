dp = {0: []}
def bestSum(target, numbers):
    if target in dp.keys(): return dp[target]
    if target < 0: return None
    
    shortest_combination = None
    
    for num in numbers:
        remainder_combination = bestSum(target - num, numbers)
        
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
            
    dp[target] = shortest_combination
    return dp[target]

print(bestSum(7, [2, 3, 5]))