
import sys
from collections import defaultdict

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
    articulation_points = [False] * (n + 1)
    sizes = [0] * (n + 1)
    
    def dfs(u, p):
        nonlocal time
        time += 1
        disc[u] = time
        low[u] = time
        sizes[u] = 1
        children = 0
        total = 0
        
        for v in graph[u]:
            if v == p:
                continue
            if disc[v] == 0:
                children += 1
                parent[v] = u
                dfs(v, u)
                sizes[u] += sizes[v]
                low[u] = min(low[u], low[v])
                
                if (p == -1 and children > 1) or (p != -1 and low[v] >= disc[u]):
                    articulation_points[u] = True
                    total += sizes[v]
            else:
                low[u] = min(low[u], disc[v])
        
        return total
    
    dfs(1, -1)
    
    result = [0] * (n + 1)
    total_nodes = n
    
    for u in range(1, n + 1):
        if articulation_points[u]:
            sum_sizes = 0
            product_sum = 0
            for v in graph[u]:
                if parent[v] == u:
                    sum_sizes += sizes[v]
                    product_sum += sizes[v] * sizes[v]
            remaining = total_nodes - 1 - sum_sizes
            pairs = (sum_sizes * sum_sizes - product_sum) // 2
            pairs += sum_sizes * remaining
            pairs += remaining * (remaining - 1) // 2
            result[u] = pairs
        else:
            result[u] = (total_nodes - 1) * (total_nodes - 2) // 2
    
    output = []
    for i in range(1, n + 1):
        output.append(str(result[i]))
    
    sys.stdout.write(" ".join(output))

if __name__ == "__main__":
    main()
