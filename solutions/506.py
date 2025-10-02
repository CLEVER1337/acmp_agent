
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K1 = int(data[1])
    K2 = int(data[2])
    S = int(data[3])
    
    from decimal import Decimal, getcontext
    getcontext().prec = 10000
    
    def probability(n, i, j):
        if i >= n:
            return Decimal(1)
        if j >= n:
            return Decimal(0)
        
        dp = [[Decimal(0) for _ in range(n)] for __ in range(n)]
        
        for a in range(n-1, -1, -1):
            for b in range(n-1, -1, -1):
                if a == n-1 and b < n-1:
                    dp[a][b] = Decimal(1)
                elif b == n-1 and a < n-1:
                    dp[a][b] = Decimal(0)
                else:
                    dp[a][b] = (dp[a+1][b] + dp[a][b+1]) / Decimal(2)
        
        return dp[i][j]
    
    prob = probability(N, K1, K2)
    petya_coins = (S * prob).to_integral_value(rounding='ROUND_HALF_UP')
    vasya_coins = S - petya_coins
    
    print(f"{petya_coins} {vasya_coins}")

if __name__ == "__main__":
    main()
