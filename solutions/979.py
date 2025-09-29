
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
    
    start = nodes[0]
    end = nodes[n-1]
    
    graph = {}
    for i in range(n):
        graph[i] = []
    
    for i in range(n):
        for j in range(i+1, n):
            dx = abs(nodes[i][0] - nodes[j][0])
            dy = abs(nodes[i][1] - nodes[j][1])
            if dx <= 1 and dy <= 1:
                graph[i].append(j)
                graph[j].append(i)
    
    if n == 1:
        print(0)
        print(1)
        return
        
    dist = [-1] * n
    prev = [-1] * n
    queue = deque()
    queue.append(0)
    dist[0] = 0
    
    while queue:
        u = queue.popleft()
        if u == n-1:
            break
            
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                prev[v] = u
                queue.append(v)
    
    if dist[n-1] == -1:
        print(-1)
        return
        
    path = []
    cur = n-1
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    
    print(len(path) - 1)
    print(' '.join(str(x+1) for x in path))

if __name__ == "__main__":
    main()
