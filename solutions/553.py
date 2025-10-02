
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        blocks = []
        for _ in range(n):
            data = f.readline().split()
            blocks.append((int(data[0]), int(data[1])))
    
    m = [blocks[i][0] for i in range(n)]
    k = [blocks[i][1] for i in range(n)]
    
    dp = [[0] * n for _ in range(n)]
    
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')
            for p in range(i, j):
                cost = dp[i][p] + dp[p+1][j] + m[i] * k[p+1] * k[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[0][n-1]))

if __name__ == '__main__':
    main()
