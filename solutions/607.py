
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    m = int(data[0])
    n = int(data[1])
    k = int(data[2])
    index = 3
    grid = []
    for i in range(m):
        row = list(map(int, data[index:index+n]))
        index += n
        grid.append(row)
    
    dp = [[[-10**9] * (1 << m) for _ in range(n)] for __ in range(k+1)]
    
    for j in range(n):
        for mask in range(1 << m):
            dp[0][j][mask] = 0
    
    for j in range(n):
        for mask in range(1 << m):
            if mask & 1:
                continue
            dp[1][j][mask | 1] = max(dp[1][j][mask | 1], dp[0][j][mask] + grid[0][j] * grid[0][j+1] if j+1 < n else -10**9)
    
    for count in range(k+1):
        for j in range(n):
            for mask in range(1 << m):
                if dp[count][j][mask] == -10**9:
                    continue
                if j == n-1:
                    continue
                next_j = j + 1
                new_mask = mask >> 1
                if mask & 1 == 0:
                    dp[count][next_j][new_mask] = max(dp[count][next_j][new_mask], dp[count][j][mask])
                    if count < k:
                        if j < n-1 and (mask & 1) == 0 and (mask & 2) == 0:
                            new_mask2 = (mask >> 1) | 1
                            value = grid[0][j] * grid[0][j+1]
                            dp[count+1][next_j][new_mask2] = max(dp[count+1][next_j][new_mask2], dp[count][j][mask] + value)
                else:
                    dp[count][next_j][new_mask] = max(dp[count][next_j][new_mask], dp[count][j][mask])
    
    result = -10**9
    for mask in range(1 << m):
        result = max(result, dp[k][n-1][mask])
    
    print(result)

if __name__ == "__main__":
    main()
