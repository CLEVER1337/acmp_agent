
def main():
    with open('INPUT.TXT', 'r') as f:
        N = int(f.read().strip())
    
    if N == 0:
        result = 0
    elif N == 1:
        result = 2
    else:
        dp = [0] * (N + 1)
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, N + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        result = dp[N]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
