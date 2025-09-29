
import heapq

def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    d = int(data[1])
    v = int(data[2])
    r = int(data[3])
    
    graph = [[] for _ in range(n + 1)]
    index = 4
    
    for _ in range(r):
        from_village = int(data[index])
        departure_time = int(data[index + 1])
        to_village = int(data[index + 2])
        arrival_time = int(data[index + 3])
        index += 4
        graph[from_village].append((to_village, departure_time, arrival_time))
    
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[d] = 0
    
    heap = []
    heapq.heappush(heap, (0, d))
    
    while heap:
        current_time, current_village = heapq.heappop(heap)
        
        if current_village == v:
            print(current_time)
            return
            
        if current_time > dist[current_village]:
            continue
            
        for next_village, dep_time, arr_time in graph[current_village]:
            if dep_time >= current_time:
                if arr_time < dist[next_village]:
                    dist[next_village] = arr_time
                    heapq.heappush(heap, (arr_time, next_village))
    
    print(-1 if dist[v] == INF else dist[v])

if __name__ == "__main__":
    main()
