
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])
    parents = list(map(int, data[3:3+n-1]))
    
    graph = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        p = parents[i-2]
        graph[p].append(i)
        graph[i].append(p)
    
    def bfs(start):
        dist = [-1] * (n+1)
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
    
    dist_a = bfs(a)
    dist_b = bfs(b)
    
    min_max_dist = float('inf')
    best_node = -1
    
    for node in range(1, n+1):
        max_dist = max(dist_a[node], dist_b[node])
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            best_node = node
    
    print(best_node)

if __name__ == "__main__":
    main()
