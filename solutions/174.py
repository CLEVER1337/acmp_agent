
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    money = list(map(int, data[1:1+n]))
    A = int(data[1+n])
    
    total = sum(money)
    dp = [False] * (total + 1)
    dp[0] = True
    
    for m in money:
        for j in range(total, m - 1, -1):
            if dp[j - m]:
                dp[j] = True
    
    max_money = 0
    for s in range(total + 1):
        if dp[s]:
            current = A + total - s
            if current > max_money:
                max_money = current
    
    print("{:.6f}".format(max_money / 2.0))

if __name__ == "__main__":
    main()
