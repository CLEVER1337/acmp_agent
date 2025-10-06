
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
        
    visited = [False] * (n+1)
    parent = [0] * (n+1)
    low = [0] * (n+1)
    disc = [0] * (n+1)
    time = 0
    is_bridge = [False] * (m+1)
    
    def bridge_dfs(u, p):
        nonlocal time
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1
        
        for v in graph[u]:
            if v == p:
                continue
            if not visited[v]:
                parent[v] = u
                bridge_dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    edge_key = (min(u, v), max(u, v))
                    if edge_key in edges:
                        idx = edges[edge_key]
                        is_bridge[idx] = True
            else:
                low[u] = min(low[u], disc[v])
                
    for i in range(1, n+1):
        if not visited[i]:
            bridge_dfs(i, -1)
            
    comp_id = [0] * (n+1)
    comp_count = 0
    visited_comp = [False] * (n+1)
    
    def mark_component(u, cid):
        stack = [u]
        comp_id[u] = cid
        visited_comp[u] = True
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if not visited_comp[neighbor]:
                    edge_key = (min(node, neighbor), max(node, neighbor))
                    idx = edges[edge_key]
                    if not is_bridge[idx]:
                        comp_id[neighbor] = cid
                        visited_comp[neighbor] = True
                        stack.append(neighbor)
                        
    for i in range(1, n+1):
        if not visited_comp[i]:
            comp_count += 1
            mark_component(i, comp_count)
            
    comp_deg = [0] * (comp_count+1)
    for i in range(1, n+1):
        for j in graph[i]:
            if i < j:
                edge_key = (i, j)
                idx = edges[edge_key]
                if is_bridge[idx]:
                    comp_deg[comp_id[i]] += 1
                    comp_deg[comp_id[j]] += 1
                    
    odd_count = 0
    for i in range(1, comp_count+1):
        if comp_deg[i] % 2 == 1:
            odd_count += 1
            
    if odd_count > 2:
        print(-1)
        return
        
    if comp_count > 1:
        print(-1)
        return
        
    ear_decomposition = []
    remaining_edges = set(range(m))
    deg_remaining = deg[:]
    is_removed = [False] * (n+1)
    edge_removed = [False] * (m)
    
    def find_ear():
        for u in range(1, n+1):
            if not is_removed[u] and deg_remaining[u] == 1:
                v = -1
                for neighbor in graph[u]:
                    edge_key = (min(u, neighbor), max(u, neighbor))
                    idx = edges[edge_key]
                    if not edge_removed[idx]:
                        v = neighbor
                        break
                if v == -1:
                    continue
                    
                path = [u]
                current = u
                prev = -1
                while True:
                    found = False
                    for neighbor in graph[current]:
                        if neighbor == prev:
                            continue
                        edge_key = (min(current, neighbor), max(current, neighbor))
                        idx = edges[edge_key]
                        if not edge_removed[idx]:
                            if deg_remaining[neighbor] > 2 or (deg_remaining[neighbor] == 1 and len(path) >= 1):
                                path.append(neighbor)
                                return path
                            elif deg_remaining[neighbor] == 2:
                                path.append(neighbor)
                                prev = current
                                current = neighbor
                                found = True
                                break
                    if not found:
                        break
                if len(path) > 1 and deg_remaining[path[-1]] >= 2:
                    return path
        return None
        
    while remaining_edges:
        ear = find_ear()
        if ear is None:
            break
            
        k = len(ear) - 1
        ear_decomposition.append(ear)
        for i in range(k):
            u = ear[i]
            v = ear[i+1]
            edge_key = (min(u, v), max(u, v))
            idx = edges[edge_key]
            if idx in remaining_edges:
                remaining_edges.remove(idx)
                edge_removed[idx] = True
                deg_remaining[u] -= 1
                deg_remaining[v] -= 1
                
        for i in range(1, len(ear)-1):
            if not is_removed[ear[i]]:
                is_removed[ear[i]] = True
                
    if remaining_edges:
        print(-1)
        return
        
    print(len(ear_decomposition))
    for ear in ear_decomposition:
        k = len(ear) - 1
        print(k, end=' ')
        for vertex in ear:
            print(vertex, end=' ')
        print()
        
if __name__ == "__main__":
    main()
