
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    g = list(map(int, data[2:2+n]))
    
    indices = sorted(range(n), key=lambda i: g[i], reverse=True)
    sorted_g = [g[i] for i in indices]
    
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    prev = [[-1] * (m + 1) for _ in range(n + 1)]
    
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(i, m + 1):
            for k in range(1, j - i + 2):
                cost = sorted_g[i - 1] * (i - 1)
                if dp[i - 1][j - k] + cost < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - k] + cost
                    prev[i][j] = k
    
    result = [0] * n
    j = m
    for i in range(n, 0, -1):
        k = prev[i][j]
        result[indices[i - 1]] = k
        j -= k
    
    print(dp[n][m])
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
