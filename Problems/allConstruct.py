dp = {'': []}
def allConstruct(target, wordBank):   #O(n * m^2)
    if target == '': return True
    if target in dp.keys(): return dp[target]
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if allConstruct(suffix, wordBank):
                dp[target] = True
                return True
    dp[target] = False
    return False 

print(allConstruct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'board']))
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'f', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
