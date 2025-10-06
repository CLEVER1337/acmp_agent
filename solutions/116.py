
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(map(int, data[i].strip())))
    
    if n == 0 or m == 0:
        print(0)
        return
        
    heights = [0] * m
    left = [0] * m
    right = [m - 1] * m
    max_area = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0
        
        current_left = 0
        for j in range(m):
            if grid[i][j] == 1:
                left[j] = max(left[j], current_left)
            else:
                left[j] = 0
                current_left = j + 1
        
        current_right = m - 1
        for j in range(m - 1, -1, -1):
            if grid[i][j] == 1:
                right[j] = min(right[j], current_right)
            else:
                right[j] = m - 1
                current_right = j - 1
        
        for j in range(m):
            width = right[j] - left[j] + 1
            area = heights[j] * width
            if area > max_area:
                max_area = area
                
    print(max_area)

if __name__ == "__main__":
    main()
