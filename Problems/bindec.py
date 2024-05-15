def bintodec(binary):
    decimal = 0
    for digit in binary:
        if digit not in '01':
            raise ValueError("Invalid binary number")
        decimal = decimal * 2 + int(digit)
    return decimal

def dectobin(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

binary_num = input("Enter a binary number : ")
decimal_num = int(input("Enter a decimal number: "))

decimal_from_binary = bintodec(binary_num)
print(f"Binary {binary_num} in decimal: {decimal_from_binary}")  

binary_from_decimal = dectobin(decimal_num)
print(f"Decimal {decimal_num} in binary: {binary_from_decimal}")  