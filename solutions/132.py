
import heapq

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    s = int(data[1]) - 1
    f = int(data[2]) - 1
    
    graph = []
    index = 3
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        graph.append(row)
    
    dist = [float('inf')] * n
    dist[s] = 0
    heap = [(0, s)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        if current_dist != dist[u]:
            continue
            
        if u == f:
            break
            
        for v in range(n):
            weight = graph[u][v]
            if weight != -1:
                new_dist = current_dist + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))
    
    result = dist[f] if dist[f] != float('inf') else -1
    with open('OUTPUT.TXT', 'w') as f_out:
        f_out.write(str(result))

if __name__ == "__main__":
    main()
