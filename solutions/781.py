
def main():
    n = int(input().strip())
    if n == 1:
        print(2)
    elif n == 2:
        print(4)
    else:
        dp = [0] * (n + 1)
        dp[1] = 2
        dp[2] = 4
        dp[3] = 6
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp[n])
