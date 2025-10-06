
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(":(")
        return
        
    n = int(data[0])
    m = int(data[1])
    graph = [[] for _ in range(n+1)]
    edges = []
    index = 2
    
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        w = int(data[index+2])
        index += 3
        graph[u].append((v, w))
        edges.append((u, v, w))
    
    INF = -10**18
    dist = [INF] * (n+1)
    dist[1] = 0
    
    for i in range(n-1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[v] < dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    
    if dist[n] == INF:
        print(":(")
        return
    
    in_cycle = [False] * (n+1)
    for u, v, w in edges:
        if dist[u] != INF and dist[v] < dist[u] + w:
            in_cycle[u] = True
            in_cycle[v] = True
    
    if in_cycle[n]:
        print(":)")
        return
        
    visited = [False] * (n+1)
    queue = deque()
    for i in range(1, n+1):
        if in_cycle[i]:
            visited[i] = True
            queue.append(i)
    
    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    
    if visited[n]:
        print(":)")
    else:
        print(dist[n])

if __name__ == "__main__":
    main()
