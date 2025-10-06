
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    money = list(map(int, data[1:1+n]))
    A = int(data[1+n])
    
    total = sum(money)
    target = total + A
    
    dp = [False] * (target + 1)
    dp[0] = True
    
    for m in money:
        for j in range(target, m - 1, -1):
            if dp[j - m]:
                dp[j] = True
    
    max_gorgona = 0
    for s in range(target, -1, -1):
        if dp[s]:
            half = s / 2.0
            remaining = target - s
            gorgona_total = A + remaining + half
            if gorgona_total > max_gorgona:
                max_gorgona = gorgona_total
    
    print("{:.6f}".format(max_gorgona))

if __name__ == "__main__":
    main()
