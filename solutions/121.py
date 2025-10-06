
def main():
    n = int(input().strip())
    coords = list(map(int, input().split()))
    coords.sort()
    
    dp = [0] * n
    dp[1] = coords[1] - coords[0]
    
    if n > 2:
        dp[2] = coords[2] - coords[0]
        
    for i in range(3, n):
        dp[i] = min(dp[i-1], dp[i-2]) + coords[i] - coords[i-1]
        
    print(dp[n-1])

if __name__ == "__main__":
    main()
