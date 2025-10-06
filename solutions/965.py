
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print("0 0")
        return
        
    n = int(data[0])
    m = int(data[1])
    graph = [0] * (n + 1)
    
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        u -= 1
        v -= 1
        graph[u] |= (1 << v)
        graph[v] |= (1 << u)
    
    total_edges_mask = (1 << n) - 1
    dp = [0] * (1 << n)
    cover_size = [0] * (1 << n)
    
    for mask in range(1 << n):
        cover_size[mask] = 0
        for i in range(n):
            if mask & (1 << i):
                cover_size[mask] |= graph[i]
    
    INF = float('inf')
    min_taken = [INF] * (1 << n)
    ways = [0] * (1 << n)
    
    min_taken[0] = 0
    ways[0] = 1
    
    for mask in range(1 << n):
        if ways[mask] == 0:
            continue
            
        for i in range(n):
            if mask & (1 << i):
                continue
                
            new_mask = mask | (1 << i)
            covered = cover_size[new_mask]
            
            if min_taken[new_mask] > min_taken[mask] + 1:
                min_taken[new_mask] = min_taken[mask] + 1
                ways[new_mask] = ways[mask]
            elif min_taken[new_mask] == min_taken[mask] + 1:
                ways[new_mask] += ways[mask]
    
    best_mask = None
    min_count = INF
    total_ways = 0
    
    for mask in range(1 << n):
        if cover_size[mask] == total_edges_mask:
            if min_taken[mask] < min_count:
                min_count = min_taken[mask]
                total_ways = ways[mask]
                best_mask = mask
            elif min_taken[mask] == min_count:
                total_ways += ways[mask]
    
    stations = []
    for i in range(n):
        if best_mask & (1 << i):
            stations.append(i + 1)
    
    print(f"{min_count} {total_ways}")
    print(" ".join(map(str, sorted(stations))))

if __name__ == "__main__":
    main()
