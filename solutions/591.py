
def main():
    import sys
    sys.setrecursionlimit(300000)
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
    
    selected_edges = []
    mst_edges = []
    
    parent_mst = list(range(n))
    rank_mst = [0] * n
    
    for u, v, idx in good_edges:
        if union(u, v):
            mst_edges.append((u, v, idx, 1))
    
    bad_count_in_mst = 0
    for u, v, idx in bad_edges:
        if union(u, v):
            mst_edges.append((u, v, idx, 2))
            bad_count_in_mst += 1
    
    if len(mst_edges) != n - 1:
        print(-1)
        return
    
    if bad_count_in_mst % 2 == 0:
        result = [edge[2] for edge in mst_edges]
        for idx in sorted(result):
            print(idx)
        return
    
    parent_copy = parent_mst[:]
    rank_copy = rank_mst[:]
    
    def find_copy(x):
        if parent_copy[x] != x:
            parent_copy[x] = find_copy(parent_copy[x])
        return parent_copy[x]
    
    def union_copy(x, y):
        rx = find_copy(x)
        ry = find_copy(y)
        if rx == ry:
            return False
        if rank_copy[rx] < rank_copy[ry]:
            parent_copy[rx] = ry
        elif rank_copy[rx] > rank_copy[ry]:
            parent_copy[ry] = rx
        else:
            parent_copy[ry] = rx
            rank_copy[rx] += 1
        return True
    
    for u, v, idx, t in mst_edges:
        if t == 1:
            union_copy(u, v)
    
    found_replacement = False
    replacement_edge = None
    removed_edge = None
    
    for u, v, idx in bad_edges:
        if find_copy(u) != find_copy(v):
            replacement_edge = idx
            break
    
    if replacement_edge is None:
        print(-1)
        return
    
    for u, v, idx, t in mst_edges:
        if t == 2:
            removed_edge = idx
            break
    
    if removed_edge is None:
        print(-1)
        return
    
    result_set = set()
    for u, v, idx, t in mst_edges:
        if idx != removed_edge:
            result_set.add(idx)
    result_set.add(replacement_edge)
    
    if len(result_set) != n - 1:
        print(-1)
        return
    
    bad_count = 0
    for edge in result_set:
        for u, v, t, idx in edges:
            if idx == edge and t == 2:
                bad_count += 1
                break
    
    if bad_count % 2 != 0:
        print(-1)
        return
    
    for idx in sorted(result_set):
        print(idx)

if __name__ == "__main__":
    main()
