
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    graph = [[] for _ in range(n+1)]
    index = 2
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n+1):
        graph[i].sort()
    
    parent = [0] * (n+1)
    depth = [0] * (n+1)
    order = []
    stack = [1]
    parent[1] = 0
    depth[1] = 0
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v in reversed(graph[u]):
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)
    
    back_edges = [[] for _ in range(n+1)]
    for u in range(1, n+1):
        for v in graph[u]:
            if v != parent[u] and parent[v] != u:
                back_edges[u].append(v)
    
    low = [0] * (n+1)
    time = 0
    disc = [-1] * (n+1)
    
    def dfs(u, p):
        nonlocal time
        disc[u] = time
        low[u] = time
        time += 1
        for v in graph[u]:
            if v == p:
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
            else:
                low[u] = min(low[u], disc[v])
    
    dfs(1, 0)
    
    is_articulation = [False] * (n+1)
    children_count = [0] * (n+1)
    for v in range(2, n+1):
        if parent[v] == 1:
            children_count[1] += 1
        if low[v] >= disc[parent[v]] and parent[v] != 1:
            is_articulation[parent[v]] = True
    
    if children_count[1] > 1:
        is_articulation[1] = True
    
    tree_edges = []
    for i in range(2, n+1):
        tree_edges.append((parent[i], i))
    
    comp_id = [0] * (n+1)
    comp_count = 0
    visited = [False] * (n+1)
    
    for u in range(1, n+1):
        if not visited[u]:
            comp_count += 1
            queue = deque([u])
            visited[u] = True
            comp_id[u] = comp_count
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        comp_id[neighbor] = comp_count
                        queue.append(neighbor)
    
    if comp_count > 1:
        print("1 " + " ".join(str(i) for i in range(2, n+1)))
        print("1 " + " ".join(str(i) for i in range(n, 1, -1)))
        return
    
    dfs_order = order.copy()
    
    reverse_dfs = [1]
    stack = [1]
    visited = [False] * (n+1)
    visited[1] = True
    
    while stack:
        u = stack.pop()
        for v in reversed(graph[u]):
            if not visited[v]:
                visited[v] = True
                stack.append(v)
                reverse_dfs.append(v)
    
    plan1 = [1]
    visited = [False] * (n+1)
    visited[1] = True
    stack = [1]
    
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                plan1.append(v)
                stack.append(v)
    
    plan2 = [1]
    visited = [False] * (n+1)
    visited[1] = True
    stack = [1]
    
    while stack:
        u = stack.pop()
        for v in reversed(graph[u]):
            if not visited[v]:
                visited[v] = True
                plan2.append(v)
                stack.append(v)
    
    print(" ".join(map(str, plan1)))
    print(" ".join(map(str, plan2)))

if __name__ == "__main__":
    main()
