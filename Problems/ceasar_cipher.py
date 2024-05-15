def caesar_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            code = ord(char)
            code += shift
            if char.islower():
                code = (code - ord('a')) % 26 + ord('a')
            else:
                code = (code - ord('A')) % 26 + ord('A')
            result += chr(code)
        else:
            result += char
    
    return result

def caesar_decrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            code = ord(char)
            code -= shift
            if char.islower():
                code = (code - ord('a')) % 26 + ord('a')
            else:
                code = (code - ord('A')) % 26 + ord('A')
            result += chr(code)
        else:
            result += char
    
    return result

plaintext = input("Enter a string: ")
shift = int(input("Enter the displacement/Shift : "))

encrypted = caesar_encrypt(plaintext, shift)
print("Encrypted text:", encrypted)  

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted text:", decrypted)  