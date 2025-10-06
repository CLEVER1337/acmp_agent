
def main():
    X = input().strip()
    Y = input().strip()
    n = len(X)
    m = len(Y)
    
    def can_remove(s, i):
        if i < 0 or i >= len(s):
            return False
        if s[i] == 'a' and i + 1 < len(s) and s[i + 1] == 'A':
            return True
        if s[i] == 'A' and i + 1 < len(s) and s[i + 1] == 'a':
            return True
        if s[i] == 'b' and i + 1 < len(s) and s[i + 1] == 'B':
            return True
        if s[i] == 'B' and i + 1 < len(s) and s[i + 1] == 'b':
            return True
        return False
    
    def reduce_word(s):
        stack = []
        for char in s:
            stack.append(char)
            while len(stack) >= 2:
                a, b = stack[-2], stack[-1]
                if (a == 'a' and b == 'A') or (a == 'A' and b == 'a') or (a == 'b' and b == 'B') or (a == 'B' and b == 'b'):
                    stack.pop()
                    stack.pop()
                else:
                    break
        return ''.join(stack)
    
    base = reduce_word(X)
    redY = reduce_word(Y)
    
    if redY == "":
        print(base)
        return
        
    best_len = float('inf')
    best_word = None
    
    for start in range(len(base) + 1):
        for end in range(start, len(base) + 1):
            left = base[:start]
            right = base[end:]
            mid = base[start:end]
            
            candidate = left + Y + right
            reduced_candidate = reduce_word(candidate)
            
            if reduce_word(reduced_candidate) == base and Y in reduced_candidate:
                if len(reduced_candidate) < best_len:
                    best_len = len(reduced_candidate)
                    best_word = reduced_candidate
    
    if best_word is None:
        best_word = base
        
    print(best_word)

if __name__ == "__main__":
    main()
