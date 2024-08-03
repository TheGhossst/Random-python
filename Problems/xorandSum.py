def xorAndSum(a, b):
    a = int(a, 2)
    b = int(b, 2)
    r = 0
    for i in range(314160):
        r += a ^ b
        b *= 2
    return ((r % (10**9+7)))

# Sample Input
a = "10"
b = "1010"

# Calculate the result
result = xorAndSum(a, b)
print(result)  # Output the result
