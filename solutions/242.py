
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
    
    row_colors = [defaultdict(int) for _ in range(n)]
    col_colors = [defaultdict(int) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            color = grid[i][j]
            row_colors[i][color] += 1
            col_colors[j][color] += 1
    
    def is_valid_row(i, color):
        return row_colors[i][color] >= 2
    
    def is_valid_col(j, color):
        return col_colors[j][color] >= 2
    
    def paint_row(i, new_color):
        for j in range(n):
            old_color = grid[i][j]
            if old_color != new_color:
                row_colors[i][old_color] -= 1
                col_colors[j][old_color] -= 1
                row_colors[i][new_color] += 1
                col_colors[j][new_color] += 1
                grid[i][j] = new_color
    
    def paint_col(j, new_color):
        for i in range(n):
            old_color = grid[i][j]
            if old_color != new_color:
                row_colors[i][old_color] -= 1
                col_colors[j][old_color] -= 1
                row_colors[i][new_color] += 1
                col_colors[j][new_color] += 1
                grid[i][j] = new_color
    
    def all_same_color():
        target = grid[0][0]
        for i in range(n):
            for j in range(n):
                if grid[i][j] != target:
                    return False
        return True
    
    min_operations = float('inf')
    best_color = None
    
    for candidate_color in range(1, k+1):
        operations = 0
        temp_grid = [row[:] for row in grid]
        temp_row_colors = [d.copy() for d in row_colors]
        temp_col_colors = [d.copy() for d in col_colors]
        
        def temp_paint_row(i, new_color):
            nonlocal operations
            for j in range(n):
                old_color = temp_grid[i][j]
                if old_color != new_color:
                    temp_row_colors[i][old_color] -= 1
                    temp_col_colors[j][old_color] -= 1
                    temp_row_colors[i][new_color] += 1
                    temp_col_colors[j][new_color] += 1
                    temp_grid[i][j] = new_color
            operations += 1
        
        def temp_paint_col(j, new_color):
            nonlocal operations
            for i in range(n):
                old_color = temp_grid[i][j]
                if old_color != new_color:
                    temp_row_colors[i][old_color] -= 1
                    temp_col_colors[j][old_color] -= 1
                    temp_row_colors[i][new_color] += 1
                    temp_col_colors[j][new_color] += 1
                    temp_grid[i][j] = new_color
            operations += 1
        
        changed = True
        while changed:
            changed = False
            for i in range(n):
                if temp_is_valid_row(i, candidate_color) and any(temp_grid[i][j] != candidate_color for j in range(n)):
                    temp_paint_row(i, candidate_color)
                    changed = True
            
            for j in range(n):
                if temp_is_valid_col(j, candidate_color) and any(temp_grid[i][j] != candidate_color for i in range(n)):
                    temp_paint_col(j, candidate_color)
                    changed = True
        
        all_same = True
        for i in range(n):
            for j in range(n):
                if temp_grid[i][j] != candidate_color:
                    all_same = False
                    break
            if not all_same:
                break
        
        if all_same and operations < min_operations:
            min_operations = operations
            best_color = candidate_color
    
    if min_operations == float('inf'):
        print("0 0")
    else:
        print(f"{min_operations} {best_color}")

def temp_is_valid_row(i, color):
    return True

def temp_is_valid_col(j, color):
    return True

if __name__ == "__main__":
    main()
