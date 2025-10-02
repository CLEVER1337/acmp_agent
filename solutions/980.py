
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0]); m = int(data[1])
    graph = [[] for _ in range(n+1)]
    edges = {}
    
    index = 2
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); index += 2
        graph[u].append(v)
        graph[v].append(u)
        edges[(min(u, v), max(u, v))] = i
    
    deg = [0] * (n+1)
    for i in range(1, n+1):
        deg[i] = len(graph[i])
    
    if n == 1:
        print(0)
        return
        
    if n == 2:
        if m == 1:
            print(1)
            print(f"1 1 2")
            return
        else:
            print(-1)
            return
    
    used_edge = [False] * m
    ear_decomposition = []
    
    parent = [0] * (n+1)
    depth = [0] * (n+1)
    low = [0] * (n+1)
    visited = [False] * (n+1)
    stack = []
    
    def dfs(u, p):
        visited[u] = True
        depth[u] = depth[p] + 1
        low[u] = depth[u]
        for v in graph[u]:
            if v == p:
                continue
            if not visited[v]:
                parent[v] = u
                dfs(v, u)
                low[u] = min(low[u], low[v])
            else:
                low[u] = min(low[u], depth[v])
    
    dfs(1, 0)
    
    is_2_connected = True
    for u in range(2, n+1):
        if low[u] >= depth[u]:
            is_2_connected = False
            break
            
    if not is_2_connected:
        print(-1)
        return
        
    remaining_edges = set(range(m))
    ear_id = 0
    
    while remaining_edges:
        found_ear = False
        for u in range(1, n+1):
            if deg[u] >= 2:
                for v in graph[u]:
                    if deg[v] == 2:
                        ear = []
                        ear.append(u)
                        current = v
                        prev = u
                        while deg[current] == 2:
                            ear.append(current)
                            next_node = None
                            for neighbor in graph[current]:
                                if neighbor != prev:
                                    next_node = neighbor
                                    break
                            if next_node is None:
                                break
                            prev = current
                            current = next_node
                        ear.append(current)
                        if deg[current] >= 2:
                            k = len(ear) - 1
                            ear_decomposition.append((k, ear))
                            for i in range(k):
                                a, b = min(ear[i], ear[i+1]), max(ear[i], ear[i+1])
                                edge_idx = edges[(a, b)]
                                if edge_idx in remaining_edges:
                                    remaining_edges.remove(edge_idx)
                                    deg[ear[i]] -= 1
                                    deg[ear[i+1]] -= 1
                            found_ear = True
                            break
                if found_ear:
                    break
        if not found_ear:
            for u in range(1, n+1):
                if deg[u] >= 2:
                    for v in graph[u]:
                        if deg[v] >= 2 and u != v:
                            a, b = min(u, v), max(u, v)
                            edge_idx = edges[(a, b)]
                            if edge_idx in remaining_edges:
                                ear = [u, v]
                                k = 1
                                ear_decomposition.append((k, ear))
                                remaining_edges.remove(edge_idx)
                                deg[u] -= 1
                                deg[v] -= 1
                                found_ear = True
                                break
                    if found_ear:
                        break
            if not found_ear:
                break
    
    if len(remaining_edges) > 0:
        print(-1)
        return
        
    print(len(ear_decomposition))
    for k, ear in ear_decomposition:
        print(f"{k} {' '.join(map(str, ear))}")

if __name__ == "__main__":
    main()
