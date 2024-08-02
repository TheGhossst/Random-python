MOD = 10**9 + 7
def min_cost_to_move(N, A, B):
    dp = [999] * (N + 1)
    dp[N] = A[N]

    for i in range(N, 0, -1):
        for j in range(1, i):
            cost = A[j - 1] + B[i - 1] + dp[i]
            print(f"cost -> {cost}")
            if cost < dp[j]:
                dp[j] = cost
            print(f"dp -> {dp}")

    return dp[1] % MOD

N = 5
A = [5, 4, 2, 4, 4, 1]
B = [1, 1, 4, 3, 3, 4]
print(min_cost_to_move(N, A, B))
