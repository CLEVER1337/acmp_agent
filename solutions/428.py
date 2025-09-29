
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        s = f.readline().strip()
    
    buttons = {
        'A': 'ABC', 'B': 'ABC', 'C': 'ABC',
        'D': 'DEF', 'E': 'DEF', 'F': 'DEF',
        'G': 'GHI', 'H': 'GHI', 'I': 'GHI',
        'J': 'JKL', 'K': 'JKL', 'L': 'JKL',
        'M': 'MNO', 'N': 'MNO', 'O': 'MNO',
        'P': 'PQRS', 'Q': 'PQRS', 'R': 'PQRS', 'S': 'PQRS',
        'T': 'TUV', 'U': 'TUV', 'V': 'TUV',
        'W': 'WXYZ', 'X': 'WXYZ', 'Y': 'WXYZ', 'Z': 'WXYZ'
    }
    
    dp = [[0] * (len(s) + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(n + 1):
        for j in range(len(s) + 1):
            if dp[i][j] == 0:
                continue
            if i < n and j < len(s):
                btn = buttons[s[j]]
                max_presses = len(btn)
                for k in range(1, max_presses + 1):
                    if j + k > len(s):
                        break
                    if all(s[j + l] in btn for l in range(k)):
                        if k == max_presses:
                            dp[i + 1][j + k] += dp[i][j]
                        else:
                            if j + k < len(s) and s[j + k] not in btn:
                                dp[i + 1][j + k] += dp[i][j]
                            elif j + k == len(s):
                                dp[i + 1][j + k] += dp[i][j]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[n][len(s)]))

if __name__ == '__main__':
    main()
