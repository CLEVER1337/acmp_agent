
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
    for (x1, y1, x2, y2) in rects:
        xs.add(x1)
        xs.add(x2)
        ys.add(y1)
        ys.add(y2)
    
    xs = sorted(xs)
    ys = sorted(ys)
    
    x_to_idx = {x: i for i, x in enumerate(xs)}
    y_to_idx = {y: i for i, y in enumerate(ys)}
    
    grid = [[False] * (len(ys) for _ in range(len(xs))]
    
    for (x1, y1, x2, y2) in rects:
        i1 = x_to_idx[x1]
        i2 = x_to_idx[x2]
        j1 = y_to_idx[y1]
        j2 = y_to_idx[y2]
        for i in range(i1, i2):
            for j in range(j1, j2):
                grid[i][j] = True
    
    rows = len(grid)
    cols = len(grid[0])
    
    visited = [[False] * cols for _ in range(rows)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def dfs(i, j):
        stack = [(i, j)]
        visited[i][j] = True
        while stack:
            ci, cj = stack.pop()
            for dx, dy in directions:
                ni, nj = ci + dx, cj + dy
                if 0 <= ni < rows and 0 <= nj < cols:
                    if not visited[ni][nj] and not grid[ni][nj]:
                        visited[ni][nj] = True
                        stack.append((ni, nj))
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and not grid[i][j]:
                dfs(i, j)
                count += 1
                
    print(count)

if __name__ == "__main__":
    main()
