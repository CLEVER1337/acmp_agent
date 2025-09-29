
def main():
    with open("INPUT.TXT", "r") as f:
        X = f.readline().strip()
        Y = f.readline().strip()
    
    n = len(X)
    m = len(Y)
    
    # Precompute next occurrence for each character in X and Y
    def build_next_table(s):
        n = len(s)
        next_table = [[n] * 26 for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for c in range(26):
                next_table[i][c] = next_table[i + 1][c]
            char_idx = ord(s[i]) - ord('a')
            next_table[i][char_idx] = i
        return next_table
    
    next_X = build_next_table(X)
    next_Y = build_next_table(Y)
    
    # Check if a common subsequence exists
    if next_X[0][0] == n and next_Y[0][0] == m:
        # No common subsequence exists
        with open("OUTPUT.TXT", "w") as f:
            f.write("")
        return
    
    res = []
    i, j = 0, 0
    
    while True:
        found = False
        # Try from 'z' to 'a'
        for c in range(25, -1, -1):
            pos_X = next_X[i][c]
            pos_Y = next_Y[j][c]
            if pos_X < n and pos_Y < m:
                res.append(chr(ord('a') + c))
                i = pos_X + 1
                j = pos_Y + 1
                found = True
                break
        if not found:
            break
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(''.join(res))

if __name__ == "__main__":
    main()
