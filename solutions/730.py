
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        c = int(data[index+2])
        index += 3
        edges.append((u, v, c, i+1))
    
    INF = float('inf')
    dist = [INF] * (n+1)
    dist[1] = 0
    prev_edge = [0] * (n+1)
    prev_node = [0] * (n+1)
    
    for i in range(n-1):
        updated = False
        for u, v, c, idx in edges:
            if dist[u] < INF and dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                prev_edge[v] = idx
                prev_node[v] = u
                updated = True
        if not updated:
            break
    
    total_cost = 0
    used_edges = set()
    for city in range(2, n+1):
        if dist[city] < INF:
            total_cost += dist[city]
            cur = city
            while cur != 1:
                used_edges.add(prev_edge[cur])
                cur = prev_node[cur]
    
    k = len(used_edges)
    print(f"{total_cost} {k}")
    print(" ".join(map(str, sorted(used_edges))))

if __name__ == "__main__":
    main()
