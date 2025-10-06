
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
    
    total_carrots = sum(sum(row) for row in grid)
    rabbit_total = 0
    hamster_total = 0
    turn = 0
    
    while total_carrots > 0:
        if turn == 0:
            start_col = 0
            max_val = -1
            for j in range(m):
                if grid[0][j] > max_val:
                    max_val = grid[0][j]
                    start_col = j
            path = []
            carrots = 0
            row = 0
            col = start_col
            while row < n:
                if grid[row][col] > 0:
                    carrots += grid[row][col]
                    grid[row][col] = 0
                path.append(col)
                if row == n-1:
                    break
                next_cols = []
                if col-1 >= 0:
                    next_cols.append((grid[row+1][col-1], col-1))
                next_cols.append((grid[row+1][col], col))
                if col+1 < m:
                    next_cols.append((grid[row+1][col+1], col+1))
                next_cols.sort(key=lambda x: (x[0], x[1]), reverse=True)
                col = next_cols[0][1]
                row += 1
            rabbit_total += carrots
            total_carrots -= carrots
        else:
            dp = [[0] * m for _ in range(n)]
            path_dp = [[[] for _ in range(m)] for _ in range(n)]
            
            for j in range(m):
                dp[0][j] = grid[0][j]
                path_dp[0][j] = [j]
            
            for i in range(1, n):
                for j in range(m):
                    best_val = -1
                    best_path = []
                    for dj in [-1, 0, 1]:
                        prev_j = j + dj
                        if 0 <= prev_j < m:
                            if dp[i-1][prev_j] > best_val:
                                best_val = dp[i-1][prev_j]
                                best_path = path_dp[i-1][prev_j][:]
                            elif dp[i-1][prev_j] == best_val:
                                current_path = path_dp[i-1][prev_j][:]
                                if current_path > best_path:
                                    best_path = current_path
                    dp[i][j] = best_val + grid[i][j]
                    best_path.append(j)
                    path_dp[i][j] = best_path
            
            max_carrots = -1
            best_path = []
            for j in range(m):
                if dp[n-1][j] > max_carrots:
                    max_carrots = dp[n-1][j]
                    best_path = path_dp[n-1][j]
                elif dp[n-1][j] == max_carrots:
                    if path_dp[n-1][j] > best_path:
                        best_path = path_dp[n-1][j]
            
            carrots_collected = 0
            row = 0
            for col in best_path:
                carrots_collected += grid[row][col]
                grid[row][col] = 0
                row += 1
            
            hamster_total += carrots_collected
            total_carrots -= carrots_collected
        
        turn = 1 - turn
    
    print(f"{rabbit_total} {hamster_total}")

if __name__ == "__main__":
    main()
