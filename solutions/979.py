
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    nodes = []
    index = 1
    for i in range(n):
        x = int(data[index]); y = int(data[index+1]); index += 2
        nodes.append((x, y))
    
    start = 0
    end = n - 1
    
    graph = {}
    for i in range(n):
        graph[i] = []
    
    for i in range(n):
        for j in range(i + 1, n):
            dx = abs(nodes[i][0] - nodes[j][0])
            dy = abs(nodes[i][1] - nodes[j][1])
            if dx <= 1 and dy <= 1:
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [-1] * n
    prev = [-1] * n
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        current = queue.popleft()
        if current == end:
            break
            
        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                prev[neighbor] = current
                queue.append(neighbor)
    
    if visited[end] == -1:
        print(-1)
    else:
        path = []
        current = end
        while current != -1:
            path.append(current + 1)
            current = prev[current]
        
        path.reverse()
        print(visited[end])
        print(" ".join(map(str, path)))

if __name__ == "__main__":
    main()
