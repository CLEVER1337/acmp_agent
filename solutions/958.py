
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, k = map(int, data[0].split())
    graph = [['' for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        line = data[i].strip()
        for j in range(1, n+1):
            if i == j:
                continue
            graph[i][j] = line[j-1]
    
    routes = []
    for i in range(n+1, n+1+k):
        route = list(map(int, data[i].split()))
        routes.append(route)
    
    in_degree = [0] * (n+1)
    adj = [[] for _ in range(n+1)]
    
    constraints = {}
    for route in routes:
        for i in range(len(route)-1):
            u, v = route[i], route[i+1]
            if u not in constraints:
                constraints[u] = set()
            constraints[u].add(v)
    
    for u in range(1, n+1):
        for v in range(1, n+1):
            if u == v:
                continue
            if graph[u][v] == '+':
                adj[u].append(v)
                in_degree[v] += 1
            elif graph[u][v] == '-':
                adj[v].append(u)
                in_degree[u] += 1
    
    for u in constraints:
        for v in constraints[u]:
            if v not in adj[u]:
                adj[u].append(v)
                in_degree[v] += 1
    
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
    
    result = []
    while q:
        if len(q) > 1:
            print(-1)
            return
        u = q.popleft()
        result.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    if len(result) != n:
        print(-1)
    else:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
