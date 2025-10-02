
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(":(")
        return
        
    n = int(data[0])
    m = int(data[1])
    index = 2
    
    graph = [[] for _ in range(n + 1)]
    edges = []
    
    for i in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        index += 3
        graph[u].append(v)
        edges.append((u, v, w))
    
    def bfs(start):
        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return visited
    
    reachable_from_start = bfs(1)
    if not reachable_from_start[n]:
        print(":(")
        return
        
    reverse_graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        reverse_graph[v].append(u)
    
    def reverse_bfs(start):
        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True
        while queue:
            u = queue.popleft()
            for v in reverse_graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return visited
    
    reachable_to_end = reverse_bfs(n)
    
    useful_nodes = [False] * (n + 1)
    for i in range(1, n + 1):
        useful_nodes[i] = reachable_from_start[i] and reachable_to_end[i]
    
    dist = [-10**18] * (n + 1)
    dist[1] = 0
    
    for i in range(n):
        updated = False
        for u, v, w in edges:
            if useful_nodes[u] and useful_nodes[v]:
                if dist[u] != -10**18 and dist[v] < dist[u] + w:
                    dist[v] = dist[u] + w
                    updated = True
        if not updated:
            break
    
    for u, v, w in edges:
        if useful_nodes[u] and useful_nodes[v]:
            if dist[u] != -10**18 and dist[v] < dist[u] + w:
                print(":)")
                return
                
    if dist[n] == -10**18:
        print(":(")
    else:
        print(dist[n])

if __name__ == "__main__":
    main()
