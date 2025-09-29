
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
    
    max_money = 0
    for j in range(target + 1):
        if dp[j] and j <= target - j:
            current = target - 2 * j
            if current > max_money:
                max_money = current
    
    result = A + max_money
    print("{:.6f}".format(float(result)))

if __name__ == "__main__":
    main()
