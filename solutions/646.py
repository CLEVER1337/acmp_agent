
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    A = list(map(int, data[2:2+n]))
    
    total_sum = sum(A)
    
    if total_sum < 2 * k:
        print(0)
        return
        
    dp = [0] * (total_sum + 1)
    dp[0] = 1
    
    for a in A:
        for s in range(total_sum, a - 1, -1):
            dp[s] += dp[s - a]
                
    count = 0
    for s in range(k, total_sum - k + 1):
        count += dp[s]
            
    print(count)

if __name__ == "__main__":
    main()
