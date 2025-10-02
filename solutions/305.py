
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    ships = []
    index = 3
    for i in range(k):
        y1 = int(data[index]); x1 = int(data[index+1])
        y2 = int(data[index+2]); x2 = int(data[index+3])
        index += 4
        ships.append((y1, x1, y2, x2))
    
    grid = [[False] * (m+2) for _ in range(n+2)]
    
    for ship in ships:
        y1, x1, y2, x2 = ship
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                grid[i][j] = True
    
    for i in range(n+2):
        for j in range(m+2):
            if i == 0 or i == n+1 or j == 0 or j == m+1:
                grid[i][j] = True
    
    max_area = 0
    
    for top in range(1, n+1):
        heights = [0] * (m+1)
        for bottom in range(top, n+1):
            for col in range(1, m+1):
                if grid[bottom][col]:
                    heights[col] = 0
                else:
                    heights[col] += 1
            
            stack = []
            left = [0] * (m+2)
            for col in range(1, m+1):
                while stack and heights[stack[-1]] >= heights[col]:
                    stack.pop()
                if stack:
                    left[col] = stack[-1]
                else:
                    left[col] = 0
                stack.append(col)
            
            stack = []
            right = [m+1] * (m+2)
            for col in range(m, 0, -1):
                while stack and heights[stack[-1]] >= heights[col]:
                    stack.pop()
                if stack:
                    right[col] = stack[-1]
                else:
                    right[col] = m+1
                stack.append(col)
            
            for col in range(1, m+1):
                width = right[col] - left[col] - 1
                area = (bottom - top + 1) * width
                if area > max_area:
                    max_area = area
    
    print(max_area)

if __name__ == "__main__":
    main()
