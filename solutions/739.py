
def main():
    import sys
    data = sys.stdin.read().splitlines()
    K = int(data[0])
    s = data[1].strip()
    n = len(s)
    
    if K == 0:
        print(s)
        return
        
    res = [''] * n
    used = [False] * n
    positions = list(range(n))
    
    for i in range(n):
        start = max(0, i - K)
        end = min(n, i + K + 1)
        
        best_char = 'z'
        best_pos = -1
        
        for j in range(start, end):
            if not used[j] and s[j] < best_char:
                best_char = s[j]
                best_pos = j
                
        if best_pos == -1:
            for j in range(start, end):
                if not used[j]:
                    best_char = s[j]
                    best_pos = j
                    break
                    
        res[i] = best_char
        used[best_pos] = True
        
    print(''.join(res))

if __name__ == '__main__':
    main()
