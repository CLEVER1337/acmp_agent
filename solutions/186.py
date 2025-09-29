
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().split()))
    
    arr.sort()
    dp = [0] * n
    dp[0] = 0
    dp[1] = arr[1] - arr[0]
    
    for i in range(2, n):
        option1 = dp[i-1] + arr[i] - arr[i-1]
        option2 = dp[i-2] + arr[i] - arr[i-1]
        dp[i] = min(option1, option2)
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[-1]))

if __name__ == "__main__":
    main()
