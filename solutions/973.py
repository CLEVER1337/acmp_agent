
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0]); m = int(data[1])
    edges = []
    graph = [[] for _ in range(n+1)]
    
    for i in range(m):
        u = int(data[2 + 3*i])
        v = int(data[3 + 3*i])
        w = int(data[4 + 3*i])
        edges.append((u, v, w))
        graph[u].append((v, w, i+1))
        graph[v].append((u, w, i+1))
    
    def dijkstra(start):
        dist = [10**18] * (n+1)
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w, idx in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))
        return dist
    
    dist1 = dijkstra(1)
    distn = dijkstra(n)
    total_time = dist1[n]
    
    if total_time == 10**18:
        print(0)
        return
        
    critical_edges = []
    
    for i, (u, v, w) in enumerate(edges):
        if dist1[u] + w + distn[v] == total_time or dist1[v] + w + distn[u] == total_time:
            critical_edges.append(i+1)
            
    print(len(critical_edges))
    if critical_edges:
        print(" ".join(map(str, critical_edges)))
    else:
        print()

if __name__ == "__main__":
    main()
