
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
        p = int(data[index])
        r = int(data[index+1])
        q = int(data[index+2])
        f = int(data[index+3])
        index += 4
        shops.append((p, r, q, f))
    
    INF = float('inf')
    dp = [INF] * (L + 101)
    dp[0] = 0
    
    for p, r, q, f in shops:
        new_dp = dp[:]
        for meters in range(len(dp)):
            if dp[meters] == INF:
                continue
            for buy in range(1, f + 1 if f > 0 else [1]):
                total_meters = meters + buy
                if total_meters >= len(dp):
                    continue
                cost = buy * p
                if buy >= r:
                    cost = buy * q
                new_dp[total_meters] = min(new_dp[total_meters], dp[meters] + cost)
        dp = new_dp
    
    min_cost = INF
    for meters in range(L, len(dp)):
        min_cost = min(min_cost, dp[meters])
    
    if min_cost == INF:
        print(-1)
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
