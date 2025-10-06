
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
    degree = [0] * (n+1)
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    max_degree = max(degree) if n > 0 else 0
    k = max_degree if max_degree % 2 == 1 else max_degree + 1
    
    color_map = {}
    for u, v in edges:
        color_map[(min(u, v), max(u, v))] = -1
    
    for node in range(1, n+1):
        used_colors = set()
        available_edges = []
        
        for neighbor in graph[node]:
            edge_key = (min(node, neighbor), max(node, neighbor))
            if color_map[edge_key] != -1:
                used_colors.add(color_map[edge_key])
            else:
                available_edges.append(neighbor)
        
        available_colors = []
        for c in range(k):
            if c not in used_colors:
                available_colors.append(c)
        
        idx = 0
        for neighbor in available_edges:
            edge_key = (min(node, neighbor), max(node, neighbor))
            if color_map[edge_key] == -1:
                color_map[edge_key] = available_colors[idx]
                idx += 1
    
    print(k)
    for u, v in edges:
        edge_key = (min(u, v), max(u, v))
        color = color_map[edge_key]
        print(u, v, color + 1)

if __name__ == "__main__":
    main()
