def removeIslands(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()

    def dfs(r, c):
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or matrix[r][c] == 0
            or (r, c) in visited
        ):
            print(f"NO DFS! for {r},{c}")
            return
        print(f"DFS for {r},{c}")
        visited.add((r, c))
        print(f"visited - > {visited}")

        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right
        
        

    for r in range(rows):
        print(f"\nr -> {r}")
        for c in range(cols):
            print(f"c -> {c}")
            if ((r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and matrix[r][c] == 1 and (r, c) not in visited):
                print("Condition satisfied!")
                dfs(r, c)

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and (r, c) not in visited:
                matrix[r][c] = 0

    return matrix

if __name__ == "__main__":
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1],
    ]
    print(removeIslands(matrix))