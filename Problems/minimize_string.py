def minimize_binary_string(S):
    stack = []
    
    for char in S:
        if stack and stack[-1] == '1' and char == '0':
            stack.pop()
            while stack and stack[-1] == '1':
                stack.pop()
            stack.append('0')
        else:
            stack.append(char)

    return ''.join(stack)

print(minimize_binary_string("0000111111"))  # Output: "0000111111"
print(minimize_binary_string("1111111"))    # Output: "1111111"
print(minimize_binary_string("110"))        # Output: "0"
