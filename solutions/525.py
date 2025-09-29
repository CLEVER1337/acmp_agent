
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.read().strip())
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    power = 1
    while power <= n:
        for i in range(power, n + 1):
            dp[i] += dp[i - power]
        power *= 2
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(dp[n]))

if __name__ == "__main__":
    main()
