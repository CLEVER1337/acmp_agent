
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, n+1):
        row = list(map(int, data[i].strip()))
        grid.append(row)
    
    if n == 0 or m == 0:
        print(0)
        return
        
    left = [0] * m
    right = [m] * m
    height = [0] * m
    
    max_area = 0
    
    for i in range(n):
        current_left = 0
        for j in range(m):
            if grid[i][j] == 1:
                height[j] += 1
                left[j] = max(left[j], current_left)
            else:
                height[j] = 0
                left[j] = 0
                current_left = j + 1
                
        current_right = m
        for j in range(m-1, -1, -1):
            if grid[i][j] == 1:
                right[j] = min(right[j], current_right)
            else:
                right[j] = m
                current_right = j
                
        for j in range(m):
            area = height[j] * (right[j] - left[j])
            if area > max_area:
                max_area = area
                
    print(max_area)

if __name__ == "__main__":
    main()
