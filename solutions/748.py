
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    parents = list(map(int, data[1:1+n-1]))
    
    graph = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        p = parents[i-2]
        graph[p].append(i)
    
    depth = [0] * (n+1)
    q = deque([1])
    while q:
        u = q.popleft()
        for v in graph[u]:
            depth[v] = depth[u] + 1
            q.append(v)
    
    max_depth = max(depth)
    colors = [0] * (n+1)
    colors[1] = 1
    
    for u in range(2, n+1):
        colors[u] = depth[u] % max_depth + 1
    
    print(max_depth)
    print(' '.join(str(colors[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()
