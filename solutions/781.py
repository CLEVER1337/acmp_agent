
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
    
    if n == 1:
        result = 2
    elif n == 2:
        result = 4
    else:
        dp = [0] * (n + 1)
        dp[1] = 2
        dp[2] = 4
        dp[3] = 6
        
        for i in range(4, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        result = dp[n]
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
