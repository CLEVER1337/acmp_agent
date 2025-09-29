
import sys
from collections import defaultdict, deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print("NO")
        return
        
    n = int(data[0])
    m = int(data[1])
    
    graph = defaultdict(set)
    edges_set = set()
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        
        if u == v:
            continue
            
        edge = (min(u, v), max(u, v))
        if edge not in edges_set:
            edges_set.add(edge)
            graph[u].add(v)
            graph[v].add(u)
    
    if n < 3:
        print("NO")
        return
        
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    
    def has_cycle(node, par):
        visited[node] = True
        parent[node] = par
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if has_cycle(neighbor, node):
                    return True
            elif neighbor != par:
                cycle_length = 1
                current = node
                while current != neighbor:
                    cycle_length += 1
                    current = parent[current]
                if cycle_length >= 3:
                    return True
        return False
    
    for i in range(1, n + 1):
        if not visited[i]:
            if has_cycle(i, 0):
                print("YES")
                return
                
    print("NO")

if __name__ == "__main__":
    main()
