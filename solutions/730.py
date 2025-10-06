
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
    
    INF = 10**9
    dist = [INF] * (n+1)
    dist[1] = 0
    parent_edge = [0] * (n+1)
    used_edges = set()
    
    for _ in range(n-1):
        updated = False
        for u, v, c, idx in edges:
            if dist[u] < INF and dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                parent_edge[v] = idx
                updated = True
        if not updated:
            break
    
    total_cost = 0
    for i in range(2, n+1):
        if dist[i] < INF:
            total_cost += dist[i]
    
    selected_edges = set()
    for i in range(2, n+1):
        if dist[i] < INF:
            current = i
            while current != 1:
                edge_id = parent_edge[current]
                selected_edges.add(edge_id)
                for u, v, c, idx in edges:
                    if idx == edge_id:
                        current = u
                        break
    
    k = len(selected_edges)
    print(total_cost, k)
    print(' '.join(map(str, sorted(selected_edges))))

if __name__ == "__main__":
    main()
