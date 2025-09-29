
import sys
import math

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    for i in range(n):
        x = float(data[1 + 2*i])
        y = float(data[2 + 2*i])
        points.append((x, y))
    
    def dist_sq(a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return dx*dx + dy*dy
    
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            d_sq = dist_sq(points[i], points[j])
            edges.append((d_sq, i, j))
    
    edges.sort()
    
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
    for d_sq, u, v in edges:
        if union(u, v):
            mst_edges.append((d_sq, u, v))
    
    graph = [[] for _ in range(n)]
    for d_sq, u, v in mst_edges:
        graph[u].append((v, d_sq))
        graph[v].append((u, d_sq))
    
    color = [0] * n
    color[0] = 1
    
    stack = [0]
    while stack:
        u = stack.pop()
        for v, d_sq in graph[u]:
            if color[v] == 0:
                color[v] = 3 - color[u]
                stack.append(v)
    
    min_edge = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            if color[i] == color[j]:
                d_sq = dist_sq(points[i], points[j])
                if d_sq < min_edge:
                    min_edge = d_sq
    
    max_power = math.sqrt(min_edge) / 2.0
    
    print(f"{max_power:.10f}")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    main()
