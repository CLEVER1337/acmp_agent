
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    A = []
    B = []
    C = []
    index = 1
    for i in range(n):
        A.append(int(data[index]))
        B.append(int(data[index+1]))
        C.append(int(data[index+2]))
        index += 3
        
    if n == 0:
        print(0)
        return
        
    dp = [0] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        dp[i] = dp[i-1] + A[i-1]
        if i >= 2:
            dp[i] = min(dp[i], dp[i-2] + B[i-2])
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + C[i-3])
            
    print(dp[n])

if __name__ == "__main__":
    main()
