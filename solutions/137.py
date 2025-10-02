
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    graph = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        graph.append(row)
    
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
            if i == j:
                dist[i][j] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    
    negative_cycle = [[False] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        negative_cycle[i][j] = True
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if negative_cycle[i][k] and dist[k][j] != float('inf'):
                    negative_cycle[i][j] = True
                if dist[i][k] != float('inf') and negative_cycle[k][j]:
                    negative_cycle[i][j] = True
    
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                result[i][j] = 0
            elif negative_cycle[i][j]:
                result[i][j] = 2
            else:
                result[i][j] = 1
    
    for i in range(n):
        print(' '.join(map(str, result[i])))

if __name__ == '__main__':
    main()
