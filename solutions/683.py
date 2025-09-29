
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    
    if n <= 2:
        print(0)
        return
        
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n):
        for i in range(0, n - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                cost = a[i] * a[k] * a[j] + dp[i][k] + dp[k][j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    
    print(dp[0][n-1])

if __name__ == "__main__":
    main()
