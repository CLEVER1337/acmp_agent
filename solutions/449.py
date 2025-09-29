
def main():
    with open("INPUT.TXT", "r") as f:
        L, N = map(int, f.readline().split())
        numbers = list(map(int, f.readline().split()))
    
    numbers.sort()
    dp = [1] * N
    
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if abs(numbers[i] - numbers[j]) <= L:
                dp[i] = max(dp[i], dp[j] + 1)
    
    result = N - max(dp) if N > 0 else 0
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
