
def main():
    with open('INPUT.TXT', 'r') as f:
        S = f.readline().strip()
    
    n = len(S)
    dp = [0] * (n + 1)
    parent = [None] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        dp[i] = float('inf')
        for j in range(i):
            substr = S[j:i]
            len_sub = i - j
            period = get_period(substr)
            if period < len_sub and len_sub % period == 0:
                count = len_sub // period
                cost = period + dp[j]
                if cost < dp[i]:
                    dp[i] = cost
                    parent[i] = (j, period, count)
            cost = len_sub + dp[j]
            if cost < dp[i]:
                dp[i] = cost
                parent[i] = (j, len_sub, 1)
    
    result = []
    pos = n
    while pos > 0:
        j, len_s, count = parent[pos]
        substr = S[j:j+len_s]
        result.append((substr, count))
        pos = j
    
    result.reverse()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[n]) + '\n')
        for s, d in result:
            f.write(f"{s} {d}\n")

def get_period(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    
    period = n - pi[-1]
    if n % period == 0:
        return period
    return n

if __name__ == '__main__':
    main()
