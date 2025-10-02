
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    index = 2
    
    graph = [[] for _ in range(n+1)]
    edges = []
    
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); t = int(data[index+2])
        index += 3
        graph[u].append((v, t))
        graph[v].append((u, t))
        edges.append((u, v, t))
    
    dist = [-1] * (n+1)
    parent = [0] * (n+1)
    parent_type = [0] * (n+1)
    
    q = deque()
    dist[1] = 0
    q.append(1)
    
    while q:
        u = q.popleft()
        for v, t in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                parent_type[v] = t
                q.append(v)
    
    tree_edges = set()
    back_edges = []
    
    for u, v, t in edges:
        if (parent[u] == v and parent_type[u] == t) or (parent[v] == u and parent_type[v] == t):
            tree_edges.add((min(u, v), max(u, v), t))
        else:
            back_edges.append((min(u, v), max(u, v), t))
    
    cnt = [0] * (n+1)
    for i in range(2, n+1):
        cnt[i] = 1
    
    order = list(range(2, n+1))
    order.sort(key=lambda x: dist[x], reverse=True)
    
    for u in order:
        cnt[parent[u]] += cnt[u]
    
    result = 0
    
    for u, v, t in back_edges:
        if dist[u] > dist[v]:
            u, v = v, u
        
        if t == 0:
            if dist[v] == dist[u] + 1:
                continue
            
            if cnt[v] == 1:
                result += 1
        else:
            if dist[v] == dist[u] + 1:
                continue
            
            if cnt[v] == 1:
                result += 1
    
    for u, v, t in tree_edges:
        if t == 1:
            if cnt[v] if dist[u] < dist[v] else cnt[u] == 1:
                result += 1
    
    print(result)

if __name__ == "__main__":
    main()
