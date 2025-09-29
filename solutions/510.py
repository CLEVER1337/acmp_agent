
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.read().strip())
    
    if n % 2 != 0:
        result = 0
    else:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(2, n + 1, 2):
            dp[i] = 3 * dp[i - 2]
            for j in range(4, i + 1, 2):
                dp[i] += 2 * dp[i - j]
    
        result = dp[n]
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
