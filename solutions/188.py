
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.read().strip())
    
    if n == 1:
        result = 0
    elif n == 2:
        result = 1
    else:
        dp = [0] * (n + 1)
        dp[1] = 0
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
        result = dp[n]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
