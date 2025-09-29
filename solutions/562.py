
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    index = 2
    
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    
    for i in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        index += 2
        adj[u].append(v)
        rev_adj[v].append(u)
    
    INF = 10**9
    dist = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        for neighbor in adj[i]:
            dist[i][neighbor] = 0
    
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                for neighbor in rev_adj[j]:
                    dist[i][j] = min(dist[i][j], dist[i][neighbor] + 1)
    
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
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
