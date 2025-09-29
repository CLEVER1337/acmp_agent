
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    d = int(data[1])
    
    graph = [[] for _ in range(n + 1)]
    index = 2
    for i in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start):
        dist = [-1] * (n + 1)
        queue = deque([start])
        dist[start] = 0
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        return dist
    
    dist1 = bfs(1)
    u = max(range(1, n + 1), key=lambda x: dist1[x])
    dist_u = bfs(u)
    v = max(range(1, n + 1), key=lambda x: dist_u[x])
    dist_v = bfs(v)
    
    diameter = dist_u[v]
    if diameter < d:
        print(0)
        return
        
    cnt_u = [0] * (n + 1)
    cnt_v = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if dist_u[i] >= d and dist_v[i] >= d:
            cnt_u[dist_u[i]] += 1
            cnt_v[dist_v[i]] += 1
    
    total = 0
    for dist in range(d, n + 1):
        total += cnt_u[dist] * cnt_v[d - dist]
        
    print(total)

if __name__ == "__main__":
    main()
