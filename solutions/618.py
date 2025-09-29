
def main():
    n = int(input())
    dp = [0] * (n + 1)
    partition = [[] for _ in range(n + 1)]
    
    dp[0] = 1
    partition[0] = []
    
    for i in range(1, n + 1):
        max_val = 0
        best_part = []
        for j in range(1, i + 1):
            if j > i:
                break
            prev = i - j
            if prev == 0:
                candidate = 1
                cand_part = [j]
            else:
                if len(partition[prev]) > 0 and j <= partition[prev][0]:
                    candidate = dp[prev] + dp[prev]
                    for k in range(len(partition[prev])):
                        if k == 0:
                            continue
                        candidate += dp[prev - sum(partition[prev][:k])]
                    cand_part = [j] + partition[prev]
                else:
                    continue
            if candidate > max_val:
                max_val = candidate
                best_part = cand_part
        dp[i] = max_val
        partition[i] = best_part
    
    print(dp[n])
    print(' '.join(map(str, partition[n])))

if __name__ == '__main__':
    main()
