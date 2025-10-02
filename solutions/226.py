
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("NO")
        return
        
    n = int(data[0])
    e = int(data[1])
    edges = []
    index = 2
    
    for _ in range(e):
        u = int(data[index])
        v = int(data[index+1])
        w = float(data[index+2])
        index += 3
        edges.append((u-1, v-1, w))
    
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0.0
        
    for u, v, w in edges:
        if u > v:
            u, v = v, u
        dist[u][v] = w
        dist[v][u] = w
        
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                continue
            for u, v, w in edges:
                if abs(dist[u][v] - w) > 1e-9:
                    print("NO")
                    return
                    
    gaps = []
    for i in range(n-1):
        gap = dist[i][i+1]
        if gap == INF:
            print("NO")
            return
        gaps.append(gap)
        
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("NO")
                return
                
    print("YES")
    for gap in gaps:
        print("{:.3f}".format(gap))

if __name__ == "__main__":
    main()
