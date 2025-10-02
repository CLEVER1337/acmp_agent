
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    m = int(data[0])
    n = int(data[1])
    k = int(data[2])
    
    board = []
    index = 3
    for i in range(m):
        row = list(map(int, data[index:index+n]))
        index += n
        board.append(row)
    
    if m == 1:
        dp = [[-10**18] * (k+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(k+1):
                if dp[i][j] == -10**18:
                    continue
                if dp[i+1][j] < dp[i][j]:
                    dp[i+1][j] = dp[i][j]
                if j < k and i+1 < n:
                    val = board[0][i] * board[0][i+1]
                    if dp[i+2][j+1] < dp[i][j] + val:
                        dp[i+2][j+1] = dp[i][j] + val
        print(dp[n][k])
        return
    
    dp_prev = [[-10**18] * (k+1) for _ in range(1<<m)]
    dp_prev[0][0] = 0
    
    for col in range(n):
        dp_next = [[-10**18] * (k+1) for _ in range(1<<m)]
        
        for mask in range(1<<m):
            for cnt in range(k+1):
                if dp_prev[mask][cnt] == -10**18:
                    continue
                
                def dfs(row, current_mask, current_sum, domino_count):
                    if row == m:
                        if dp_next[current_mask][domino_count] < current_sum:
                            dp_next[current_mask][domino_count] = current_sum
                        return
                    
                    if current_mask & (1 << row):
                        dfs(row+1, current_mask, current_sum, domino_count)
                        return
                    
                    dfs(row+1, current_mask, current_sum, domino_count)
                    
                    if domino_count < k:
                        if row < m-1 and not (current_mask & (1 << (row+1))):
                            val = board[row][col] * board[row+1][col]
                            dfs(row+2, current_mask | (1<<row) | (1<<(row+1)), current_sum + val, domino_count+1)
                        
                        if col < n-1 and not (mask & (1 << row)):
                            val = board[row][col] * board[row][col+1]
                            dfs(row+1, current_mask | (1<<row), current_sum + val, domino_count+1)
                
                dfs(0, mask, dp_prev[mask][cnt], cnt)
        
        dp_prev = dp_next
    
    result = -10**18
    for mask in range(1<<m):
        if dp_prev[mask][k] > result:
            result = dp_prev[mask][k]
    print(result)

if __name__ == "__main__":
    main()
