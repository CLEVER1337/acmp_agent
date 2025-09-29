
def main():
    data = list(map(int, input().split()))
    n = data[0]
    coins = data[1:1+n]
    k = data[1+n]
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + coins[i-1]
    
    dp = [0] * (n + 1)
    take = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = prefix[i]
        take[i] = i
        
    for i in range(1, n + 1):
        for j in range(1, min(take[i], k) + 1):
            if i + j > n:
                continue
            total = prefix[i+j] - prefix[i]
            opponent = dp[i]
            my_score = total + (prefix[n] - prefix[i+j] - opponent)
            if my_score > dp[i+j]:
                dp[i+j] = my_score
                take[i+j] = j
                
    print(dp[n])

if __name__ == "__main__":
    main()
