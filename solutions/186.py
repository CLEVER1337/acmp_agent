
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    a.sort()
    
    dp = [0] * n
    dp[1] = a[1] - a[0]
    
    for i in range(2, n):
        if i % 2 == 1:
            dp[i] = max(dp[i-2], a[i] - a[i-1])
        else:
            dp[i] = min(max(dp[i-2], a[i] - a[i-1]), max(dp[i-3] if i >= 3 else 0, a[i] - a[i-1]))
    
    print(dp[n-1])

if __name__ == "__main__":
    main()
