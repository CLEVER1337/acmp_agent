
def main():
    s1 = input().strip()
    s2 = input().strip()
    n, m = len(s1), len(s2)
    
    lcs_dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                lcs_dp[i+1][j+1] = lcs_dp[i][j] + 1
            else:
                lcs_dp[i+1][j+1] = max(lcs_dp[i][j+1], lcs_dp[i+1][j])
    
    i, j = n, m
    lcs = []
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif lcs_dp[i-1][j] > lcs_dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    lcs = ''.join(reversed(lcs))
    
    if not lcs:
        print("")
        print("")
        return
        
    left1 = [0] * len(lcs)
    left2 = [0] * len(lcs)
    right1 = [0] * len(lcs)
    right2 = [0] * len(lcs)
    
    idx = 0
    for i in range(n):
        if idx < len(lcs) and s1[i] == lcs[idx]:
            left1[idx] = i
            idx += 1
            
    idx = 0
    for i in range(m):
        if idx < len(lcs) and s2[i] == lcs[idx]:
            left2[idx] = i
            idx += 1
            
    idx = len(lcs) - 1
    for i in range(n-1, -1, -1):
        if idx >= 0 and s1[i] == lcs[idx]:
            right1[idx] = i
            idx -= 1
            
    idx = len(lcs) - 1
    for i in range(m-1, -1, -1):
        if idx >= 0 and s2[i] == lcs[idx]:
            right2[idx] = i
            idx -= 1
            
    max_len = -1
    best_alpha = ""
    best_beta = ""
    
    for k in range(-1, len(lcs)):
        i1 = left1[k] if k >= 0 else -1
        j1 = right1[k+1] if k+1 < len(lcs) else n
        i2 = left2[k] if k >= 0 else -1
        j2 = right2[k+1] if k+1 < len(lcs) else m
        
        alpha = s1[i1+1:j1] if k >= 0 and k+1 < len(lcs) else ""
        beta = s2[i2+1:j2] if k >= 0 and k+1 < len(lcs) else ""
        
        if k == -1:
            alpha = s1[:right1[0]] if lcs else s1
            beta = s2[:right2[0]] if lcs else s2
        elif k == len(lcs) - 1:
            alpha = s1[left1[-1]+1:]
            beta = s2[left2[-1]+1:]
            
        total_len = len(alpha) + len(beta)
        if total_len > max_len:
            max_len = total_len
            best_alpha = alpha
            best_beta = beta
            
    print(best_alpha)
    print(best_beta)

if __name__ == "__main__":
    main()
