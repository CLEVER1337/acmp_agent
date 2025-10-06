
import math

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = float(data[index])
        y = float(data[index+1])
        index += 2
        points.append((x, y))
    
    if n <= 1:
        print("0.00")
        return
        
    INF = 10**18
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            d = math.sqrt(dx*dx + dy*dy)
            dist[i][j] = d
            dist[j][i] = d
    
    selected = [False] * n
    min_edge = [INF] * n
    min_edge[0] = 0
    max_edge_in_mst = 0
    
    for i in range(n):
        v = -1
        for j in range(n):
            if not selected[j] and (v == -1 or min_edge[j] < min_edge[v]):
                v = j
                
        selected[v] = True
        if min_edge[v] > max_edge_in_mst:
            max_edge_in_mst = min_edge[v]
            
        for to in range(n):
            if not selected[to] and dist[v][to] < min_edge[to]:
                min_edge[to] = dist[v][to]
                
    print("{:.2f}".format(max_edge_in_mst))

if __name__ == "__main__":
    main()
