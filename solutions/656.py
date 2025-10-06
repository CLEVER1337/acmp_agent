
import sys
from collections import defaultdict

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
    
    graph = defaultdict(list)
    for i, (a, b, c, idx) in enumerate(edges):
        graph[a].append((b, c, idx))
        graph[b].append((a, c, idx))
    
    parent = list(range(n+1))
    rank = [0] * (n+1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    mst_edges = []
    for a, b, c, idx in sorted_edges:
        if union(a, b):
            mst_edges.append((a, b, c, idx))
    
    if len(mst_edges) < k:
        print("\n".join(map(str, range(1, k+1))))
        return
    
    mst_edges = mst_edges[:k]
    result_indices = [idx for _, _, _, idx in mst_edges]
    
    print("\n".join(map(str, result_indices)))

if __name__ == "__main__":
    main()
