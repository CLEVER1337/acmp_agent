
def main():
    with open('INPUT.TXT', 'r') as f:
        xi = f.readline().strip()
        eta = f.readline().strip()
    
    n, m = len(xi), len(eta)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if xi[i] == eta[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
    max_len = dp[0][0]
    if max_len == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('\n\n')
        return
    
    alpha_end_i, alpha_end_j = -1, -1
    max_alpha_len = 0
    
    for i in range(n):
        for j in range(m):
            if dp[i][j] > max_alpha_len:
                max_alpha_len = dp[i][j]
                alpha_end_i, alpha_end_j = i, j
    
    alpha = ''
    i, j = alpha_end_i, alpha_end_j
    while i < n and j < m and dp[i][j] > 0:
        if xi[i] == eta[j]:
            alpha += xi[i]
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    
    rem_len = max_len - len(alpha)
    if rem_len == 0:
        with open('OUTPUT.TXT', 'w') as f:
            f.write(alpha + '\n\n')
        return
    
    dp2 = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if xi[i - 1] == eta[j - 1]:
                dp2[i][j] = dp2[i - 1][j - 1] + 1
            else:
                dp2[i][j] = max(dp2[i - 1][j], dp2[i][j - 1])
    
    beta_start_i, beta_start_j = -1, -1
    max_beta_len = 0
    
    for i in range(n):
        for j in range(m):
            if dp2[i][j] > max_beta_len and dp[i][j] == max_len - dp2[i][j]:
                max_beta_len = dp2[i][j]
                beta_start_i, beta_start_j = i, j
    
    beta = ''
    i, j = beta_start_i, beta_start_j
    while i > 0 and j > 0 and dp2[i][j] > 0:
        if xi[i - 1] == eta[j - 1]:
            beta = xi[i - 1] + beta
            i -= 1
            j -= 1
        elif dp2[i - 1][j] >= dp2[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(alpha + '\n')
        f.write(beta + '\n')

if __name__ == '__main__':
    main()
