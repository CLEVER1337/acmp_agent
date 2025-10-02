
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    rects = []
    for i in range(n):
        idx = 1 + i * 4
        x1 = int(data[idx])
        y1 = int(data[idx + 1])
        x2 = int(data[idx + 2])
        y2 = int(data[idx + 3])
        rects.append((x1, y1, x2, y2))
    
    def intersects(a, b):
        ax1, ay1, ax2, ay2 = a
        bx1, by1, bx2, by2 = b
        if ax2 <= bx1 or bx2 <= ax1:
            return False
        if ay2 <= by1 or by2 <= ay1:
            return False
        return True
    
    def touches(a, b):
        ax1, ay1, ax2, ay2 = a
        bx1, by1, bx2, by2 = b
        if (ax2 == bx1 or ax1 == bx2) and (ay2 > by1 and by2 > ay1):
            return True
        if (ay2 == by1 or ay1 == by2) and (ax2 > bx1 and bx2 > ax1):
            return True
        return False
    
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if intersects(rects[i], rects[j]) or touches(rects[i], rects[j]):
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [False] * n
    
    def dfs(u, component):
        visited[u] = True
        component.append(u)
        for v in graph[u]:
            if not visited[v]:
                dfs(v, component)
    
    max_area = 0
    for i in range(n):
        if not visited[i]:
            component = []
            dfs(i, component)
            min_x = float('inf')
            min_y = float('inf')
            max_x = -float('inf')
            max_y = -float('inf')
            for idx in component:
                x1, y1, x2, y2 = rects[idx]
                min_x = min(min_x, x1)
                min_y = min(min_y, y1)
                max_x = max(max_x, x2)
                max_y = max(max_y, y2)
            area = (max_x - min_x) * (max_y - min_y)
            if area > max_area:
                max_area = area
    
    print(max_area)

if __name__ == "__main__":
    main()
