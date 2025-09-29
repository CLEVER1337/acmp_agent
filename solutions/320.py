
def main():
    with open("INPUT.TXT", "r") as f:
        M, N = map(int, f.read().split())
    
    if M == N:
        print(2)
        return
        
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, N + 1):
        dp[i] = dp[i - 1]
        if i >= M:
            dp[i] += dp[i - M]
            
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(dp[N]))

if __name__ == "__main__":
    main()
