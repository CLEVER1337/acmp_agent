
import sys
from collections import deque, defaultdict
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    
    edges = []
    graph = [[] for _ in range(n+1)]
    
    for i in range(1, m+1):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w, i))
        graph[u].append((v, w, i))
        graph[v].append((u, w, i))
    
    def dijkstra(start):
        dist = [10**18] * (n+1)
        dist[start] = 0
        heap = [(0, start)]
        
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w, idx in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))
        return dist
    
    dist1 = dijkstra(1)
    distn = dijkstra(n)
    shortest = dist1[n]
    
    if shortest == 10**18:
        print(0)
        return
    
    graph_dag = [[] for _ in range(n+1)]
    graph_dag_rev = [[] for _ in range(n+1)]
    
    for u in range(1, n+1):
        for v, w, idx in graph[u]:
            if dist1[u] + w + distn[v] == shortest or dist1[v] + w + distn[u] == shortest:
                graph_dag[u].append((v, idx))
                graph_dag_rev[v].append((u, idx))
    
    order = []
    visited = [False] * (n+1)
    
    def dfs(u):
        visited[u] = True
        for v, idx in graph_dag[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    
    comp = [0] * (n+1)
    comp_id = 0
    visited2 = [False] * (n+1)
    
    def dfs_rev(u, comp_id_val):
        visited2[u] = True
        comp[u] = comp_id_val
        for v, idx in graph_dag_rev[u]:
            if not visited2[v]:
                dfs_rev(v, comp_id_val)
    
    for u in reversed(order):
        if not visited2[u]:
            comp_id += 1
            dfs_rev(u, comp_id)
    
    bridges = []
    for u in range(1, n+1):
        for v, idx in graph_dag[u]:
            if comp[u] != comp[v]:
                bridges.append(idx)
    
    bridges = sorted(set(bridges))
    print(len(bridges))
    if bridges:
        print(' '.join(map(str, bridges)))
    else:
        print()

if __name__ == '__main__':
    main()
