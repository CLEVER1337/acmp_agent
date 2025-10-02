
def main():
    with open("INPUT.TXT", "r") as f:
        X = f.readline().strip()
        Y = f.readline().strip()
    
    n = len(X)
    m = len(Y)
    
    # Precompute next occurrence for each character in X and Y
    def build_next(s):
        n = len(s)
        next_arr = [[n] * 26 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(26):
                next_arr[i][j] = next_arr[i+1][j]
            c = ord(s[i]) - ord('a')
            next_arr[i][c] = i
        return next_arr
    
    next_X = build_next(X)
    next_Y = build_next(Y)
    
    # Check if a string can be formed from both parents
    def is_valid(s):
        i, j = 0, 0
        for c in s:
            idx = ord(c) - ord('a')
            i = next_X[i][idx]
            if i >= n:
                return False
            i += 1
            
            j = next_Y[j][idx]
            if j >= m:
                return False
            j += 1
        return True
    
    # Find lexicographically largest string using binary search on length
    low, high = 0, min(n, m)
    best = ""
    
    while low <= high:
        mid = (low + high) // 2
        candidate = find_candidate(mid)
        if candidate:
            best = candidate
            low = mid + 1
        else:
            high = mid - 1
    
    print(best)
    
    def find_candidate(length):
        # Try to build the lexicographically largest string of given length
        res = []
        i, j = 0, 0
        for pos in range(length):
            # Try characters from 'z' to 'a'
            for c in range(25, -1, -1):
                char = chr(ord('a') + c)
                next_i = next_X[i][c]
                next_j = next_Y[j][c]
                if next_i < n and next_j < m:
                    # Check if remaining length can be satisfied
                    if can_form(length - pos - 1, next_i + 1, next_j + 1):
                        res.append(char)
                        i, j = next_i + 1, next_j + 1
                        break
            else:
                return None
        return ''.join(res)
    
    def can_form(remaining, start_i, start_j):
        # Check if we can form 'remaining' characters starting from (start_i, start_j)
        i, j = start_i, start_j
        for _ in range(remaining):
            # Find any character that exists in both strings from current positions
            found = False
            for c in range(26):
                if next_X[i][c] < n and next_Y[j][c] < m:
                    i = next_X[i][c] + 1
                    j = next_Y[j][c] + 1
                    found = True
                    break
            if not found:
                return False
        return True

if __name__ == "__main__":
    main()
