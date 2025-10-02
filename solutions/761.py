
def main():
    import sys
    sys.setrecursionlimit(1000000)
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
    parent = [0] * (n + 1)
    disc = [0] * (n + 1)
    low = [0] * (n + 1)
    time = 0
    bridges = []
    
    def dfs(u):
        nonlocal time
        visited[u] = True
        disc[u] = low[u] = time
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
    
    components = []
    visited_comp = [False] * (n + 1)
    
    def dfs_components(u, comp):
        visited_comp[u] = True
        comp.append(u)
        for v in graph[u]:
            if not visited_comp[v]:
                dfs_components(v, comp)
    
    for i in range(1, n + 1):
        if not visited_comp[i]:
            comp = []
            dfs_components(i, comp)
            components.append(comp)
    
    comp_id = [0] * (n + 1)
    for idx, comp in enumerate(components):
        for node in comp:
            comp_id[node] = idx
    
    comp_graph = [[] for _ in range(len(components))]
    for u in range(1, n + 1):
        for v in graph[u]:
            if comp_id[u] != comp_id[v]:
                comp_graph[comp_id[u]].append(comp_id[v])
    
    leaves = 0
    for i in range(len(components)):
        if len(comp_graph[i]) == 1:
            leaves += 1
    
    if leaves == 0:
        print(0)
    else:
        print((leaves + 1) // 2)

if __name__ == "__main__":
    main()
