
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, k = map(int, data[0].split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        line = data[i].strip()
        for j in range(1, n+1):
            if i == j:
                continue
            if line[j-1] == '+':
                graph[j][i] = 1
            elif line[j-1] == '-':
                graph[i][j] = 1
    
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
            if v not in constraints:
                constraints[v] = set()
            constraints[v].add(u)
    
    for v in range(1, n+1):
        if v in constraints:
            for u in constraints[v]:
                if graph[u][v] == 1:
                    adj[u].append(v)
                    in_degree[v] += 1
    
    for u in range(1, n+1):
        for v in range(1, n+1):
            if u != v and graph[u][v] == 1:
                if v in constraints and u not in constraints[v]:
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
