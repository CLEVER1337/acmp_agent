
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
        q = deque([start])
        dist[start] = 0
        while q:
            u = q.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist
    
    dist1 = bfs(1)
    u = max(range(1, n + 1), key=lambda x: dist1[x])
    dist_u = bfs(u)
    v = max(range(1, n + 1), key=lambda x: dist_u[x])
    dist_v = bfs(v)
    
    diameter = dist_u[v]
    if d > diameter:
        print(0)
        return
        
    center = None
    for i in range(1, n + 1):
        if dist_u[i] + dist_v[i] == diameter and abs(dist_u[i] - dist_v[i]) <= 1:
            center = i
            break
            
    if center is None:
        print(0)
        return
        
    dist_center = bfs(center)
    
    count = [0] * (n + 1)
    for i in range(1, n + 1):
        if dist_center[i] <= n:
            count[dist_center[i]] += 1
            
    if d % 2 == 0:
        r = d // 2
        if r >= len(count):
            print(0)
            return
            
        total = 0
        for dist in range(r + 1, min(n + 1, r + d + 1)):
            if dist < len(count):
                total += count[dist]
                
        result = count[r] * (total * (total - 1) // 2)
        print(result)
    else:
        r1 = d // 2
        r2 = r1 + 1
        if r1 >= len(count) or r2 >= len(count):
            print(0)
            return
            
        total1 = count[r1]
        total2 = count[r2]
        
        result = total1 * total2 * (total1 + total2 - 2) // 2
        print(result)

if __name__ == "__main__":
    main()
