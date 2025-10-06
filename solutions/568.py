
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    graph = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
    
    odd_vertices = []
    for i in range(1, n + 1):
        if degrees[i] % 2 != 0:
            odd_vertices.append(i)
    
    if len(odd_vertices) == 0:
        start = 1
    else:
        start = odd_vertices[0]
    
    stack = [start]
    path = []
    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            graph[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())
    
    print(len(path) - 1)
    print(" ".join(map(str, path)))

if __name__ == "__main__":
    main()
