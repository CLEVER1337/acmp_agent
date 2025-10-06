
def main():
    X = input().strip()
    Y = input().strip()
    
    n = len(X)
    m = len(Y)
    
    next_pos_X = [None] * (n + 2)
    next_pos_Y = [None] * (m + 2)
    
    last_occurrence_X = {}
    last_occurrence_Y = {}
    
    for i in range(n - 1, -1, -1):
        next_pos_X[i] = last_occurrence_X.copy()
        last_occurrence_X[X[i]] = i
    
    for i in range(m - 1, -1, -1):
        next_pos_Y[i] = last_occurrence_Y.copy()
        last_occurrence_Y[Y[i]] = i
    
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    dp[n][m] = 0
    
    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if i == n and j == m:
                continue
            if dp[i][j] != -1:
                continue
            best_next = -1
            for c in 'zyxwvutsrqponmlkjihgfedcba':
                ni = n
                nj = m
                if i < n and c in next_pos_X[i]:
                    ni = next_pos_X[i][c] + 1
                if j < m and c in next_pos_Y[j]:
                    nj = next_pos_Y[j][c] + 1
                if ni != n or nj != m:
                    if dp[ni][nj] != -1:
                        if best_next == -1 or dp[ni][nj] + 1 > best_next:
                            best_next = dp[ni][nj] + 1
            dp[i][j] = best_next
    
    if dp[0][0] == -1:
        print("")
        return
        
    i, j = 0, 0
    res = []
    while i < n or j < m:
        found = False
        for c in 'zyxwvutsrqponmlkjihgfedcba':
            ni = n
            nj = m
            if i < n and c in next_pos_X[i]:
                ni = next_pos_X[i][c] + 1
            if j < m and c in next_pos_Y[j]:
                nj = next_pos_Y[j][c] + 1
            if ni != n or nj != m:
                if dp[ni][nj] != -1 and dp[ni][nj] == dp[i][j] - 1:
                    res.append(c)
                    i, j = ni, nj
                    found = True
                    break
        if not found:
            break
            
    print(''.join(res))

if __name__ == '__main__':
    main()
