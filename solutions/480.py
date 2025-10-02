
def main():
    data = list(map(int, input().split()))
    n = data[0]
    coins = data[1:1+n]
    k = data[-1]
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + coins[i-1]
    
    dp = [0] * (n + 1)
    take = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = float('-inf')
        for j in range(1, min(i, k) + 1):
            current = prefix[i] - prefix[i - j] + (prefix[i - j] - dp[i - j])
            if current > dp[i]:
                dp[i] = current
                take[i] = j
    
    for i in range(k + 1, n + 1):
        dp[i] = float('-inf')
        for j in range(1, take[i - 1] + 1):
            if i - j < 0:
                break
            current = prefix[i] - prefix[i - j] + (prefix[i - j] - dp[i - j])
            if current > dp[i]:
                dp[i] = current
                take[i] = j
    
    print(dp[n])

if __name__ == "__main__":
    main()
