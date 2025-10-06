
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1
    grid = []
    for i in range(N):
        row = list(map(int, data[idx:idx+N]))
        idx += N
        grid.append(row)
    
    if K == 1:
        print(grid[0][0])
        return
        
    max_val = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > max_val:
                max_val = grid[i][j]
                
    if K % 2 == 1:
        steps = (K + 1) // 2
    else:
        steps = K // 2
        
    if steps == 0:
        print(grid[0][0])
        return
        
    dp_prev = [[-10**18] * N for _ in range(N)]
    dp_prev[0][0] = grid[0][0]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for step in range(1, steps):
        dp_curr = [[-10**18] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if dp_prev[i][j] == -10**18:
                    continue
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < N:
                        new_val = dp_prev[i][j] + grid[ni][nj]
                        if new_val > dp_curr[ni][nj]:
                            dp_curr[ni][nj] = new_val
        dp_prev = dp_curr
        
    max_sum = -10**18
    if K % 2 == 1:
        for i in range(N):
            for j in range(N):
                if dp_prev[i][j] != -10**18:
                    total = dp_prev[i][j] * 2 - grid[i][j]
                    if total > max_sum:
                        max_sum = total
    else:
        for i in range(N):
            for j in range(N):
                if dp_prev[i][j] != -10**18:
                    total = dp_prev[i][j] * 2
                    if total > max_sum:
                        max_sum = total
                        
    if max_sum < max_val * K:
        max_sum = max_val * K
        
    print(max_sum)

if __name__ == "__main__":
    main()
