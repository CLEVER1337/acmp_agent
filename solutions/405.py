
import sys
from sys import stdin
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    if not data:
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
    
    disc = [0] * (n + 1)
    low = [0] * (n + 1)
    parent = [0] * (n + 1)
    time = 0
    is_articulation = [False] * (n + 1)
    size = [0] * (n + 1)
    
    def dfs(u, p):
        nonlocal time
        disc[u] = time + 1
        low[u] = time + 1
        time += 1
        parent[u] = p
        size[u] = 1
        children = 0
        
        for v in graph[u]:
            if v == p:
                continue
            if disc[v] == 0:
                children += 1
                dfs(v, u)
                size[u] += size[v]
                low[u] = min(low[u], low[v])
                
                if p != 0 and low[v] >= disc[u]:
                    is_articulation[u] = True
            else:
                low[u] = min(low[u], disc[v])
                
        if p == 0 and children > 1:
            is_articulation[u] = True
    
    dfs(1, 0)
    
    total = n
    result = [0] * (n + 1)
    
    for u in range(1, n + 1):
        if not is_articulation[u]:
            continue
            
        sum_sizes = 0
        count = 0
        for v in graph[u]:
            if parent[v] == u:
                sum_sizes += size[v]
                count += 1
        
        if parent[u] != 0:
            remaining = total - sum_sizes - 1
            result[u] += remaining * sum_sizes
        
        for v in graph[u]:
            if parent[v] == u:
                remaining = total - size[v] - 1
                result[u] += size[v] * remaining
        
        result[u] //= 2
    
    output = []
    for i in range(1, n + 1):
        output.append(str(result[i]))
    
    sys.stdout.write(" ".join(output))

if __name__ == "__main__":
    main()
