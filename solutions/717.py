
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    p = list(map(int, data[1:1+n]))
    index = 1 + n
    
    graph = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    required_by = [[] for _ in range(n+1)]
    
    for i in range(1, n+1):
        ki = int(data[index]); index += 1
        for j in range(ki):
            dep = int(data[index]); index += 1
            graph[dep].append(i)
            in_degree[i] += 1
            required_by[i].append(dep)
    
    topo_order = []
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
    
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    dp = [0] * (n+1)
    for node in topo_order:
        max_prev = 0
        for dep in required_by[node]:
            if dp[dep] > max_prev:
                max_prev = dp[dep]
        dp[node] = max_prev + p[node-1]
    
    result_order = []
    visited = [False] * (n+1)
    
    def dfs(u):
        if visited[u]:
            return
        visited[u] = True
        
        deps_with_time = []
        for dep in required_by[u]:
            deps_with_time.append((dp[dep], dep))
        
        deps_with_time.sort(reverse=True)
        
        for _, dep in deps_with_time:
            dfs(dep)
        
        result_order.append(u)
    
    dfs(1)
    
    print(f"{dp[1]} {len(result_order)}")
    print(" ".join(map(str, result_order)))

if __name__ == "__main__":
    main()
