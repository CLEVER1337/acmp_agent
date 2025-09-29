
def main():
    import sys
    input = sys.stdin.read().split()
    M = int(input[0])
    N = int(input[1])
    
    total_cells = M * N
    max_patterns = 1 << total_cells
    count = 0
    
    for pattern in range(max_patterns):
        valid = True
        for i in range(M - 1):
            for j in range(N - 1):
                pos1 = i * N + j
                pos2 = i * N + j + 1
                pos3 = (i + 1) * N + j
                pos4 = (i + 1) * N + j + 1
                
                bit1 = (pattern >> pos1) & 1
                bit2 = (pattern >> pos2) & 1
                bit3 = (pattern >> pos3) & 1
                bit4 = (pattern >> pos4) & 1
                
                if bit1 == bit2 == bit3 == bit4:
                    valid = False
                    break
            if not valid:
                break
                
        if valid:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
