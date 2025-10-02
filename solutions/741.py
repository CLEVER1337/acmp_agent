
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    graph = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        graph[u].append((v, i))
        graph[v].append((u, i))
        degrees[u] += 1
        degrees[v] += 1
    
    max_degree = max(degrees) if n > 0 else 0
    k = max_degree if max_degree % 2 == 1 else max_degree + 1
    
    colors = [-1] * m
    used_colors = [False] * (k + 1)
    
    for u, v in edges:
        pass
    
    for node in range(1, n + 1):
        neighbors = graph[node]
        if not neighbors:
            continue
            
        available_colors = set(range(1, k + 1))
        for neighbor, edge_idx in neighbors:
            if colors[edge_idx] != -1:
                if colors[edge_idx] in available_colors:
                    available_colors.remove(colors[edge_idx])
        
        for neighbor, edge_idx in neighbors:
            if colors[edge_idx] == -1:
                if available_colors:
                    color = available_colors.pop()
                    colors[edge_idx] = color
                else:
                    colors[edge_idx] = 1
    
    print(k)
    for i, (u, v) in enumerate(edges):
        print(u, v, colors[i] if colors[i] != -1 else 1)

if __name__ == "__main__":
    main()
