
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
    
    INF = float('inf')
    dist = [-INF] * (n+1)
    dist[1] = 0
    
    for i in range(n-1):
        updated = False
        for u, v, w in edges:
            if dist[u] != -INF and dist[v] < dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    
    if dist[n] == -INF:
        print(":(")
        return
    
    positive_cycle_nodes = set()
    for u, v, w in edges:
        if dist[u] != -INF and dist[v] < dist[u] + w:
            positive_cycle_nodes.add(u)
            positive_cycle_nodes.add(v)
    
    if positive_cycle_nodes:
        visited = [False] * (n+1)
        queue = deque()
        
        for node in positive_cycle_nodes:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
        
        while queue:
            u = queue.popleft()
            for v, w in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        
        if visited[n]:
            print(":)")
            return
    
    print(dist[n])

if __name__ == "__main__":
    main()
