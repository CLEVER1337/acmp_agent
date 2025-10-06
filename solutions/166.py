
def main():
    data = input().split()
    K = int(data[0])
    N = int(data[1])
    
    if N == 1:
        print(K)
        return
        
    dp = [0] * (N + 1)
    dp[1] = K
    
    for year in range(2, N + 1):
        if year % 2 == 1:
            dp[year] = dp[year - 1] * 2
        else:
            dp[year] = dp[year - 1] + K
            
    print(dp[N])

if __name__ == "__main__":
    main()
