
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        costs = [int(f.readline().strip()) for _ in range(n)]
    
    dp = [[float('inf')] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(n + 1):
            if dp[i][j] == float('inf'):
                continue
                
            current_cost = costs[i]
            if current_cost > 100:
                if j + 1 <= n:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + current_cost)
            else:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + current_cost)
                
            if j > 0:
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
    
    min_cost = float('inf')
    min_j = 0
    for j in range(n + 1):
        if dp[n][j] < min_cost:
            min_cost = dp[n][j]
            min_j = j
    
    coupons_left = min_j
    coupons_used = 0
    
    j = coupons_left
    for i in range(n, 0, -1):
        if j < n and dp[i][j] == dp[i - 1][j + 1]:
            coupons_used += 1
            j += 1
        elif j > 0 and dp[i][j] == dp[i - 1][j - 1] + costs[i - 1]:
            j -= 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{min_cost}\n")
        f.write(f"{coupons_left} {coupons_used}\n")

if __name__ == "__main__":
    main()
