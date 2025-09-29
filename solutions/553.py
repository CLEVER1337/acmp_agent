
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        blocks = []
        for i in range(n):
            m, k = map(int, f.readline().split())
            blocks.append((m, k))
    
    if n == 1:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    dp = [[0] * n for _ in range(n)]
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + blocks[i][0] * blocks[k+1][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[0][n-1]))

if __name__ == '__main__':
    main()
