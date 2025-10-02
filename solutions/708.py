
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
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
    
    while any(any(cell != -1 for cell in row) for row in grid):
        if turn % 2 == 0:
            start_col = -1
            max_val = -1
            for j in range(m):
                if grid[0][j] > max_val and grid[0][j] != -1:
                    max_val = grid[0][j]
                    start_col = j
                elif grid[0][j] == max_val and grid[0][j] != -1:
                    if j > start_col:
                        start_col = j
            
            if start_col == -1:
                break
                
            collected = 0
            current_col = start_col
            path = []
            for i in range(n):
                if grid[i][current_col] == -1:
                    break
                collected += grid[i][current_col]
                grid[i][current_col] = -1
                path.append(current_col)
                
                if i < n - 1:
                    next_cols = []
                    for dj in [-1, 0, 1]:
                        nj = current_col + dj
                        if 0 <= nj < m and grid[i+1][nj] != -1:
                            next_cols.append((grid[i+1][nj], nj))
                    
                    if not next_cols:
                        break
                    
                    next_cols.sort(key=lambda x: (-x[0], -x[1]))
                    current_col = next_cols[0][1]
            
            total_rabbits += collected
            
        else:
            dp = [[-1] * m for _ in range(n)]
            path_choice = [[-1] * m for _ in range(n)]
            
            for j in range(m):
                if grid[n-1][j] != -1:
                    dp[n-1][j] = grid[n-1][j]
                    path_choice[n-1][j] = j
            
            for i in range(n-2, -1, -1):
                for j in range(m):
                    if grid[i][j] == -1:
                        continue
                    max_next = -1
                    best_next_col = -1
                    for dj in [-1, 0, 1]:
                        nj = j + dj
                        if 0 <= nj < m and dp[i+1][nj] != -1:
                            if dp[i+1][nj] > max_next:
                                max_next = dp[i+1][nj]
                                best_next_col = nj
                            elif dp[i+1][nj] == max_next:
                                if best_next_col != -1 and nj > best_next_col:
                                    best_next_col = nj
                    
                    if max_next != -1:
                        dp[i][j] = grid[i][j] + max_next
                        path_choice[i][j] = best_next_col
                    else:
                        dp[i][j] = grid[i][j]
                        path_choice[i][j] = j
            
            max_start_val = -1
            start_col = -1
            for j in range(m):
                if dp[0][j] > max_start_val and grid[0][j] != -1:
                    max_start_val = dp[0][j]
                    start_col = j
                elif dp[0][j] == max_start_val and grid[0][j] != -1:
                    if j > start_col:
                        start_col = j
            
            if start_col == -1:
                break
                
            collected = 0
            current_col = start_col
            for i in range(n):
                if grid[i][current_col] == -1:
                    break
                collected += grid[i][current_col]
                grid[i][current_col] = -1
                if i < n - 1:
                    current_col = path_choice[i][current_col]
            
            total_hamsters += collected
            
        turn += 1
        
    print(f"{total_rabbits} {total_hamsters}")

if __name__ == "__main__":
    main()
