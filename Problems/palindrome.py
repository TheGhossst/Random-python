

def palindrome(string): #O(n)
    return string == string[::-1]

def palindrome1(string): #O(n)
    left = 0
    right = len(string) - 1
    
    while(left < right):
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1
        
    return True
    
if __name__ == "__main__":
    string = input("Enter a string: ")
    if palindrome(string):
        print("Palindrome")
    else:
        print("Not a palindrome")
    
    if palindrome1(string):
        print("Palindrome")
    else:
        print("Not a palindrome")