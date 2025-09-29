
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    
    packs = []
    index = 2
    for i in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        packs.append((a, b))
    
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for a, b in packs:
        for j in range(n + 1):
            if dp[j] != float('inf'):
                next_j = j + a
                if next_j > n:
                    next_j = n
                if dp[next_j] > dp[j] + b:
                    dp[next_j] = dp[j] + b
    
    print(dp[n])

if __name__ == "__main__":
    main()
