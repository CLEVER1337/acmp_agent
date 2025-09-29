
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); idx += 2
    R = list(map(int, data[idx:idx+n])); idx += n
    C = list(map(int, data[idx:idx+m])); idx += m
    
    Z = []
    for i in range(n):
        row = list(map(int, data[idx:idx+m]))
        idx += m
        Z.append(row)
    
    total_sum = 0
    fixed_cells = []
    free_cells = []
    
    for i in range(n):
        for j in range(m):
            if Z[i][j] != -1:
                total_sum += Z[i][j]
                fixed_cells.append((i, j, Z[i][j]))
            else:
                free_cells.append((i, j))
    
    row_used = [0] * n
    col_used = [0] * m
    
    for i, j, val in fixed_cells:
        row_used[i] += val
        col_used[j] += val
        
        if row_used[i] > R[i] or col_used[j] > C[j]:
            print(-1)
            return
    
    for i, j in free_cells:
        max_possible = min(R[i] - row_used[i], C[j] - col_used[j])
        if max_possible < 0:
            print(-1)
            return
        total_sum += max_possible
        row_used[i] += max_possible
        col_used[j] += max_possible
    
    print(total_sum)

if __name__ == "__main__":
    main()
