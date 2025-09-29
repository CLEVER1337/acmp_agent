
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
        r1 = int(data[index]) - 1
        c1 = int(data[index+1]) - 1
        r2 = int(data[index+2]) - 1
        c2 = int(data[index+3]) - 1
        ships.append((r1, c1, r2, c2))
        index += 4
    
    grid = [[0] * m for _ in range(n)]
    
    for ship in ships:
        r1, c1, r2, c2 = ship
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                grid[r][c] = 1
    
    max_area = 0
    
    for r1 in range(n):
        for c1 in range(m):
            if grid[r1][c1] == 1:
                continue
                
            max_width = m - c1
            for c2 in range(c1, m):
                if grid[r1][c2] == 1:
                    max_width = c2 - c1
                    break
            
            for r2 in range(r1, n):
                if grid[r2][c1] == 1:
                    break
                    
                width = max_width
                for c2 in range(c1, c1 + width):
                    if c2 >= m or grid[r2][c2] == 1:
                        width = c2 - c1
                        break
                
                if width == 0:
                    break
                    
                max_width = min(max_width, width)
                area = (r2 - r1 + 1) * max_width
                max_area = max(max_area, area)
    
    print(max_area)

if __name__ == "__main__":
    main()
