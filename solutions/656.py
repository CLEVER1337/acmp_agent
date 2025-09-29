
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    edges = []
    index = 3
    for i in range(m):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        edges.append((a, b, c, i+1))
    
    edges.sort(key=lambda x: x[2])
    
    parent = list(range(n+1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx != ry:
            parent[ry] = rx
            return True
        return False
    
    selected_edges = []
    mst_edges = []
    
    for edge in edges:
        a, b, c, idx = edge
        if find(a) != find(b):
            union(a, b)
            mst_edges.append(edge)
            if len(mst_edges) == n - 1:
                break
    
    if k <= len(mst_edges):
        selected_edges = [edge[3] for edge in mst_edges[:k]]
    else:
        selected_edges = [edge[3] for edge in mst_edges]
        remaining_edges = [edge for edge in edges if edge not in mst_edges]
        remaining_edges.sort(key=lambda x: x[2])
        for i in range(k - len(mst_edges)):
            if i < len(remaining_edges):
                selected_edges.append(remaining_edges[i][3])
    
    for edge_id in selected_edges:
        print(edge_id)

if __name__ == "__main__":
    main()
