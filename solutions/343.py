
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    grid = [[0] * m for _ in range(n)]
    commands = []
    index = 3
    for i in range(k):
        t = int(data[index])
        y = int(data[index+1])
        x = int(data[index+2])
        index += 3
        commands.append((t, y, x))
    
    covered_area = 0
    
    for cmd in commands:
        t, y, x = cmd
        if t == 1:
            cells = [(y, x), (y, x+1), (y+1, x)]
        elif t == 2:
            cells = [(y, x), (y, x+1), (y+1, x+1)]
        elif t == 3:
            cells = [(y, x), (y+1, x), (y+1, x+1)]
        elif t == 4:
            cells = [(y, x+1), (y+1, x), (y+1, x+1)]
        
        valid = True
        for cy, cx in cells:
            if cy < 0 or cy >= n or cx < 0 or cx >= m or grid[cy][cx] == 1:
                valid = False
                break
        
        if valid:
            for cy, cx in cells:
                grid[cy][cx] = 1
                covered_area += 1
    
    print(covered_area)

if __name__ == "__main__":
    main()
