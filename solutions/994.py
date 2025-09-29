
def main():
    with open('INPUT.TXT', 'r') as f:
        xi = f.readline().strip()
        eta = f.readline().strip()
    
    n, m = len(xi), len(eta)
    
    # Precompute suffix arrays for both strings
    # We'll find the longest common substring and then split it optimally
    
    # First, find all common substrings and their positions
    # But more efficiently, we can use dynamic programming
    
    # We need to find (alpha, beta) that appears in both strings in order
    
    # Alternative approach: find the longest common subsequence but with splitting?
    # Actually, we can think: the pair (alpha, beta) means that alpha appears before beta in both strings
    
    # Let's precompute for each string the positions where each substring appears
    # But that would be too expensive
    
    # Better: use DP to find the best split point
    
    # Let L1[i][j] be the length of the longest common substring ending at xi[i] and eta[j]
    # But we need to consider two parts
    
    # Actually, we can solve by finding the best i,j,k,l such that:
    # alpha is common substring ending at i in xi and j in eta
    # beta is common substring starting at k in xi and l in eta, with i < k
    
    # Precompute two arrays:
    # dp1[i][j] = length of LCS ending at xi[i] and eta[j]
    # dp2[i][j] = length of LCS starting at xi[i] and eta[j]
    
    # Initialize dp1
    dp1 = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if xi[i-1] == eta[j-1]:
                dp1[i][j] = dp1[i-1][j-1] + 1
            else:
                dp1[i][j] = 0
    
    # Initialize dp2 (longest common substring starting from position i,j)
    dp2 = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if xi[i] == eta[j]:
                dp2[i][j] = dp2[i+1][j+1] + 1
            else:
                dp2[i][j] = 0
    
    best_total = -1
    best_i1, best_j1 = -1, -1  # end of alpha
    best_i2, best_j2 = -1, -1  # start of beta
    
    # Try all possible splits: alpha ends at i-1 in xi, j-1 in eta
    # beta starts at k in xi, l in eta, with k >= i
    for i in range(0, n+1):
        for j in range(0, m+1):
            len_alpha = dp1[i][j]
            if len_alpha == 0:
                continue
            # Now look for the best beta starting after i in xi and after j in eta
            # We need to check all k >= i, l >= j
            # But we can precompute the maximum dp2 for positions >= i,j
            # Precomputation: create max_dp2 array
            # Alternatively, we can iterate in reverse and keep track of maximum
            
    # Precompute max_dp2 for efficiency
    max_dp2 = [[0] * (m+1) for _ in range(n+1)]
    # Fill max_dp2 from bottom-right
    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if i == n or j == m:
                max_dp2[i][j] = 0
            else:
                max_dp2[i][j] = max(dp2[i][j], max_dp2[i+1][j], max_dp2[i][j+1])
    
    # Now try all possible alpha endings
    for i in range(1, n+1):
        for j in range(1, m+1):
            len_alpha = dp1[i][j]
            if len_alpha == 0:
                continue
            # Beta must start at i or later in xi, j or later in eta
            if i < n and j < m:
                len_beta = max_dp2[i][j]
                total_len = len_alpha + len_beta
                if total_len > best_total:
                    best_total = total_len
                    best_i1, best_j1 = i, j
                    # For beta, we need to find the actual position where max_dp2[i][j] is achieved
                    # Find the actual starting position of beta
                    found = False
                    for k in range(i, n):
                        for l in range(j, m):
                            if dp2[k][l] == len_beta:
                                best_i2, best_j2 = k, l
                                found = True
                                break
                        if found:
                            break
    
    # Also consider the case where alpha is empty or beta is empty
    # Check if better solution exists with only beta
    max_beta = 0
    beta_start_i, beta_start_j = -1, -1
    for i in range(n):
        for j in range(m):
            if dp2[i][j] > max_beta:
                max_beta = dp2[i][j]
                beta_start_i, beta_start_j = i, j
    if max_beta > best_total:
        best_total = max_beta
        best_i1, best_j1 = 0, 0  # empty alpha
        best_i2, best_j2 = beta_start_i, beta_start_j
    
    # Check if better solution exists with only alpha
    max_alpha = 0
    alpha_end_i, alpha_end_j = -1, -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp1[i][j] > max_alpha:
                max_alpha = dp1[i][j]
                alpha_end_i, alpha_end_j = i, j
    if max_alpha > best_total:
        best_total = max_alpha
        best_i1, best_j1 = alpha_end_i, alpha_end_j
        best_i2, best_j2 = n, m  # empty beta
    
    # Extract alpha and beta
    alpha = ""
    if best_i1 > 0:
        alpha = xi[best_i1 - dp1[best_i1][best_j1] : best_i1]
    
    beta = ""
    if best_i2 < n:
        beta = xi[best_i2 : best_i2 + dp2[best_i2][best_j2]]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(alpha + '\n')
        f.write(beta + '\n')

if __name__ == '__main__':
    main()
