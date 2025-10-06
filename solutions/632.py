
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    W = int(data[0])
    H = int(data[1])
    n = int(data[2])
    segments = []
    index = 3
    for i in range(n):
        a, b, c, d = map(int, data[index:index+4])
        index += 4
        if a == c:
            if b > d:
                b, d = d, b
            segments.append(('v', a, b, d))
        else:
            if a > c:
                a, c = c, a
            segments.append(('h', b, a, c))
    
    verticals = []
    horizontals = []
    for seg in segments:
        if seg[0] == 'v':
            verticals.append(seg)
        else:
            horizontals.append(seg)
    
    verticals.sort(key=lambda x: x[1])
    horizontals.sort(key=lambda x: x[1])
    
    xs = [0, W]
    ys = [0, H]
    
    for seg in verticals:
        xs.append(seg[1])
    for seg in horizontals:
        ys.append(seg[1])
    
    xs = sorted(set(xs))
    ys = sorted(set(ys))
    
    grid = [[False] * (len(ys) - 1) for _ in range(len(xs) - 1)]
    
    for seg in verticals:
        x = seg[1]
        y1 = seg[2]
        y2 = seg[3]
        idx_x = xs.index(x)
        for j in range(len(ys) - 1):
            if ys[j] >= y1 and ys[j+1] <= y2:
                if idx_x > 0:
                    grid[idx_x - 1][j] = True
                if idx_x < len(xs) - 1:
                    grid[idx_x][j] = True
    
    for seg in horizontals:
        y = seg[1]
        x1 = seg[2]
        x2 = seg[3]
        idx_y = ys.index(y)
        for i in range(len(xs) - 1):
            if xs[i] >= x1 and xs[i+1] <= x2:
                if idx_y > 0:
                    grid[i][idx_y - 1] = True
                if idx_y < len(ys) - 1:
                    grid[i][idx_y] = True
    
    areas = []
    visited = [[False] * (len(ys) - 1) for _ in range(len(xs) - 1)]
    
    from collections import deque
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            if not visited[i][j] and not grid[i][j]:
                area = 0
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    ci, cj = queue.popleft()
                    cell_area = (xs[ci+1] - xs[ci]) * (ys[cj+1] - ys[cj])
                    area += cell_area
                    for dx, dy in directions:
                        ni, nj = ci + dx, cj + dy
                        if 0 <= ni < len(xs)-1 and 0 <= nj < len(ys)-1:
                            if not visited[ni][nj] and not grid[ni][nj]:
                                visited[ni][nj] = True
                                queue.append((ni, nj))
                areas.append(area)
    
    areas.sort(reverse=True)
    print(' '.join(map(str, areas)))

if __name__ == "__main__":
    main()
