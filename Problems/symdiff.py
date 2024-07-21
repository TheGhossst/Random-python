def sym(a, b):
    c = []
    for x in a:
        if x not in b:
            c.append(x)
        
    for x in b:
        if x not in a:
            c.append(x)
    
    print(c)
    
sym([1,2,3], [2,3,4])