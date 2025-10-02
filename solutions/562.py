
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    graph = [[] for _ in range(n)]
    
    for i in range(m):
        u = int(data[2 + i*2]) - 1
        v = int(data[2 + i*2 + 1]) - 1
        graph[u].append(v)
    
    def bfs(start):
        dist = [-1] * n
        q = deque()
        dist[start] = 0
        q.append(start)
        
        while q:
            u = q.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist
    
    max_k = 0
    for i in range(n):
        dist = bfs(i)
        for j in range(n):
            if i != j:
                max_k = max(max_k, dist[j])
    
    print(max_k)

if __name__ == "__main__":
    main()
