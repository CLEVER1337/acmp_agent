
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    prices = list(map(int, data[1:1+n]))
    m = int(data[1+n])
    
    graph = [[] for _ in range(n)]
    index = 1 + n + 1
    for i in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    
    INF = float('inf')
    cost = [INF] * n
    cost[0] = prices[0]
    
    visited = [False] * n
    
    for _ in range(n):
        min_cost = INF
        u = -1
        for i in range(n):
            if not visited[i] and cost[i] < min_cost:
                min_cost = cost[i]
                u = i
                
        if u == -1:
            break
            
        visited[u] = True
        
        for v in graph[u]:
            if not visited[v]:
                new_cost = cost[u] + prices[v]
                if new_cost < cost[v]:
                    cost[v] = new_cost
    
    result = cost[n-1]
    if result == INF:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()
