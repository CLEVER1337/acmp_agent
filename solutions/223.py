
def main():
    s1 = input().strip()
    s2 = input().strip()
    n = len(s1)
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
        
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            
    count = [0] * 26
    for c in s1:
        count[ord(c) - ord('A')] += 1
        
    for c in s2:
        count[ord(c) - ord('A')] -= 1
        
    for c in count:
        if c != 0:
            print(0)
            return
            
    result = 1
    i = 0
    while i < n:
        j = i
        while j < n and s2[j] == s2[i]:
            j += 1
        length = j - i
        result *= dp[n][length]
        n -= length
        i = j
        
    print(result)

if __name__ == "__main__":
    main()
