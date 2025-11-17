
def partition(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j]*dp[i-j-1])
    
    return dp[n]

def partitions_squares(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            if dp[i] < dp[j]*dp[i-j-1]:
                dp[i] = dp[j]*dp[i-j-1]
    
    squares = []
    while n > 0:
        for i in range(n):
            if dp[i]*dp[n-i-1] == dp[n]:
                squares.append(n-i)
                n -= i+1
                break
    
    return squares[::-1]

if __name__ == '__main__':
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(partition(n)) + '\n')
        f.write(' '.join(map(str, partitions_squares(n))))
