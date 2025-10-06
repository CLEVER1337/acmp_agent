
def main():
    r, c = map(int, input().split())
    n = r * c
    dp = [[0] * (1 << n) for _ in range(n)]
    
    for mask in range(1 << n):
        if mask & 1:
            dp[0][mask] = 1
    
    for pos in range(1, n):
        for mask in range(1 << n):
            if not dp[pos-1][mask]:
                continue
            i, j = pos // c, pos % c
            prev_mask = mask
            up_mask = 1 << (pos - c) if i > 0 else 0
            left_mask = 1 << (pos - 1) if j > 0 else 0
            current_mask = 1 << pos
            
            if j == 0:
                up_connected = bool(prev_mask & up_mask)
                if up_connected:
                    new_mask = prev_mask & ~up_mask
                    dp[pos][new_mask] += dp[pos-1][prev_mask]
                else:
                    new_mask = prev_mask | current_mask
                    dp[pos][new_mask] += dp[pos-1][prev_mask]
            else:
                up_connected = bool(prev_mask & up_mask)
                left_connected = bool(prev_mask & left_mask)
                
                if up_connected and left_connected:
                    new_mask = prev_mask & ~up_mask & ~left_mask
                    dp[pos][new_mask] += dp[pos-1][prev_mask]
                elif up_connected and not left_connected:
                    new_mask1 = prev_mask & ~up_mask
                    new_mask2 = prev_mask | current_mask
                    dp[pos][new_mask1] += dp[pos-1][prev_mask]
                    dp[pos][new_mask2] += dp[pos-1][prev_mask]
                elif not up_connected and left_connected:
                    new_mask1 = prev_mask & ~left_mask
                    new_mask2 = prev_mask | current_mask
                    dp[pos][new_mask1] += dp[pos-1][prev_mask]
                    dp[pos][new_mask2] += dp[pos-1][prev_mask]
                else:
                    new_mask = prev_mask | current_mask
                    dp[pos][new_mask] += dp[pos-1][prev_mask]
    
    result = dp[n-1][0]
    print(result)

if __name__ == "__main__":
    main()
