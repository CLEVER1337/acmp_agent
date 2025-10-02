
def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    rects = []
    index = 1
    for i in range(n):
        x1 = int(data[index]); y1 = int(data[index+1])
        x2 = int(data[index+2]); y2 = int(data[index+3])
        index += 4
        rects.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    
    if n == 0:
        print(1)
        return
    
    xs = set()
    ys = set()
    for rect in rects:
        x1, y1, x2, y2 = rect
        xs.add(x1)
        xs.add(x2)
        ys.add(y1)
        ys.add(y2)
    
    xs = sorted(xs)
    ys = sorted(ys)
    
    grid = [[False] * (len(ys) - 1) for _ in range(len(xs) - 1)]
    
    for rect in rects:
        x1, y1, x2, y2 = rect
        idx_x1 = xs.index(x1)
        idx_x2 = xs.index(x2)
        idx_y1 = ys.index(y1)
        idx_y2 = ys.index(y2)
        
        for i in range(idx_x1, idx_x2):
            for j in range(idx_y1, idx_y2):
                grid[i][j] = True
    
    visited = [[False] * (len(ys) - 1) for _ in range(len(xs) - 1)]
    
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if visited[i][j] or grid[i][j]:
            return
        visited[i][j] = True
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and not grid[i][j]:
                dfs(i, j)
                count += 1
    
    print(count)

if __name__ == "__main__":
    main()
