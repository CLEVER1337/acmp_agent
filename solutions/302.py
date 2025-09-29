
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        cities = []
        for _ in range(n):
            x, y = map(float, f.readline().split())
            cities.append((x, y))
    
    if n <= 1:
        print("0.00")
        return
    
    INF = float('inf')
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dx = cities[i][0] - cities[j][0]
            dy = cities[i][1] - cities[j][1]
            d = math.sqrt(dx*dx + dy*dy)
            dist[i][j] = d
            dist[j][i] = d
    
    min_edge = [INF] * n
    visited = [False] * n
    min_edge[0] = 0.0
    
    max_edge = 0.0
    for _ in range(n):
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        visited[u] = True
        max_edge = max(max_edge, min_edge[u])
        
        for v in range(n):
            if not visited[v] and dist[u][v] < min_edge[v]:
                min_edge[v] = dist[u][v]
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.2f}".format(max_edge))

if __name__ == "__main__":
    main()
