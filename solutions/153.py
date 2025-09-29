
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    m = int(data[1])
    coins = list(map(int, data[2:2+m]))
    
    coins.sort()
    total = sum(coins) * 2
    
    if total < n:
        print(-1)
        return
        
    dp = {}
    dp[0] = 0
    
    for coin in coins:
        new_dp = dp.copy()
        for amount, count in dp.items():
            for cnt in range(1, 3):
                new_amount = amount + coin * cnt
                new_count = count + cnt
                if new_amount > n:
                    continue
                if new_amount not in new_dp or new_count < new_dp[new_amount]:
                    new_dp[new_amount] = new_count
        dp = new_dp
    
    if n in dp:
        print(dp[n])
    else:
        print(0)

if __name__ == "__main__":
    main()
