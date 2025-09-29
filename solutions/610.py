
def main():
    with open('INPUT.TXT', 'r') as f:
        r, c = map(int, f.read().split())
    
    n = r * c
    if n % 2 != 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('0')
        return
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if i % c != 0:
            if i > c:
                dp[i] += dp[i - c - 1]
            if i >= 2:
                dp[i] += dp[i - 2]
        if i >= c:
            dp[i] += dp[i - c]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[n]))

if __name__ == '__main__':
    main()
