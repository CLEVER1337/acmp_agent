
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        print("NO")
        return
        
    n = int(data[0])
    e = int(data[1])
    index = 2
    
    edges = []
    for i in range(e):
        u = int(data[index]); v = int(data[index+1]); w = float(data[index+2])
        index += 3
        edges.append((u, v, w))
    
    INF = 10**18
    dist = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0.0
        
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    for u, v, w in edges:
        if abs(dist[u][v] - w) > 1e-9:
            print("NO")
            return
            
    gaps = [0.0] * (n+1)
    gaps[1] = 0.0
    for i in range(2, n+1):
        gaps[i] = dist[1][i]
    
    segments = []
    for i in range(1, n):
        seg_len = gaps[i+1] - gaps[i]
        if seg_len < -1e-9:
            print("NO")
            return
        segments.append(seg_len)
    
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if abs(dist[i][j] - (gaps[j] - gaps[i])) > 1e-9:
                print("NO")
                return
                
    print("YES")
    for seg in segments:
        print("{:.3f}".format(seg))

if __name__ == "__main__":
    main()
