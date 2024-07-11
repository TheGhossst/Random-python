def beautifulDays(i, j, k):
    count = 0
    for x in range(i, j + 1):
        reversed_x = int(str(x)[::-1])
        if abs(x - reversed_x) % k == 0:
            print(x)
            count += 1
    return count

i = 20
j = 23
k = 6
print(beautifulDays(i, j, k)) 
