
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    
    graph = [[] for _ in range(n+1)]
    edges = []
    
    for i in range(m):
        u = int(next(it)); v = int(next(it)); t = int(next(it))
        graph[u].append((v, t, i))
        graph[v].append((u, t, i))
        edges.append((u, v, t))
    
    dist = [-1] * (n+1)
    parent = [0] * (n+1)
    parent_type = [0] * (n+1)
    dist[1] = 0
    q = deque([1])
    
    while q:
        u = q.popleft()
        for v, t, idx in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + t
                parent[v] = u
                parent_type[v] = t
                q.append(v)
    
    tree_edges = set()
    back_edges = []
    
    for i, (u, v, t) in enumerate(edges):
        if (parent[u] == v and parent_type[u] == t) or (parent[v] == u and parent_type[v] == t):
            tree_edges.add(i)
        else:
            back_edges.append((u, v, t, i))
    
    depth = [0] * (n+1)
    for i in range(2, n+1):
        depth[i] = depth[parent[i]] + 1
    
    up = [[0] * (n+1) for _ in range(17)]
    for i in range(1, n+1):
        up[0][i] = parent[i]
    
    for k in range(1, 17):
        for i in range(1, n+1):
            up[k][i] = up[k-1][up[k-1][i]]
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        d = depth[u] - depth[v]
        k = 0
        while d:
            if d & 1:
                u = up[k][u]
            d //= 2
            k += 1
        if u == v:
            return u
        for k in range(16, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return parent[u]
    
    stone_count = [0] * (n+1)
    dirt_count = [0] * (n+1)
    
    for u, v, t, idx in back_edges:
        w = lca(u, v)
        if t == 1:
            stone_count[u] += 1
            stone_count[v] += 1
            stone_count[w] -= 2
        else:
            dirt_count[u] += 1
            dirt_count[v] += 1
            dirt_count[w] -= 2
    
    stack = []
    for i in range(1, n+1):
        if depth[i] > 0:
            stack.append(i)
    
    stack.sort(key=lambda x: depth[x], reverse=True)
    
    for u in stack:
        p = parent[u]
        stone_count[p] += stone_count[u]
        dirt_count[p] += dirt_count[u]
    
    total = 0
    for i in range(2, n+1):
        if parent_type[i] == 1:
            if stone_count[i] == 0:
                total += dirt_count[i]
            if dirt_count[i] == 0:
                total += 1
        else:
            if stone_count[i] == 0:
                total += 1
    
    print(total)

if __name__ == "__main__":
    main()
