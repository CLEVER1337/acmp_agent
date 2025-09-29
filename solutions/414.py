
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    target1 = int(data[1])
    target2 = int(data[2])
    parents = list(map(int, data[3:3+n-1]))
    
    graph = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        parent = parents[i-2]
        graph[parent].append(i)
        graph[i].append(parent)
    
    def bfs(start):
        dist = [-1] * (n+1)
        queue = deque()
        dist[start] = 0
        queue.append(start)
        
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        return dist
    
    dist1 = bfs(target1)
    dist2 = bfs(target2)
    
    min_max_dist = float('inf')
    result = 0
    
    for i in range(1, n+1):
        max_dist = max(dist1[i], dist2[i])
        if max_dist < min_max_dist:
            min_max_dist = max_dist
            result = i
        elif max_dist == min_max_dist and i < result:
            result = i
            
    print(result)

if __name__ == "__main__":
    main()
