
def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    if n <= 2:
        print(0)
        return
        
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + arr[i] * arr[j] * arr[k]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    
    print(dp[0][n-1])

if __name__ == "__main__":
    main()
