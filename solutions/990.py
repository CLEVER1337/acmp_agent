
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    g = list(map(int, data[2:2+n]))
    
    indices = sorted(range(n), key=lambda i: g[i])
    sorted_g = [g[i] for i in indices]
    
    dp = [[10**18] * (m + 1) for _ in range(n + 1)]
    prev = [[-1] * (m + 1) for _ in range(n + 1)]
    
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j] == 10**18:
                continue
            for k in range(1, m - j + 1):
                if j + k > m:
                    break
                cost = dp[i][j] + (n - i - 1) * sorted_g[i] * k
                if cost < dp[i + 1][j + k]:
                    dp[i + 1][j + k] = cost
                    prev[i + 1][j + k] = k
    
    result = [0] * n
    j = m
    for i in range(n - 1, -1, -1):
        k = prev[i + 1][j]
        result[i] = k
        j -= k
    
    original_result = [0] * n
    for idx, pos in enumerate(indices):
        original_result[pos] = result[idx]
    
    print(dp[n][m])
    print(' '.join(map(str, original_result)))

if __name__ == '__main__':
    main()
