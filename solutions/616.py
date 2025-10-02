
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("NO")
        return
        
    n = int(data[0])
    matrix = []
    for i in range(1, 1 + n):
        row = data[i].strip()
        matrix.append([int(c) for c in row])
    
    graph = [[] for _ in range(n)]
    trans_graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                graph[i].append(j)
                trans_graph[j].append(i)
    
    visited = [False] * n
    order = []
    
    def dfs1(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs1(u)
        order.append(v)
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
            
    comp = [-1] * n
    comp_list = []
    
    def dfs2(v, c):
        comp[v] = c
        comp_list[-1].append(v)
        for u in trans_graph[v]:
            if comp[u] == -1:
                dfs2(u, c)
    
    comp_count = 0
    visited = [False] * n
    for i in range(n - 1, -1, -1):
        v = order[i]
        if comp[v] == -1:
            comp_list.append([])
            dfs2(v, comp_count)
            comp_count += 1
            
    comp_graph = [[] for _ in range(comp_count)]
    in_degree = [0] * comp_count
    
    for i in range(n):
        for j in graph[i]:
            if comp[i] != comp[j]:
                comp_graph[comp[i]].append(comp[j])
                in_degree[comp[j]] += 1
                
    for i in range(comp_count):
        comp_graph[i] = list(set(comp_graph[i]))
    
    topo_order = []
    q = deque()
    for i in range(comp_count):
        if in_degree[i] == 0:
            q.append(i)
            
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in comp_graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                
    f_vals = [0] * comp_count
    g_vals = [0] * comp_count
    
    for comp_id in reversed(topo_order):
        max_g = -10**18
        for v in comp_list[comp_id]:
            for u in graph[v]:
                if comp[u] != comp_id:
                    if g_vals[comp[u]] > max_g:
                        max_g = g_vals[comp[u]]
        
        if max_g == -10**18:
            f_vals[comp_id] = 0
        else:
            f_vals[comp_id] = max_g - 1
            
        min_f = 10**18
        for v in comp_list[comp_id]:
            for u in trans_graph[v]:
                if comp[u] != comp_id:
                    if f_vals[comp[u]] < min_f:
                        min_f = f_vals[comp[u]]
        
        if min_f == 10**18:
            g_vals[comp_id] = f_vals[comp_id] + 1
        else:
            g_vals[comp_id] = min_f + 1
            
    f_res = [0] * n
    g_res = [0] * n
    
    for comp_id in range(comp_count):
        for node in comp_list[comp_id]:
            f_res[node] = f_vals[comp_id]
            g_res[node] = g_vals[comp_id]
            
    for i in range(n):
        for j in range(n):
            expected = 1 if f_res[i] <= g_res[j] else 0
            if matrix[i][j] != expected:
                print("NO")
                return
                
    print("YES")
    print(" ".join(map(str, f_res)))
    print(" ".join(map(str, g_res)))

if __name__ == "__main__":
    main()
