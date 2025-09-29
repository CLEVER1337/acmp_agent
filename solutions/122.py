
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().split()))
    
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    result = max(dp) if n > 0 else 0
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
