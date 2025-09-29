
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        row = list(map(int, list(data[i].strip())))
        grid.append(row)
    
    if n == 0 or m == 0:
        print(0)
        return
        
    left = [0] * m
    right = [m] * m
    height = [0] * m
    
    max_area = 0
    
    for i in range(n):
        cur_left = 0
        cur_right = m
        
        for j in range(m):
            if grid[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0
                
        for j in range(m):
            if grid[i][j] == 1:
                left[j] = max(left[j], cur_left)
            else:
                left[j] = 0
                cur_left = j + 1
                
        for j in range(m-1, -1, -1):
            if grid[i][j] == 1:
                right[j] = min(right[j], cur_right)
            else:
                right[j] = m
                cur_right = j
                
        for j in range(m):
            area = height[j] * (right[j] - left[j])
            if area > max_area:
                max_area = area
                
    print(max_area)

if __name__ == "__main__":
    main()
