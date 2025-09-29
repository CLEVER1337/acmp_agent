
def main():
    s = input().strip()
    n = len(s)
    dp = [[0] * (n+2) for _ in range(n+2)]
    dp[0][0] = 1
    
    for i in range(n):
        for balance in range(n+1):
            if dp[i][balance] == 0:
                continue
            if s[i] == '(':
                dp[i+1][balance+1] += dp[i][balance]
            elif s[i] == ')':
                if balance > 0:
                    dp[i+1][balance-1] += dp[i][balance]
            else:
                dp[i+1][balance+1] += dp[i][balance]
                if balance > 0:
                    dp[i+1][balance-1] += dp[i][balance]
    
    print(dp[n][0])

if __name__ == "__main__":
    main()
