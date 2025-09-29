
def main():
    with open("INPUT.TXT", "r") as f:
        n = int(f.readline().strip())
        graph = []
        for i in range(n):
            row = list(map(int, f.readline().split()))
            graph.append(row)
    
    INF = 10**9
    dist = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != -1:
                dist[i][j] = graph[i][j]
            if i == j:
                dist[i][j] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < INF and dist[k][j] < INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    max_dist = -1
    for i in range(n):
        for j in range(n):
            if dist[i][j] < INF and dist[i][j] > max_dist:
                max_dist = dist[i][j]
    
    with open("OUTPUT.TXT", "w") as f:
        f.write(str(max_dist))

if __name__ == "__main__":
    main()
