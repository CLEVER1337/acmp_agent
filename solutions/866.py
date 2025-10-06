
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    graph = [[] for _ in range(n+1)]
    index = 2
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n+1):
        graph[i].sort()
    
    visited = [False] * (n+1)
    order = []
    stack = [1]
    visited[1] = True
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v in reversed(graph[u]):
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    print(' '.join(map(str, order)))
    
    visited2 = [False] * (n+1)
    order2 = []
    q = deque([1])
    visited2[1] = True
    
    while q:
        u = q.popleft()
        order2.append(u)
        for v in graph[u]:
            if not visited2[v]:
                visited2[v] = True
                q.append(v)
    
    print(' '.join(map(str, order2)))

if __name__ == "__main__":
    main()
