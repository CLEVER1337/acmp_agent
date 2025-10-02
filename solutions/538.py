
import sys
import math

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = float(data[index])
        y = float(data[index + 1])
        index += 2
        points.append((x, y))
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist = math.sqrt(dx*dx + dy*dy)
            edges.append((dist, i, j))
    
    edges.sort(key=lambda x: x[0])
    
    parent = list(range(n))
    rank = [0] * n
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return False
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
        return True
    
    mst_edges = []
    for dist, u, v in edges:
        if union(u, v):
            mst_edges.append((dist, u, v))
    
    graph = [[] for _ in range(n)]
    for dist, u, v in mst_edges:
        graph[u].append((v, dist))
        graph[v].append((u, dist))
    
    color = [-1] * n
    color[0] = 0
    
    stack = [0]
    while stack:
        u = stack.pop()
        for v, dist in graph[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                stack.append(v)
    
    critical_dist = float('inf')
    for dist, u, v in edges:
        if color[u] == color[v]:
            critical_dist = min(critical_dist, dist)
    
    max_power = critical_dist / 2.0
    
    print(f"{max_power:.10f}")
    print(" ".join(str(c + 1) for c in color))

if __name__ == "__main__":
    main()
