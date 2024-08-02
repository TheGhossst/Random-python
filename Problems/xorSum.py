def xorSum(x, A):
    res = 0
    for i in range(1, x):
        s = 0
        for x in A:
            s += i ^ x
            print(f"s-> {s}\ni-> {i}\nx->{x}\n")
        if s > res:
            res = s
    return res

print(xorSum(7, [1, 6, 3])) # Output: 14