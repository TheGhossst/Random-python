def sockMerchant(n, ar):
    d = {}
    
    for x in ar:
        if x not in d.keys():
            d[x] = 1
        else:
            d[x] += 1
            
    print(d)
    
    count = 0
    for x in d.values():
        print(f"value -> {x}")
        if x % 2 == 0:
            count += x // 2
        else:
            count += (x - 1) // 2
        print(f"count -> {count}")
    return count

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    
    print(result)

