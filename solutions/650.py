
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    
    graph = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(data[2 + 2 * i])
        v = int(data[3 + 2 * i])
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    total_sum = 0
    
    for i in range(1, n + 1):
        if not visited[i]:
            component_nodes = []
            queue = deque([i])
            visited[i] = True
            
            while queue:
                node = queue.popleft()
                component_nodes.append(node)
                
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            k = len(component_nodes)
            total_sum += k * (k - 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            total_sum += 1
    
    print(total_sum)

if __name__ == "__main__":
    main()
