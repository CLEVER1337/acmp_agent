
import sys
sys.setrecursionlimit(1000000)

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    
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
    articulation_points = set()
    
    def dfs(u):
        nonlocal time
        children = 0
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1
        
        for v in graph[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                
                if parent[u] == 0 and children > 1:
                    articulation_points.add(u)
                elif parent[u] != 0 and low[v] >= disc[u]:
                    articulation_points.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    visited = [False] * (n + 1)
    components = []
    
    def dfs_component(u, comp):
        visited[u] = True
        comp.append(u)
        for v in graph[u]:
            if not visited[v] and v not in articulation_points:
                dfs_component(v, comp)
    
    for i in range(1, n + 1):
        if not visited[i] and i not in articulation_points:
            comp = []
            dfs_component(i, comp)
            components.append(comp)
    
    if n == 1:
        print(0)
        return
        
    if m == 0:
        print(0)
        return
        
    if not articulation_points:
        if len(components) == 1:
            print(1)
        else:
            print(0)
        return
    
    count = 0
    for comp in components:
        connections = 0
        for node in comp:
            for neighbor in graph[node]:
                if neighbor in articulation_points:
                    connections += 1
        if connections == 1:
            count += 1
            
    isolated_aps = 0
    for ap in articulation_points:
        has_connection = False
        for neighbor in graph[ap]:
            if neighbor not in articulation_points:
                has_connection = True
                break
        if not has_connection:
            isolated_aps += 1
            
    result = (count + 1) // 2 + isolated_aps
    print(result)

if __name__ == "__main__":
    main()
