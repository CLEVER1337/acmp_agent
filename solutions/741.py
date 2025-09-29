
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
    deg = [0] * (n+1)
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        graph[u].append((v, i))
        graph[v].append((u, i))
        deg[u] += 1
        deg[v] += 1
    
    max_deg = max(deg)
    colors = [0] * m
    
    for i in range(m):
        u, v = edges[i]
        used_colors = set()
        
        for neighbor, edge_idx in graph[u]:
            if colors[edge_idx] != 0:
                used_colors.add(colors[edge_idx])
                
        for neighbor, edge_idx in graph[v]:
            if colors[edge_idx] != 0:
                used_colors.add(colors[edge_idx])
                
        color = 1
        while color in used_colors:
            color += 1
            
        colors[i] = color
    
    print(max_deg if max_deg % 2 == 1 else max_deg + 1)
    
    for i in range(m):
        u, v = edges[i]
        print(u, v, colors[i])

if __name__ == "__main__":
    main()
