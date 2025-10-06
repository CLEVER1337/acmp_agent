
def main():
    n = int(input().strip())
    mat = []
    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        if dp[mask] == float('inf'):
            continue
        i = 0
        while i < n and (mask >> i) & 1:
            i += 1
        if i >= n:
            continue
        new_mask = mask | (1 << i)
        dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
        for j in range(i + 1, n):
            if not (mask >> j) & 1 and mat[i][j] == 0:
                new_mask2 = new_mask | (1 << j)
                dp[new_mask2] = min(dp[new_mask2], dp[mask] + 1)
    
    print(dp[(1 << n) - 1])

if __name__ == '__main__':
    main()
