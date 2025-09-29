
import sys
sys.setrecursionlimit(1000000)

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print(0)
        return
        
    graph = [[] for _ in range(n + 1)]
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    disc = [-1] * (n + 1)
    low = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    time = 0
    bridges = []
    
    def dfs(u):
        nonlocal time
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1
        
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    visited_comp = [False] * (n + 1)
    comp_id = [0] * (n + 1)
    comp_count = 0
    
    def dfs_comp(u, cid):
        visited_comp[u] = True
        comp_id[u] = cid
        for v in graph[u]:
            if not visited_comp[v]:
                dfs_comp(v, cid)
    
    for i in range(1, n + 1):
        if not visited_comp[i]:
            comp_count += 1
            dfs_comp(i, comp_count)
    
    deg = [0] * (comp_count + 1)
    for u, v in bridges:
        deg[comp_id[u]] += 1
        deg[comp_id[v]] += 1
    
    leaves = 0
    for i in range(1, comp_count + 1):
        if deg[i] == 1:
            leaves += 1
    
    if comp_count == 1:
        print(0)
    else:
        print((leaves + 1) // 2)

if __name__ == "__main__":
    main()
