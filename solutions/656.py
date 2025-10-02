
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    edges = []
    index = 3
    for i in range(m):
        a = int(data[index]); b = int(data[index+1]); c = int(data[index+2])
        index += 3
        edges.append((a, b, c, i+1))
    
    graph = defaultdict(list)
    for i, (a, b, c, idx) in enumerate(edges):
        graph[a].append((b, c, idx))
        graph[b].append((a, c, idx))
    
    parent = list(range(n+1))
    rank = [0] * (n+1)
    
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
    
    sorted_edges = sorted(edges, key=lambda x: x[2])
    mst_edges = []
    total_cost = 0
    
    for a, b, c, idx in sorted_edges:
        if union(a, b):
            mst_edges.append((a, b, c, idx))
            total_cost += c
            if len(mst_edges) == n - 1:
                break
    
    if len(mst_edges) < k:
        print(-1)
        return
    
    mst_edges_sorted_by_index = sorted(mst_edges[:k], key=lambda x: x[3])
    for edge in mst_edges_sorted_by_index:
        print(edge[3])

if __name__ == "__main__":
    main()
