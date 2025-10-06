
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for i in range(m):
        u = int(data[index]); v = int(data[index+1]); index += 2
        edges.append((min(u, v), max(u, v)))
        
    from collections import defaultdict
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * (n + 1)
    comp_count = 0
    comp_sizes = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            comp_count += 1
            stack = [i]
            visited[i] = True
            size = 0
            while stack:
                node = stack.pop()
                size += 1
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            comp_sizes.append(size)
            
    if comp_count != 1:
        print(0)
        return
        
    total_edges = n * (n - 1) // 2
    mod = 10**9 + 7
    
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            dp[j] = (dp[j] + dp[j - 1] * i) % mod
                
    result = 0
    for k in range(n - 1, total_edges + 1):
        result = (result + dp[k]) % mod
        
    print(result % mod)

if __name__ == "__main__":
    main()
