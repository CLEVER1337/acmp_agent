
def main():
    S = input().strip()
    n = len(S)
    dp = [0] * (n + 1)
    prev = [None] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        dp[i] = float('inf')
        for j in range(i):
            candidate = dp[j] + (i - j)
            if candidate < dp[i]:
                dp[i] = candidate
                prev[i] = (j, i - j, 1)
            
            substr = S[j:i]
            L = i - j
            for rep in range(2, i // L + 1):
                end = j + rep * L
                if end > n:
                    break
                if S[j:end] != substr * rep:
                    break
                candidate = dp[j] + L
                if candidate < dp[end]:
                    dp[end] = candidate
                    prev[end] = (j, L, rep)
    
    result = []
    pos = n
    while pos > 0:
        j, L, rep = prev[pos]
        result.append((S[j:j+L], rep))
        pos = j
    
    print(dp[n])
    for s, d in reversed(result):
        print(s, d)

if __name__ == "__main__":
    main()
