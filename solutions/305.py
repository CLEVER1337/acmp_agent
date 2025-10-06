
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    ships = []
    index = 3
    for i in range(k):
        r1 = int(data[index])
        c1 = int(data[index+1])
        r2 = int(data[index+2])
        c2 = int(data[index+3])
        index += 4
        ships.append((r1, c1, r2, c2))
    
    grid = [[0] * (m + 2) for _ in range(n + 2)]
    
    for ship in ships:
        r1, c1, r2, c2 = ship
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                grid[i][j] = 1
                
        for i in range(r1 - 1, r2 + 2):
            for j in range(c1 - 1, c2 + 2):
                if 1 <= i <= n and 1 <= j <= m:
                    grid[i][j] = 2
    
    max_area = 0
    heights = [0] * (m + 2)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] == 0:
                heights[j] += 1
            else:
                heights[j] = 0
        
        stack = []
        for j in range(1, m + 2):
            while stack and heights[stack[-1]] > heights[j]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else 0
                width = j - left - 1
                area = h * width
                if area > max_area:
                    max_area = area
            stack.append(j)
    
    print(max_area)

if __name__ == "__main__":
    main()
