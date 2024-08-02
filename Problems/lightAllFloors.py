def min_cost_to_light_floors(n, m, cost):
    res = [[0] * m for _ in range(n)]
    
    for j in range(m):
        res[0][j] = cost[0][j]
        
    for i in range(1, n):
        for j in range(m):
            min_cost = 999999
            for k in range(m):
                if k != j:
                    min_cost = min(min_cost, res[i-1][k])
               
            res[i][j] = cost[i][j] + min_cost
    min_total_cost = min(res[n-1])
    print(f"table -> {res}")
    return min_total_cost

cost = [
    [1, 2, 3],
    [1, 10, 6],
    [7, 8, 9],
    [10,1,3]
]

print(min_cost_to_light_floors(4, 3, cost))
