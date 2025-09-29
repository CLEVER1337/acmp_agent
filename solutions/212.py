
def main():
    import sys
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    
    n = int(data[0])
    p = int(data[1])
    
    graph = [[] for _ in range(n+1)]
    index = 2
    for i in range(n-1):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    size = [0] * (n+1)
    
    def dfs(u, parent):
        dp[u][1] = 0
        size[u] = 1
        
        for v in graph[u]:
            if v == parent:
                continue
            dfs(v, u)
            size[u] += size[v]
            
            temp = [float('inf')] * (size[u] + 1)
            for j in range(size[u], 0, -1):
                dp[u][j] += 1
                for k in range(1, min(j, size[v] + 1)):
                    if dp[u][j - k] != float('inf') and dp[v][k] != float('inf'):
                        temp[j] = min(temp[j], dp[u][j - k] + dp[v][k])
            for j in range(1, size[u] + 1):
                if temp[j] != float('inf'):
                    dp[u][j] = min(dp[u][j], temp[j])
    
    dfs(1, -1)
    
    result = float('inf')
    for i in range(1, n+1):
        if dp[i][p] != float('inf'):
            result = min(result, dp[i][p])
    
    print(result)

if __name__ == "__main__":
    main()
