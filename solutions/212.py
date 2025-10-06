
import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    p = int(data[1])
    edges = []
    index = 2
    graph = [[] for _ in range(n+1)]
    
    for i in range(n-1):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    parent = [0] * (n+1)
    children = [[] for _ in range(n+1)]
    size = [0] * (n+1)
    
    stack = [1]
    parent[1] = 0
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                children[u].append(v)
                stack.append(v)
    
    for u in reversed(order):
        size[u] = 1
        for v in children[u]:
            size[u] += size[v]
    
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = len(children[i])
    
    for u in reversed(order):
        for v in children[u]:
            new_dp = [float('inf')] * (n+1)
            for j in range(size[u], 0, -1):
                for k in range(1, min(j, size[v]+1)):
                    if dp[u][j] != float('inf') and dp[v][k] != float('inf'):
                        new_dp[j-k] = min(new_dp[j-k], dp[u][j] + dp[v][k] - 1)
                if dp[u][j] != float('inf'):
                    new_dp[j] = min(new_dp[j], dp[u][j])
            for j in range(n+1):
                if new_dp[j] != float('inf'):
                    dp[u][j] = new_dp[j]
    
    result = float('inf')
    for i in range(1, n+1):
        if size[i] >= p:
            if i == 1:
                result = min(result, dp[i][p])
            else:
                result = min(result, dp[i][p] + 1)
    
    print(result)

if __name__ == "__main__":
    main()
