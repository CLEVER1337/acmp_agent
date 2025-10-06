
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, k = map(int, data[0].split())
    graph = []
    for i in range(1, 1+n):
        graph.append(data[i].strip())
    
    routes = []
    for i in range(1+n, 1+n+k):
        parts = list(map(int, data[i].split()))
        routes.append(parts)
    
    in_degree = [0] * (n+1)
    adj = [[] for _ in range(n+1)]
    
    constraints = {}
    for route in routes:
        for i in range(len(route)-1):
            u = route[i]
            v = route[i+1]
            if u not in constraints:
                constraints[u] = set()
            constraints[u].add(v)
            for j in range(i+2, len(route)):
                w = route[j]
                constraints[u].add(w)
    
    for u in range(1, n+1):
        for v in range(1, n+1):
            if u == v:
                continue
            if u in constraints and v in constraints[u]:
                if graph[u-1][v-1] == '+':
                    adj[u].append(v)
                    in_degree[v] += 1
                else:
                    print(-1)
                    return
            elif v in constraints and u in constraints[v]:
                if graph[u-1][v-1] == '-':
                    adj[u].append(v)
                    in_degree[v] += 1
                else:
                    print(-1)
                    return
            else:
                if graph[u-1][v-1] == '+':
                    adj[u].append(v)
                    in_degree[v] += 1
                elif graph[u-1][v-1] == '-':
                    adj[v].append(u)
                    in_degree[u] += 1
    
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
