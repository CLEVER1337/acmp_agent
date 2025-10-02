
def main():
    import sys
    sys.setrecursionlimit(10000)
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
    size = [0] * (n+1)
    
    def dfs(u, par):
        parent[u] = par
        size[u] = 1
        for v in graph[u]:
            if v != par:
                dfs(v, u)
                size[u] += size[v]
    
    dfs(1, 0)
    
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = len(graph[i])
        if parent[i] != 0:
            dp[i][1] -= 1
    
    for u in range(1, n+1):
        for v in graph[u]:
            if v == parent[u]:
                continue
            new_dp = [float('inf')] * (n+1)
            for j in range(1, n+1):
                if dp[u][j] == float('inf'):
                    continue
                new_dp[j] = min(new_dp[j], dp[u][j])
                for k in range(1, size[v]+1):
                    if j+k > n:
                        break
                    if dp[v][k] != float('inf'):
                        new_dp[j+k] = min(new_dp[j+k], dp[u][j] + dp[v][k] - 1)
            dp[u] = new_dp
    
    result = float('inf')
    for i in range(1, n+1):
        if dp[i][p] != float('inf'):
            if i == 1:
                result = min(result, dp[i][p])
            else:
                result = min(result, dp[i][p] + 1)
    
    print(result)

if __name__ == '__main__':
    main()
