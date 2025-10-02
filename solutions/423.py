
def main():
    with open('INPUT.TXT', 'r') as f:
        s = f.readline().strip()
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        
        if i >= 2:
            num = int(s[i-2:i])
            if 10 <= num <= 33:
                dp[i] += dp[i-2]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[n]))

if __name__ == '__main__':
    main()
