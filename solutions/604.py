
def main():
    import sys
    sys.setrecursionlimit(10000)
    n = int(input().strip())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    parent = [0] * (n+1)
    depth = [0] * (n+1)
    order = []
    stack = [1]
    parent[1] = 0
    depth[1] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            stack.append(v)
    
    dp = [1] * (n+1)
    ways = [1] * (n+1)
    size = [1] * (n+1)
    
    for u in reversed(order):
        for v in graph[u]:
            if v == parent[u]:
                continue
            ways[u] = ways[u] * ways[v] * (size[u] + size[v]) // (size[u] * size[v])
            size[u] += size[v]
    
    print(ways[1])
