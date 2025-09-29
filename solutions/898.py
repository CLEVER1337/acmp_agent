
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    folds = data[1].strip()
    parts = data[2].split()
    k = int(parts[0])
    edges = list(map(int, parts[1:1+k]))
    
    result = []
    for edge_num in edges:
        pos = edge_num - 1
        direction = 'K'
        for i in range(n):
            fold_type = folds[i]
            half = (2**n) // (2**(i+1))
            if pos < half:
                if fold_type == 'Z':
                    direction = 'O' if direction == 'K' else 'K'
            else:
                pos = 2 * half - 1 - pos
                if fold_type == 'P':
                    direction = 'O' if direction == 'K' else 'K'
        result.append(direction)
    
    print(''.join(result))

if __name__ == '__main__':
    main()
