
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    s = data[1].strip()
    k_and_edges = list(map(int, data[2].split()))
    k = k_and_edges[0]
    edges = k_and_edges[1:1+k]
    
    result = []
    for edge in edges:
        pos = edge - 1
        fold_type = 'K'
        for i in range(n):
            mid = (2**n - 1) // 2
            if pos == mid:
                fold_type = 'K' if s[i] == 'P' else 'O'
                break
            elif pos > mid:
                pos = 2**n - 2 - pos
            pos %= 2**(n - i - 1)
        result.append(fold_type)
    
    print(''.join(result))

if __name__ == '__main__':
    main()
