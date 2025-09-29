
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    coins = list(map(int, data[1:1+n]))
    k = int(data[1+n])
    
    dp = [float('inf')] * (k + 1)
    dp[0] = 0
    
    for coin in coins:
        for amount in range(coin, k + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
                
    result = dp[k] if dp[k] != float('inf') else -1
    print(result)

if __name__ == "__main__":
    main()
