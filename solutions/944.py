
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
        coins = list(map(int, f.readline().split()))
        k = int(f.readline().strip())
        sums = list(map(int, f.readline().split()))
    
    max_sum = max(sums)
    dp = [False] * (max_sum + 1)
    dp[0] = True
    
    for coin in coins:
        for j in range(coin, max_sum + 1):
            if dp[j - coin]:
                dp[j] = True
    
    result = []
    for s in sums:
        result.append('1' if dp[s] else '0')
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(" ".join(result))

if __name__ == "__main__":
    main()
