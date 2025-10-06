
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print("NO")
        return
        
    n = int(data[0])
    e = int(data[1])
    edges = []
    index = 2
    
    graph = [[] for _ in range(n+1)]
    for i in range(e):
        u = int(data[index]); v = int(data[index+1]); d = float(data[index+2])
        index += 3
        edges.append((u, v, d))
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    dist = [None] * (n+1)
    dist[1] = 0.0
    stack = [1]
    
    while stack:
        u = stack.pop()
        for v, d in graph[u]:
            new_dist = dist[u] + d
            if dist[v] is None:
                dist[v] = new_dist
                stack.append(v)
            else:
                if abs(dist[v] - new_dist) > 1e-9:
                    print("NO")
                    return
                    
    if any(d is None for d in dist[1:n+1]):
        print("NO")
        return
        
    gaps = []
    for i in range(1, n):
        gap = dist[i+1] - dist[i]
        gaps.append(gap)
        
    print("YES")
    for gap in gaps:
        print("{:.3f}".format(gap))

if __name__ == "__main__":
    main()
