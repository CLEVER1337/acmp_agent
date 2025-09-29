
import heapq

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
        if not data:
            return
            
        idx = 0
        N = int(data[idx]); M = int(data[idx+1]); K = int(data[idx+2]); idx += 3
        capital = int(data[idx]); idx += 1
        
        cities = []
        for i in range(K):
            cities.append(int(data[idx])); idx += 1
            
        graph = [[] for _ in range(N+1)]
        for i in range(M):
            u = int(data[idx]); v = int(data[idx+1]); t = int(data[idx+2]); idx += 3
            graph[u].append((v, t))
            graph[v].append((u, t))
            
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[capital] = 0
    heap = [(0, capital)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, t in graph[u]:
            new_dist = d + t
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
                
    results = []
    for city in cities:
        results.append((city, dist[city]))
        
    results.sort(key=lambda x: (x[1], x[0]))
    
    with open('OUTPUT.TXT', 'w') as f:
        for city, time in results:
            f.write(f"{city} {time}\n")

if __name__ == "__main__":
    main()
