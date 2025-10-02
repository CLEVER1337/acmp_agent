
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    coins = list(map(int, data[1:1+n]))
    k = int(data[1+n])
    
    dp = [float('inf')] * (k + 1)
    dp[0] = 0
    
    for coin in coins:
        for j in range(coin, k + 1):
            if dp[j - coin] != float('inf'):
                dp[j] = min(dp[j], dp[j - coin] + 1)
                
    result = dp[k] if dp[k] != float('inf') else -1
    print(result)

if __name__ == "__main__":
    main()
