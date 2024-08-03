def canConstructRecursive(target, wordBank): # O(n^m)
    if target == '': return True
    #if target not in wordBank: return False
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            #print(f"word -> {word}\nSuffix -> {suffix}")
            if canConstructRecursive(suffix, wordBank):
                return True
    return False 

dp = {}
def canConstructDp(target, wordBank):   #O(n * m^2)
    if target == '': return True
    if target in dp.keys(): return dp[target]
    
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstructDp(suffix, wordBank):
                dp[target] = True
                return True
    dp[target] = False
    return False 

print(canConstructRecursive("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'board']))
print(canConstructRecursive("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'f', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
print("\n")
print(canConstructDp("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'board']))
print(canConstructDp("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', 'f', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))