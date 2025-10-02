
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
    
    colors_count = [0] * (k + 1)
    for i in range(n):
        for j in range(n):
            color = grid[i][j]
            if color <= k:
                colors_count[color] += 1
    
    min_ops = float('inf')
    best_color = 0
    
    for candidate in range(1, k + 1):
        if colors_count[candidate] < 2:
            continue
            
        ops = 0
        temp_grid = [row[:] for row in grid]
        
        for i in range(n):
            row_colors = {}
            for j in range(n):
                color = temp_grid[i][j]
                row_colors[color] = row_colors.get(color, 0) + 1
                
            if candidate in row_colors and row_colors[candidate] >= 2:
                for j in range(n):
                    temp_grid[i][j] = candidate
                ops += 1
            else:
                found_valid = False
                for color, count in row_colors.items():
                    if count >= 2:
                        for j in range(n):
                            temp_grid[i][j] = color
                        ops += 1
                        found_valid = True
                        break
                if not found_valid:
                    break
        
        if not found_valid:
            continue
            
        for j in range(n):
            col_colors = {}
            for i in range(n):
                color = temp_grid[i][j]
                col_colors[color] = col_colors.get(color, 0) + 1
                
            if candidate in col_colors and col_colors[candidate] >= 2:
                for i in range(n):
                    temp_grid[i][j] = candidate
                ops += 1
            else:
                found_valid = False
                for color, count in col_colors.items():
                    if count >= 2:
                        for i in range(n):
                            temp_grid[i][j] = color
                        ops += 1
                        found_valid = True
                        break
                if not found_valid:
                    break
        
        if not found_valid:
            continue
            
        all_same = True
        for i in range(n):
            for j in range(n):
                if temp_grid[i][j] != candidate:
                    all_same = False
                    break
            if not all_same:
                break
                
        if all_same and ops < min_ops:
            min_ops = ops
            best_color = candidate
    
    if min_ops != float('inf'):
        print(f"{min_ops} {best_color}")
    else:
        print("0 0")

if __name__ == "__main__":
    main()
