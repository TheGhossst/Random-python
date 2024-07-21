def binarySearch(ranked, score):
    n = len(ranked)
    low, high = 0, n
    while low < high:
        mid = (low + high) // 2
        if ranked[mid] > score:
            low = mid + 1
        else:
            high = mid
    return low + 1

def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    
    player_rank = []
    for score in player:
        player_rank.append(binarySearch(ranked, score))
    
    return player_rank

print(climbingLeaderboard([100, 90, 90, 80, 70, 60, 50, 40, 30, 20, 10], [5, 25, 50, 85]))
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))