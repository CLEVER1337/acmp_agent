
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
    
    best_pos = -1
    best_len = float('inf')
    
    for i in range(len(normY) + 1):
        left = normY[:i]
        right = normY[i:]
        
        candidate_left = normalize(normX + left)
        if candidate_left.endswith(left):
            candidate = candidate_left[:-len(left)] + normY
            if len(candidate) < best_len:
                best_len = len(candidate)
                best_candidate = candidate
                
        candidate_right = normalize(right + normX)
        if candidate_right.startswith(right):
            candidate = normY + candidate_right[len(right):]
            if len(candidate) < best_len:
                best_len = len(candidate)
                best_candidate = candidate
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(best_candidate)

if __name__ == '__main__':
    main()
