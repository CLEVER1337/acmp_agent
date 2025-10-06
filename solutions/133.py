
import heapq

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        costs = list(map(int, f.readline().split()))
        m = int(f.readline().strip())
        
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
    
    INF = float('inf')
    dist = [INF] * n
    dist[0] = 0
    
    pq = []
    heapq.heappush(pq, (0, 0))
    
    while pq:
        current_cost, u = heapq.heappop(pq)
        
        if current_cost > dist[u]:
            continue
            
        for v in graph[u]:
            new_cost = current_cost + costs[u]
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    
    result = dist[n-1] if dist[n-1] != INF else -1
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(result))

if __name__ == "__main__":
    main()
