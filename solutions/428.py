
def main():
    n = int(input().strip())
    s = input().strip()
    
    mapping = {
        'A': 2, 'B': 2, 'C': 2,
        'D': 3, 'E': 3, 'F': 3,
        'G': 4, 'H': 4, 'I': 4,
        'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6,
        'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8,
        'W': 9, 'X': 9, 'Y': 9, 'Z': 9
    }
    
    count = {
        'A': 1, 'B': 2, 'C': 3,
        'D': 1, 'E': 2, 'F': 3,
        'G': 1, 'H': 2, 'I': 3,
        'J': 1, 'K': 2, 'L': 3,
        'M': 1, 'N': 2, 'O': 3,
        'P': 1, 'Q': 2, 'R': 3, 'S': 4,
        'T': 1, 'U': 2, 'V': 3,
        'W': 1, 'X': 2, 'Y': 3, 'Z': 4
    }
    
    dp = [[0] * (len(s) + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(n + 1):
        for j in range(len(s)):
            if dp[i][j] == 0:
                continue
            if i < n:
                for k in range(j, len(s)):
                    if mapping[s[k]] != mapping[s[j]]:
                        break
                    if count[s[k]] <= k - j + 1 <= count[s[k]] * 2 - 1:
                        dp[i + 1][k + 1] += dp[i][j]
    
    result = 0
    for j in range(len(s) + 1):
        result += dp[n][j]
    
    print(result)

if __name__ == "__main__":
    main()
