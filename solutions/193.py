
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
    
    rects = [None] * (k + 1)
    
    for num in range(1, k + 1):
        min_i = n
        max_i = -1
        min_j = m
        max_j = -1
        
        found = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == num:
                    found = True
                    if i < min_i:
                        min_i = i
                    if i > max_i:
                        max_i = i
                    if j < min_j:
                        min_j = j
                    if j > max_j:
                        max_j = j
        
        if found:
            rects[num] = (min_j, n - max_i - 1, max_j, n - min_i - 1)
        else:
            rects[num] = (0, 0, 0, 0)
    
    for num in range(1, k + 1):
        x1, y1, x2, y2 = rects[num]
        print(f"{x1} {y1} {x2} {y2}")

if __name__ == "__main__":
    main()
