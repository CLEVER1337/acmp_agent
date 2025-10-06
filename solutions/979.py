
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
    
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    
    node_map = {}
    for idx, (x, y) in enumerate(nodes):
        node_map[(x, y)] = idx
    
    for idx, (x, y) in enumerate(nodes):
        for d in range(9):
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx, ny) in node_map:
                neighbor_idx = node_map[(nx, ny)]
                graph[idx].append(neighbor_idx)
    
    dist = [-1] * n
    prev = [-1] * n
    queue = deque()
    dist[start] = 0
    prev[start] = -1
    queue.append(start)
    
    while queue:
        current = queue.popleft()
        if current == end:
            break
            
        for neighbor in graph[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                prev[neighbor] = current
                queue.append(neighbor)
    
    if dist[end] == -1:
        print(-1)
    else:
        path = []
        current = end
        while current != -1:
            path.append(current)
            current = prev[current]
        path.reverse()
        
        print(dist[end])
        print(" ".join(str(node + 1) for node in path))

if __name__ == "__main__":
    main()
