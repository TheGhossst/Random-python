
def isBalanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for x in s:
        if x in bracket_map.values():
            stack.append(x)
        elif x in bracket_map.keys():
            if stack and stack[-1] == bracket_map[x]:
                stack.pop()
            else:
                return "NO"
    
    return "YES" if not stack else "NO"

    
print(isBalanced("{(([])[])[]]}"))
