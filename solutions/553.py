
def main():
    n = int(input().strip())
    blocks = []
    for _ in range(n):
        data = input().split()
        m = int(data[0])
        k = int(data[1])
        blocks.append((m, k))
    
    if n == 1:
        print(0)
        return
        
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + blocks[i][0] * blocks[k + 1][0] * blocks[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    
    print(dp[0][n - 1])

if __name__ == "__main__":
    main()
