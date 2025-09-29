
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    m = int(data[0])
    n = int(data[1])
    matrix = []
    index = 2
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(data[index]))
            index += 1
        matrix.append(row)
    
    dp = [[0] * n for _ in range(m)]
    prev = [[-1] * n for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = matrix[i][0]
        prev[i][0] = -1
    
    for j in range(1, n):
        for i in range(m):
            min_val = float('inf')
            best_prev = -1
            
            for di in [-1, 0, 1]:
                ni = i + di
                if 0 <= ni < m:
                    if dp[ni][j-1] < min_val:
                        min_val = dp[ni][j-1]
                        best_prev = ni
                    elif dp[ni][j-1] == min_val and ni < best_prev:
                        best_prev = ni
            
            dp[i][j] = min_val + matrix[i][j]
            prev[i][j] = best_prev
    
    min_cost = float('inf')
    start_row = -1
    for i in range(m):
        if dp[i][n-1] < min_cost:
            min_cost = dp[i][n-1]
            start_row = i
    
    path = []
    current_row = start_row
    for j in range(n-1, -1, -1):
        path.append(current_row + 1)
        if j > 0:
            current_row = prev[current_row][j]
    
    path.reverse()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(' '.join(map(str, path)) + '\n')
        f.write(str(min_cost) + '\n')

if __name__ == "__main__":
    main()
