
def main():
    with open('INPUT.TXT', 'r') as f:
        X = f.readline().strip()
        Y = f.readline().strip()
    
    n = len(X)
    m = len(Y)
    
    def normalize(s):
        stack = []
        for c in s:
            if stack and stack[-1].swapcase() == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
    
    normX = normalize(X)
    normY = normalize(Y)
    
    best_len = float('inf')
    best_word = None
    
    for i in range(len(normX) + 1):
        for j in range(len(normY) + 1):
            prefix = normX[:i]
            suffix = normY[j:]
            
            candidate = prefix + normY + suffix
            normalized_candidate = normalize(candidate)
            
            if normalized_candidate == normalize(normX + normY[j:]):
                if len(candidate) < best_len:
                    best_len = len(candidate)
                    best_word = candidate
    
    print(best_word)

if __name__ == '__main__':
    main()
