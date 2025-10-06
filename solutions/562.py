
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    graph = [[0] * n for _ in range(n)]
    
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        index += 2
        graph[u][v] = 1
        
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                dist[i][j] = 0
            elif i != j:
                dist[i][j] = 1
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    ans = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] > ans:
                ans = dist[i][j]
                
    print(ans)

if __name__ == "__main__":
    main()
