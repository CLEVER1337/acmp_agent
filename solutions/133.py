
import heapq

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    costs = list(map(int, data[1:1+n]))
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
    dist = [INF] * n
    dist[0] = costs[0]
    
    pq = [(costs[0], 0)]
    
    while pq:
        current_cost, u = heapq.heappop(pq)
        
        if current_cost > dist[u]:
            continue
            
        for v in graph[u]:
            new_cost = current_cost + costs[v]
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    
    result = dist[n-1] if dist[n-1] != INF else -1
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()
