
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    graph = [[] for _ in range(n+1)]
    stone_edges = []
    dirt_edges = []
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        t = int(data[index+2])
        index += 3
        edges.append((u, v, t))
        graph[u].append((v, t))
        graph[v].append((u, t))
        if t == 1:
            stone_edges.append((u, v))
        else:
            dirt_edges.append((u, v))
    
    dist = [-1] * (n+1)
    parent = [0] * (n+1)
    dist[1] = 0
    q = deque([1])
    
    while q:
        u = q.popleft()
        for v, t in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)
    
    tree_edges = set()
    for u in range(2, n+1):
        tree_edges.add((min(u, parent[u]), max(u, parent[u])))
    
    stone_tree_edges = []
    for u, v in stone_edges:
        if (min(u, v), max(u, v)) in tree_edges:
            stone_tree_edges.append((u, v))
    
    dirt_tree_edges = []
    for u, v in dirt_edges:
        if (min(u, v), max(u, v)) in tree_edges:
            dirt_tree_edges.append((u, v))
    
    count = 0
    for stone_edge in stone_tree_edges:
        for dirt_edge in dirt_tree_edges:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()
