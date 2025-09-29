
import sys
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    
    for i in range(m):
        u = int(data[index])
        v = int(data[index+1])
        t = int(data[index+2])
        index += 3
        edges.append((u-1, v-1, t, i+1))
    
    parent = list(range(n))
    rank = [0] * n
    
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
    
    good_edges = []
    bad_edges = []
    
    for u, v, t, idx in edges:
        if t == 1:
            good_edges.append((u, v, idx))
        else:
            bad_edges.append((u, v, idx))
    
    mst_edges = []
    parent_mst = list(range(n))
    rank_mst = [0] * n
    
    def find_mst(x):
        if parent_mst[x] != x:
            parent_mst[x] = find_mst(parent_mst[x])
        return parent_mst[x]
    
    def union_mst(x, y):
        rx = find_mst(x)
        ry = find_mst(y)
        if rx == ry:
            return False
        if rank_mst[rx] < rank_mst[ry]:
            parent_mst[rx] = ry
        elif rank_mst[rx] > rank_mst[ry]:
            parent_mst[ry] = rx
        else:
            parent_mst[ry] = rx
            rank_mst[rx] += 1
        return True
    
    for u, v, idx in good_edges:
        if union_mst(u, v):
            mst_edges.append(idx)
    
    bad_count = 0
    for u, v, idx in bad_edges:
        if union_mst(u, v):
            mst_edges.append(idx)
            bad_count += 1
    
    if len(mst_edges) != n - 1:
        print(-1)
        return
    
    if bad_count % 2 == 0:
        for edge in sorted(mst_edges):
            print(edge)
        return
    
    parent_dsu = list(range(n))
    rank_dsu = [0] * n
    
    def find_dsu(x):
        if parent_dsu[x] != x:
            parent_dsu[x] = find_dsu(parent_dsu[x])
        return parent_dsu[x]
    
    def union_dsu(x, y):
        rx = find_dsu(x)
        ry = find_dsu(y)
        if rx == ry:
            return False
        if rank_dsu[rx] < rank_dsu[ry]:
            parent_dsu[rx] = ry
        elif rank_dsu[rx] > rank_dsu[ry]:
            parent_dsu[ry] = rx
        else:
            parent_dsu[ry] = rx
            rank_dsu[rx] += 1
        return True
    
    for idx in mst_edges:
        for u, v, t, edge_idx in edges:
            if edge_idx == idx:
                if t == 1:
                    union_dsu(u, v)
                break
    
    candidate = -1
    candidate_idx = -1
    
    for u, v, t, idx in edges:
        if t == 2 and find_dsu(u) != find_dsu(v):
            candidate = idx
            candidate_idx = idx
            break
    
    if candidate == -1:
        print(-1)
        return
    
    new_mst = []
    parent_new = list(range(n))
    rank_new = [0] * n
    
    def find_new(x):
        if parent_new[x] != x:
            parent_new[x] = find_new(parent_new[x])
        return parent_new[x]
    
    def union_new(x, y):
        rx = find_new(x)
        ry = find_new(y)
        if rx == ry:
            return False
        if rank_new[rx] < rank_new[ry]:
            parent_new[rx] = ry
        elif rank_new[rx] > rank_new[ry]:
            parent_new[ry] = rx
        else:
            parent_new[ry] = rx
            rank_new[rx] += 1
        return True
    
    union_new(edges[candidate_idx-1][0], edges[candidate_idx-1][1])
    new_mst.append(candidate_idx)
    new_bad_count = 1
    
    for u, v, idx in good_edges:
        if union_new(u, v):
            new_mst.append(idx)
    
    for u, v, idx in bad_edges:
        if idx == candidate_idx:
            continue
        if union_new(u, v):
            new_mst.append(idx)
            new_bad_count += 1
    
    if len(new_mst) != n - 1 or new_bad_count % 2 != 0:
        print(-1)
        return
    
    for edge in sorted(new_mst):
        print(edge)

if __name__ == "__main__":
    main()
