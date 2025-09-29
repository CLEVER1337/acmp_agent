
def main():
    import sys
    data = sys.stdin.read().splitlines()
    K = int(data[0])
    S = data[1].strip()
    n = len(S)
    
    from collections import defaultdict, deque
    
    freq = defaultdict(int)
    window = deque()
    min_chars = float('inf')
    best_set = set()
    
    for i in range(n):
        if len(window) >= K:
            old_char = window.popleft()
            freq[old_char] -= 1
            if freq[old_char] == 0:
                del freq[old_char]
        
        window.append(S[i])
        freq[S[i]] += 1
        
        if len(window) == K:
            if len(freq) < min_chars:
                min_chars = len(freq)
                best_set = set(freq.keys())
            elif len(freq) == min_chars:
                best_set = set(freq.keys())
    
    print(min_chars)
    for char in sorted(best_set):
        print(char)

if __name__ == "__main__":
    main()
