
def main():
    with open('INPUT.TXT', 'r') as f:
        S = f.readline().strip()
    
    n = len(S)
    dp = [0] * (n + 1)
    parent = [(-1, -1)] * (n + 1)
    period = [0] * (n + 1)
    
    for i in range(n + 1):
        dp[i] = i
        parent[i] = (-1, 1)
        period[i] = i
    
    for i in range(n):
        p = [0] * (n + 1)
        k = 0
        for j in range(i + 1, n):
            while k > 0 and S[j] != S[i + k]:
                k = p[i + k - 1]
            if S[j] == S[i + k]:
                k += 1
            else:
                k = 0
            p[j] = k
        
        for j in range(i, n):
            len_sub = j - i + 1
            per = len_sub - p[j]
            if len_sub % per == 0:
                period[j] = per
            else:
                period[j] = len_sub
    
    for i in range(n):
        for j in range(i, n):
            len_sub = j - i + 1
            per = period[j]
            if len_sub % per == 0:
                cnt = len_sub // per
                cost = per
                if dp[i] + cost < dp[j + 1]:
                    dp[j + 1] = dp[i] + cost
                    parent[j + 1] = (i, cnt)
            else:
                cost = len_sub
                if dp[i] + cost < dp[j + 1]:
                    dp[j + 1] = dp[i] + cost
                    parent[j + 1] = (i, 1)
    
    res = []
    pos = n
    while pos > 0:
        prev, cnt = parent[pos]
        substr = S[prev:pos]
        if cnt > 1:
            per = period[pos - 1]
            actual_sub = S[prev:prev + per]
            res.append((actual_sub, cnt))
        else:
            res.append((substr, 1))
        pos = prev
    
    res.reverse()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[n]) + '\n')
        for s, cnt in res:
            f.write(f"{s} {cnt}\n")

if __name__ == '__main__':
    main()
