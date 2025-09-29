
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    A = list(map(int, data[2:2+n]))
    
    total = sum(A)
    if total < 2 * k:
        print(0)
        return
        
    dp = [0] * (total + 1)
    dp[0] = 1
    
    for a in A:
        for j in range(total, a - 1, -1):
            dp[j] += dp[j - a]
                
    count = 0
    for s in range(k, total - k + 1):
        count += dp[s]
            
    print(count)

if __name__ == "__main__":
    main()
