
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        index += m
        grid.append(row)
    
    total_rabbits = 0
    total_hamsters = 0
    turn = 0
    
    while any(any(row) for row in grid):
        if turn % 2 == 0:
            start_j = 0
            max_val = -1
            for j in range(m):
                if grid[0][j] > max_val:
                    max_val = grid[0][j]
                    start_j = j
            i = 0
            j = start_j
            collected = 0
            path = []
            while i < n:
                if grid[i][j] > 0:
                    collected += grid[i][j]
                    grid[i][j] = 0
                    path.append(j)
                if i == n - 1:
                    break
                next_j_candidates = []
                for dj in [-1, 0, 1]:
                    nj = j + dj
                    if 0 <= nj < m:
                        next_j_candidates.append((grid[i+1][nj], nj))
                next_j_candidates.sort(key=lambda x: (-x[0], -x[1]))
                j = next_j_candidates[0][1]
                i += 1
            total_rabbits += collected
        else:
            dp = [[0] * m for _ in range(n)]
            path_dp = [[None] * m for _ in range(n)]
            for j in range(m):
                dp[0][j] = grid[0][j]
                path_dp[0][j] = [j]
            
            for i in range(1, n):
                for j in range(m):
                    best_val = -1
                    best_path = None
                    for dj in [-1, 0, 1]:
                        prev_j = j + dj
                        if 0 <= prev_j < m:
                            current_val = dp[i-1][prev_j] + grid[i][j]
                            if current_val > best_val:
                                best_val = current_val
                                best_path = path_dp[i-1][prev_j] + [j]
                            elif current_val == best_val:
                                candidate_path = path_dp[i-1][prev_j] + [j]
                                if candidate_path > best_path:
                                    best_val = current_val
                                    best_path = candidate_path
                    dp[i][j] = best_val
                    path_dp[i][j] = best_path
            
            max_collected = -1
            best_j = -1
            for j in range(m):
                if dp[n-1][j] > max_collected:
                    max_collected = dp[n-1][j]
                    best_j = j
                elif dp[n-1][j] == max_collected:
                    if path_dp[n-1][j] > path_dp[n-1][best_j]:
                        max_collected = dp[n-1][j]
                        best_j = j
            
            collected = max_collected
            path = path_dp[n-1][best_j]
            for i in range(n):
                j = path[i]
                grid[i][j] = 0
            total_hamsters += collected
        
        turn += 1
    
    print(f"{total_rabbits} {total_hamsters}")

if __name__ == "__main__":
    main()
