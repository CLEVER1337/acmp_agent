
import sys

def main():
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
        w = int(data[index+2])
        index += 3
        edges.append((u, v, w))
    
    INF = 30000
    dist = [INF] * (n + 1)
    dist[1] = 0
    
    for i in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] < INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    
    for i in range(1, n + 1):
        if dist[i] >= INF:
            print(30000, end=' ')
        else:
            print(dist[i], end=' ')

if __name__ == "__main__":
    main()
