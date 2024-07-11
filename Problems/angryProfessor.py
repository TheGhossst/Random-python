def angryProfessor(k, a): #k -> min number of students on time to continue the class
    arrivedOnTime = 0
    for x in a:
        if x <= 0:
            arrivedOnTime += 1
    
    if arrivedOnTime < k:
        return "YES"
    return "NO"

print(angryProfessor(3 ,[-1,-3,4,2]))
print(angryProfessor(2 ,[0,-1,2,1]))