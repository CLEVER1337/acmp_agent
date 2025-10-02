
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
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            comp = []
            
            while queue:
                node = queue.popleft()
                comp.append(node)
                
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            components.append(comp)
    
    total_sum = 0
    
    for comp in components:
        size = len(comp)
        if size > 1:
            total_sum += size * (size - 1)
    
    print(total_sum)

if __name__ == "__main__":
    main()
