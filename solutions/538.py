
import sys
import math

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = float(data[index])
        y = float(data[index+1])
        index += 2
        points.append((x, y))
    
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist = math.sqrt(dx*dx + dy*dy)
            edges.append((dist, i, j))
    
    edges.sort(key=lambda x: x[0])
    
    parent = list(range(n))
    rank = [0] * n
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return False
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
        return True
    
    graph = [[] for _ in range(n)]
    mst_edges = []
    for dist, u, v in edges:
        if union(u, v):
            graph[u].append((v, dist))
            graph[v].append((u, dist))
            mst_edges.append((u, v, dist))
    
    max_edge = 0
    for u, v, dist in mst_edges:
        if dist > max_edge:
            max_edge = dist
    
    low = 0.0
    high = max_edge * 2
    
    def is_bipartite(limit):
        color = [-1] * n
        for i in range(n):
            if color[i] == -1:
                stack = [i]
                color[i] = 0
                while stack:
                    u = stack.pop()
                    for v, dist in graph[u]:
                        if dist > limit:
                            if color[v] == -1:
                                color[v] = 1 - color[u]
                                stack.append(v)
                            elif color[v] == color[u]:
                                return False
        return True
    
    for _ in range(100):
        mid = (low + high) / 2.0
        if is_bipartite(mid):
            low = mid
        else:
            high = mid
    
    power = low / 2.0
    
    color = [-1] * n
    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            while stack:
                u = stack.pop()
                for v, dist in graph[u]:
                    if dist > low:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            stack.append(v)
    
    result = []
    for i in range(n):
        result.append(str(color[i] + 1))
    
    print("{:.10f}".format(power))
    print(" ".join(result))

if __name__ == "__main__":
    main()
