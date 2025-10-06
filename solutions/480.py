
def main():
    data = list(map(int, input().split()))
    n = data[0]
    coins = data[1:1+n]
    k = data[1+n]
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + coins[i-1]
    
    dp = [0] * (n + 1)
    take = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = 0
        take[i] = float('inf')
        for j in range(1, min(i, k) + 1):
            total = prefix[i] - prefix[i - j]
            if j > take[i - j]:
                continue
            candidate = total + (prefix[i - j] - prefix[i - j - take[i - j]] - dp[i - j]) if i - j - take[i - j] >= 0 else total
            if candidate > dp[i]:
                dp[i] = candidate
                take[i] = j
            elif candidate == dp[i]:
                take[i] = min(take[i], j)
    
    print(dp[n])

if __name__ == "__main__":
    main()
