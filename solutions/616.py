
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    graph = []
    for i in range(1, n+1):
        graph.append(list(map(int, list(data[i].strip()))))
    
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                adj[i].append(j)
                rev_adj[j].append(i)
    
    comp = [-1] * n
    visited = [False] * n
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
            
    visited = [False] * n
    comp_id = 0
    
    def dfs2(u, cid):
        comp[u] = cid
        visited[u] = True
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, cid)
                
    for u in reversed(order):
        if not visited[u]:
            dfs2(u, comp_id)
            comp_id += 1
            
    dag_adj = [[] for _ in range(comp_id)]
    in_degree = [0] * comp_id
    
    for u in range(n):
        for v in adj[u]:
            if comp[u] != comp[v]:
                dag_adj[comp[u]].append(comp[v])
                in_degree[comp[v]] += 1
                
    for i in range(comp_id):
        dag_adj[i] = list(set(dag_adj[i]))
        for j in dag_adj[i]:
            in_degree[j] += 1
            
    q = deque()
    dist_f = [0] * comp_id
    for i in range(comp_id):
        if in_degree[i] == 0:
            q.append(i)
            
    while q:
        u = q.popleft()
        for v in dag_adj[u]:
            in_degree[v] -= 1
            if dist_f[v] < dist_f[u] + 1:
                dist_f[v] = dist_f[u] + 1
            if in_degree[v] == 0:
                q.append(v)
                
    dist_g = [0] * comp_id
    for i in range(comp_id):
        dist_g[i] = dist_f[i]
        
    for u in range(comp_id):
        for v in dag_adj[u]:
            if dist_g[u] <= dist_g[v]:
                dist_g[u] = dist_g[v] + 1
                
    for i in range(n):
        for j in range(n):
            required = graph[i][j]
            has = 1 if dist_f[comp[i]] <= dist_g[comp[j]] else 0
            if required != has:
                print("NO")
                return
                
    f_vals = [dist_f[comp[i]] for i in range(n)]
    g_vals = [dist_g[comp[i]] for i in range(n)]
    
    print("YES")
    print(" ".join(map(str, f_vals)))
    print(" ".join(map(str, g_vals)))

if __name__ == "__main__":
    main()
