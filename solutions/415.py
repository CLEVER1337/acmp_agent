
def main():
    s1 = input().strip()
    s2 = input().strip()
    
    n = len(s1)
    m = len(s2)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    lcs_len = dp[n][m]
    lcs = []
    i, j = n, m
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    lcs.reverse()
    lcs_str = ''.join(lcs)
    
    i = j = 0
    result = []
    
    for char in lcs_str:
        while i < n and s1[i] != char:
            result.append(s1[i])
            i += 1
        while j < m and s2[j] != char:
            result.append(s2[j])
            j += 1
        
        result.append(char)
        i += 1
        j += 1
    
    while i < n:
        result.append(s1[i])
        i += 1
    while j < m:
        result.append(s2[j])
        j += 1
    
    merged = ''.join(result)
    
    first_misha = merged.find(s1)
    first_masha = merged.find(s2)
    
    if first_misha != -1 and first_masha != -1:
        output = list(merged)
        output[first_misha] = output[first_misha].upper()
        output[first_masha] = output[first_masha].upper()
        print(''.join(output))
    else:
        print(merged)

if __name__ == "__main__":
    main()
