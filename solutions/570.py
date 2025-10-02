
def main():
    import sys
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, n+1):
        grid.append(data[i].strip())
    
    min_i, max_i = n, -1
    min_j, max_j = m, -1
    black_count = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                black_count += 1
                min_i = min(min_i, i)
                max_i = max(max_i, i)
                min_j = min(min_j, j)
                max_j = max(max_j, j)
    
    if black_count == 0:
        print("CIRCLE")
        return
        
    height = max_i - min_i + 1
    width = max_j - min_j + 1
    
    if height != width:
        print("CIRCLE")
        return
        
    k = height
    
    if k < 3:
        print("SQUARE")
        return
        
    expected_black = k * k - (k - 2) * (k - 2)
    
    actual_black = 0
    for i in range(min_i, max_i+1):
        for j in range(min_j, max_j+1):
            if grid[i][j] == '*':
                actual_black += 1
    
    if abs(actual_black - expected_black) <= k * 2:
        print("SQUARE")
    else:
        print("CIRCLE")

if __name__ == "__main__":
    main()
