
def main():
    with open("INPUT.TXT", "r") as f:
        n, k = map(int, f.readline().split())
    
    dp = [[0] * (n + 2) for _ in range(2 * n + 1)]
    dp[0][0] = 1
    
    for i in range(1, 2 * n + 1):
        for j in range(n + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < n:
                dp[i][j] += dp[i - 1][j + 1]
    
    result = 0
    for i in range(2 * n + 1):
        if dp[i][k] > 0:
            result += dp[i][k] * dp[2 * n - i][0]
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
