
def main():
    n = int(input().strip())
    costs = []
    for _ in range(n):
        costs.append(int(input().strip()))
    
    dp = [[10**9] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(n + 1):
            if dp[i][j] == 10**9:
                continue
            if costs[i] > 100:
                if j + 1 <= n:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + costs[i])
                if j >= 1:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
            else:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + costs[i])
                if j >= 1:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
    
    min_cost = min(dp[n])
    max_coupons = -1
    for j in range(n + 1):
        if dp[n][j] == min_cost:
            max_coupons = j
    
    used = 0
    coupons = max_coupons
    for i in range(n - 1, -1, -1):
        if coupons < n and dp[i][coupons + 1] + costs[i] == dp[i + 1][coupons] and costs[i] > 100:
            used += 1
            coupons += 1
        elif coupons > 0 and dp[i][coupons - 1] == dp[i + 1][coupons]:
            coupons -= 1
    
    print(min_cost)
    print(f"{max_coupons} {used}")
