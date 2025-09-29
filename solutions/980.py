
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    graph = [[] for _ in range(n+1)]
    edges = {}
    
    for i in range(m):
        u = int(next(it)); v = int(next(it))
        graph[u].append(v)
        graph[v].append(u)
        edges[(min(u, v), max(u, v))] = i
        
    deg = [0] * (n+1)
    for i in range(1, n+1):
        deg[i] = len(graph[i])
        
    if n == 1:
        print(0)
        return
        
    remaining_edges = set(range(m))
    remaining_vertices = set(range(1, n+1))
    ear_decomposition = []
    
    bridge_edges = set()
    low = [0] * (n+1)
    disc = [0] * (n+1)
    parent = [0] * (n+1)
    time = 0
    
    def dfs_bridges(u, p):
        nonlocal time
        disc[u] = low[u] = time + 1
        time += 1
        for v in graph[u]:
            if v == p:
                continue
            if disc[v] == 0:
                parent[v] = u
                dfs_bridges(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    edge_key = (min(u, v), max(u, v))
                    bridge_edges.add(edges[edge_key])
            else:
                low[u] = min(low[u], disc[v])
                
    for i in range(1, n+1):
        if disc[i] == 0:
            dfs_bridges(i, 0)
            
    if len(bridge_edges) > 0:
        print(-1)
        return
        
    visited_edges = [False] * m
    visited_vertices = [False] * (n+1)
    ear_list = []
    
    def find_ear(start):
        stack = [start]
        path = []
        while stack:
            u = stack.pop()
            if visited_vertices[u]:
                continue
            path.append(u)
            visited_vertices[u] = True
            found = False
            for v in graph[u]:
                edge_key = (min(u, v), max(u, v))
                edge_idx = edges[edge_key]
                if not visited_edges[edge_idx]:
                    visited_edges[edge_idx] = True
                    stack.append(v)
                    found = True
                    break
            if not found:
                break
        return path
        
    for i in range(1, n+1):
        if deg[i] >= 2 and not visited_vertices[i]:
            ear = find_ear(i)
            if len(ear) >= 2:
                ear_list.append(ear)
                
    for ear in ear_list:
        k = len(ear) - 1
        ear_decomposition.append((k, ear))
        
    if len(ear_decomposition) == 0:
        print(-1)
        return
        
    print(len(ear_decomposition))
    for k, ear in ear_decomposition:
        print(k, end=' ')
        print(' '.join(map(str, ear)))
        
if __name__ == "__main__":
    main()
