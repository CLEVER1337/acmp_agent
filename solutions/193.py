
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    grid = []
    index = 3
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        grid.append(row)
        index += m
    
    results = [None] * (k + 1)
    
    for rect_id in range(1, k + 1):
        min_row = n
        max_row = -1
        min_col = m
        max_col = -1
        
        found = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == rect_id:
                    found = True
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        
        if found:
            x1 = min_col
            y1 = n - 1 - max_row
            x2 = max_col
            y2 = n - 1 - min_row
            results[rect_id] = (x1, y1, x2, y2)
        else:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] > rect_id:
                        covered = True
                        for rect_id2 in range(rect_id + 1, k + 1):
                            if results[rect_id2] is not None:
                                x1, y1, x2, y2 = results[rect_id2]
                                y1_orig = n - 1 - y2
                                y2_orig = n - 1 - y1
                                if x1 <= j <= x2 and y1_orig <= i <= y2_orig:
                                    covered = False
                                    break
                        if covered:
                            if min_row == n:
                                min_row = i
                                max_row = i
                                min_col = j
                                max_col = j
                            else:
                                min_row = min(min_row, i)
                                max_row = max(max_row, i)
                                min_col = min(min_col, j)
                                max_col = max(max_col, j)
            if min_row != n:
                x1 = min_col
                y1 = n - 1 - max_row
                x2 = max_col
                y2 = n - 1 - min_row
                results[rect_id] = (x1, y1, x2, y2)
            else:
                results[rect_id] = (0, 0, 0, 0)
    
    for i in range(1, k + 1):
        if results[i] is None:
            results[i] = (0, 0, 0, 0)
        x1, y1, x2, y2 = results[i]
        print(f"{x1} {y1} {x2} {y2}")

if __name__ == "__main__":
    main()
