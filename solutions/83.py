
def main():
    import sys
    data = sys.stdin.read().split()
    M = int(data[0])
    N = int(data[1])
    
    total_cells = M * N
    max_patterns = 2 ** total_cells
    
    patterns = []
    for i in range(max_patterns):
        grid = []
        for row in range(M):
            row_pattern = []
            for col in range(N):
                bit_pos = row * N + col
                color = (i >> bit_pos) & 1
                row_pattern.append(color)
            grid.append(tuple(row_pattern))
        patterns.append(tuple(grid))
    
    valid_count = 0
    for pattern in patterns:
        valid = True
        for i in range(M - 1):
            for j in range(N - 1):
                if (pattern[i][j] == pattern[i][j+1] == 
                    pattern[i+1][j] == pattern[i+1][j+1]):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            valid_count += 1
    
    print(valid_count)

if __name__ == "__main__":
    main()
