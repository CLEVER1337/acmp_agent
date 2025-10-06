
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
        for j in range(i, m + 1):
            if dp[i][j] == 10**18:
                continue
            for k in range(j + 1, m + 1):
                add = sorted_g[i] * (k - j - 1)
                new_val = dp[i][j] + add
                if new_val < dp[i + 1][k]:
                    dp[i + 1][k] = new_val
                    prev[i + 1][k] = j
    
    min_val = 10**18
    last = -1
    for j in range(n, m + 1):
        if dp[n][j] < min_val:
            min_val = dp[n][j]
            last = j
    
    res = [0] * n
    current = last
    for i in range(n, 0, -1):
        prev_val = prev[i][current]
        res[i-1] = current - prev_val
        current = prev_val
    
    original_res = [0] * n
    for i in range(n):
        original_res[indices[i]] = res[i]
    
    print(min_val)
    print(' '.join(map(str, original_res)))

if __name__ == '__main__':
    main()
