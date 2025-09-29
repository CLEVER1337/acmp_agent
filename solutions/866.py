
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
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n+1):
        graph[i].sort()
    
    visited = [False] * (n+1)
    order1 = []
    stack = [1]
    visited[1] = True
    
    while stack:
        u = stack.pop()
        order1.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    visited = [False] * (n+1)
    order2 = []
    queue = deque([1])
    visited[1] = True
    
    while queue:
        u = queue.popleft()
        order2.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    
    print(' '.join(map(str, order1)))
    print(' '.join(map(str, order2)))

if __name__ == "__main__":
    main()
