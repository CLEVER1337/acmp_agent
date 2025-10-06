
def main():
    n = int(input().strip())
    if n == 1:
        print(2)
        return
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 5
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] * 2 + dp[i-2] + dp[i-3]) % 1000000007
    print(dp[n])

if __name__ == "__main__":
    main()
