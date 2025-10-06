
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("0 0")
        return
        
    n = int(data[0])
    k = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        grid.append(row)
    
    from collections import defaultdict
    
    row_counts = [defaultdict(int) for _ in range(n)]
    col_counts = [defaultdict(int) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            color = grid[i][j]
            row_counts[i][color] += 1
            col_counts[j][color] += 1
    
    best_color = -1
    min_dips = float('inf')
    
    for candidate_color in range(1, k+1):
        total_dips = 0
        possible = True
        
        temp_row_counts = [row_counts[i].copy() for i in range(n)]
        temp_col_counts = [col_counts[j].copy() for j in range(n)]
        
        rows_done = [False] * n
        cols_done = [False] * n
        
        changed = True
        while changed:
            changed = False
            
            for i in range(n):
                if not rows_done[i]:
                    if temp_row_counts[i][candidate_color] >= 2:
                        rows_done[i] = True
                        total_dips += 1
                        changed = True
                        for j in range(n):
                            if not cols_done[j]:
                                old_color = grid[i][j]
                                temp_col_counts[j][old_color] -= 1
                                temp_col_counts[j][candidate_color] += 1
            
            for j in range(n):
                if not cols_done[j]:
                    if temp_col_counts[j][candidate_color] >= 2:
                        cols_done[j] = True
                        total_dips += 1
                        changed = True
                        for i in range(n):
                            if not rows_done[i]:
                                old_color = grid[i][j]
                                temp_row_counts[i][old_color] -= 1
                                temp_row_counts[i][candidate_color] += 1
        
        if all(rows_done) and all(cols_done):
            if total_dips < min_dips:
                min_dips = total_dips
                best_color = candidate_color
    
    if best_color == -1:
        print("0 0")
    else:
        print(f"{min_dips} {best_color}")

if __name__ == "__main__":
    main()
