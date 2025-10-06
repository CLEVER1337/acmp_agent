
import sys
from collections import deque, defaultdict
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    
    edges = []
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    
    for i in range(1, m+1):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w, i))
        graph[u].append((v, w, i))
        graph[v].append((u, w, i))
        reverse_graph[v].append((u, w, i))
        reverse_graph[u].append((v, w, i))
    
    INF = 10**18
    dist1 = [INF] * (n+1)
    dist1[1] = 0
    heap = [(0, 1)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist1[u]:
            continue
        for v, w, idx in graph[u]:
            if dist1[v] > dist1[u] + w:
                dist1[v] = dist1[u] + w
                heapq.heappush(heap, (dist1[v], v))
    
    distn = [INF] * (n+1)
    distn[n] = 0
    heap = [(0, n)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != distn[u]:
            continue
        for v, w, idx in reverse_graph[u]:
            if distn[v] > distn[u] + w:
                distn[v] = distn[u] + w
                heapq.heappush(heap, (distn[v], v))
    
    total_shortest = dist1[n]
    
    adj = [[] for _ in range(n+1)]
    for u, v, w, idx in edges:
        if dist1[u] + w + distn[v] == total_shortest:
            adj[u].append((v, idx))
            adj[v].append((u, idx))
        elif dist1[v] + w + distn[u] == total_shortest:
            adj[u].append((v, idx))
            adj[v].append((u, idx))
    
    low = [0] * (n+1)
    disc = [0] * (n+1)
    parent = [0] * (n+1)
    time = 0
    bridges = set()
    
    def dfs(u, p):
        nonlocal time
        time += 1
        disc[u] = time
        low[u] = time
        for v, idx in adj[u]:
            if v == p:
                continue
            if disc[v] == 0:
                parent[v] = u
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add(idx)
            else:
                low[u] = min(low[u], disc[v])
    
    for i in range(1, n+1):
        if disc[i] == 0:
            dfs(i, 0)
    
    result = sorted(bridges)
    print(len(result))
    if result:
        print(' '.join(map(str, result)))
    else:
        print()

if __name__ == "__main__":
    main()
