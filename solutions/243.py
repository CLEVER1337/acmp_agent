
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    L = int(data[1])
    shops = []
    index = 2
    for i in range(n):
        P = int(data[index])
        R = int(data[index+1])
        Q = int(data[index+2])
        F = int(data[index+3])
        index += 4
        shops.append((P, R, Q, F))
    
    INF = float('inf')
    dp = [INF] * (L + 101)
    dp[0] = 0
    
    for P, R, Q, F in shops:
        new_dp = dp[:]
        for meters in range(len(dp)):
            if dp[meters] == INF:
                continue
            max_buy = min(F, len(dp) - meters - 1)
            for buy in range(1, max_buy + 1):
                total_meters = meters + buy
                if total_meters >= len(dp):
                    continue
                cost = buy * P
                if buy >= R:
                    cost = buy * Q
                new_dp[total_meters] = min(new_dp[total_meters], dp[meters] + cost)
        dp = new_dp
    
    result = INF
    for meters in range(L, len(dp)):
        result = min(result, dp[meters])
    
    if result == INF:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()
