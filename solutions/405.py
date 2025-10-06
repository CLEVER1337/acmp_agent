
import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    graph = [[] for _ in range(n+1)]
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    disc = [0] * (n+1)
    low = [0] * (n+1)
    parent = [0] * (n+1)
    time = 0
    is_articulation = [False] * (n+1)
    size = [1] * (n+1)
    result = [0] * (n+1)
    
    stack = []
    visited = [False] * (n+1)
    order = []
    
    def dfs(u):
        nonlocal time
        disc[u] = time + 1
        low[u] = time + 1
        time += 1
        stack.append(u)
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] >= disc[u]:
                    comp = []
                    while stack and stack[-1] != u:
                        comp.append(stack.pop())
                    comp_size = len(comp) + 1
                    for node in comp:
                        size[u] += size[node]
                    result[u] += size[u] * (n - size[u])
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    
    output = []
    for i in range(1, n+1):
        output.append(str(result[i]))
    
    sys.stdout.write(" ".join(output))

if __name__ == "__main__":
    main()
