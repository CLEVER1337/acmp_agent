
def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        graph = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            graph.append(row)
    
    INF = 10**9
    dist = [0] * n
    
    for _ in range(n):
        updated = False
        for u in range(n):
            for v in range(n):
                if graph[u][v] != 100000:
                    if dist[v] > dist[u] + graph[u][v]:
                        dist[v] = dist[u] + graph[u][v]
                        updated = True
        if not updated:
            break
    
    has_negative_cycle = False
    for u in range(n):
        for v in range(n):
            if graph[u][v] != 100000:
                if dist[v] > dist[u] + graph[u][v]:
                    has_negative_cycle = True
                    break
        if has_negative_cycle:
            break
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("YES" if has_negative_cycle else "NO")

if __name__ == "__main__":
    main()
