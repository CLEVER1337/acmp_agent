
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    graph = [[] for _ in range(n+1)]
    edges = []
    index = 2
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); t = int(data[index+2]); index += 3
        graph[u].append((v, t))
        graph[v].append((u, t))
        edges.append((u, v, t))
    
    dist = [-1] * (n+1)
    parent = [0] * (n+1)
    road_type = [0] * (n+1)
    dist[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        for v, t in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                road_type[v] = t
                q.append(v)
    
    tree_edges = set()
    back_edges = []
    for u, v, t in edges:
        if (parent[u] == v and road_type[u] == t) or (parent[v] == u and road_type[v] == t):
            tree_edges.add((min(u, v), max(u, v)))
        else:
            if dist[u] < dist[v]:
                u, v = v, u
            back_edges.append((u, v, t))
    
    low = [0] * (n+1)
    disc = [-1] * (n+1)
    time = 0
    bridges = set()
    def dfs(u, p):
        nonlocal time
        disc[u] = time
        low[u] = time
        time += 1
        for v, t in graph[u]:
            if v == p:
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add((min(u, v), max(u, v)))
            else:
                low[u] = min(low[u], disc[v])
    
    for i in range(1, n+1):
        if disc[i] == -1:
            dfs(i, -1)
    
    stone_bridges = set()
    for u, v in bridges:
        if (u, v) in tree_edges or (v, u) in tree_edges:
            stone_bridges.add((min(u, v), max(u, v)))
    
    count_back = [0] * (n+1)
    for u, v, t in back_edges:
        if t == 0:
            count_back[u] += 1
            count_back[v] += 1
    
    total = 0
    for u, v, t in edges:
        if t == 1:
            if (min(u, v), max(u, v)) in stone_bridges:
                total += 1
        else:
            if count_back[u] > 1 or count_back[v] > 1:
                continue
            total += 1
    
    print(total)

if __name__ == "__main__":
    main()
