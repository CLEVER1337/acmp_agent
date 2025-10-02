
def main():
    n = int(input().strip())
    dp = [0] * (n + 1)
    parts = [[] for _ in range(n + 1)]
    
    dp[0] = 1
    parts[0] = []
    
    for i in range(1, n + 1):
        max_val = 0
        best_part = []
        for j in range(1, i + 1):
            if i - j < 0:
                continue
            prev = i - j
            if not parts[prev] or j <= parts[prev][-1]:
                candidate = dp[prev] + sum(1 for x in parts[prev] if x >= j) + 1
                if candidate > max_val:
                    max_val = candidate
                    best_part = parts[prev] + [j]
        dp[i] = max_val
        parts[i] = best_part
    
    result = parts[n]
    print(dp[n])
    print(' '.join(map(str, sorted(result, reverse=True))))

if __name__ == "__main__":
    main()
