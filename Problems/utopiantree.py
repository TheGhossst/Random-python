def utopianTree(n):
    height = 1
    cycles = 0
    while True:
        if cycles == n:
            break
        #Sprint double
        height *= 2
        cycles += 1
        if cycles == n:
            break
        
        #Summer incement
        height += 1
        cycles += 1
        if cycles == n:
            break
    return height

print(utopianTree(0))
print(utopianTree(1))
print(utopianTree(2))
print(utopianTree(3))
print(utopianTree(4))
print(utopianTree(5))