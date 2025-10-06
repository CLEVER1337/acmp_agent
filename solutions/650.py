
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
    total_sum = 0
    
    for i in range(1, n + 1):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            component = []
            
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            size = len(component)
            total_sum += size * (size - 1)
    
    result = 0
    for i in range(1, n + 1):
        if not graph[i]:
            continue
            
        visited = [False] * (n + 1)
        distance = [0] * (n + 1)
        queue = deque([i])
        visited[i] = True
        
        while queue:
            node = queue.popleft()
            result += distance[node]
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
    
    print(result - total_sum)

if __name__ == "__main__":
    main()
