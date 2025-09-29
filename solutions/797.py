
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    objects = []
    for i in range(n):
        x = int(data[2 + i*2])
        y = int(data[3 + i*2])
        objects.append((x, y))
    
    if k == 0:
        print(0)
        return
        
    cols_needed = set()
    rows_needed = set()
    
    for x, y in objects:
        col = (x - 1) // k
        row = (y - 1) // k
        cols_needed.add(col)
        rows_needed.add(row)
    
    if not cols_needed or not rows_needed:
        print(0)
        return
        
    min_col = min(cols_needed)
    max_col = max(cols_needed)
    min_row = min(rows_needed)
    max_row = max(rows_needed)
    
    total_cols = max_col - min_col + 1
    total_rows = max_row - min_row + 1
    
    days = 0
    
    if total_rows > 0:
        days += (total_rows - 1) * 2
    
    if total_cols > 0:
        days += max_col - min_col
    
    if total_rows % 2 == 1:
        days += max_col - min_col
    else:
        days += min_col - max_col
    
    print(days)

if __name__ == "__main__":
    main()
