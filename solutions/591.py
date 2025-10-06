
import sys

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
    parent_copy = parent[:]
    rank_copy = rank[:]
    
    for u, v, idx in good_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, idx, 1))
    
    bad_count = 0
    for u, v, idx in bad_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, idx, 2))
            bad_count += 1
    
    if len(mst_edges) != n - 1:
        print(-1)
        return
    
    if bad_count % 2 == 0:
        result = [edge[2] for edge in mst_edges]
        result.sort()
        for res in result:
            print(res)
        return
    
    parent = parent_copy
    rank = rank_copy
    
    mst_edges2 = []
    for u, v, idx in bad_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges2.append((u, v, idx, 2))
    
    for u, v, idx in good_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges2.append((u, v, idx, 1))
    
    if len(mst_edges2) != n - 1:
        print(-1)
        return
    
    bad_count2 = sum(1 for edge in mst_edges2 if edge[3] == 2)
    if bad_count2 % 2 == 0:
        result = [edge[2] for edge in mst_edges2]
        result.sort()
        for res in result:
            print(res)
        return
    
    graph = [[] for _ in range(n)]
    edge_info = {}
    for i, (u, v, t, idx) in enumerate(edges):
        graph[u].append((v, i))
        graph[v].append((u, i))
        edge_info[i] = (u, v, t)
    
    parent = list(range(n))
    rank = [0] * n
    
    mst_edges3 = []
    for u, v, idx in good_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges3.append((u, v, idx, 1))
    
    for u, v, idx in bad_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges3.append((u, v, idx, 2))
    
    if len(mst_edges3) != n - 1:
        print(-1)
        return
    
    bad_count3 = sum(1 for edge in mst_edges3 if edge[3] == 2)
    if bad_count3 % 2 == 0:
        result = [edge[2] for edge in mst_edges3]
        result.sort()
        for res in result:
            print(res)
        return
    
    mst_set = set(edge[2] for edge in mst_edges3)
    non_mst_edges = [edge for edge in edges if edge[3] not in mst_set]
    
    for non_edge in non_mst_edges:
        u, v, t, idx = non_edge
        if t == 2:
            continue
            
        parent_temp = parent[:]
        rank_temp = rank[:]
        
        def find_temp(x):
            if parent_temp[x] != x:
                parent_temp[x] = find_temp(parent_temp[x])
            return parent_temp[x]
        
        def union_temp(x, y):
            rx = find_temp(x)
            ry = find_temp(y)
            if rx == ry:
                return False
            if rank_temp[rx] < rank_temp[ry]:
                parent_temp[rx] = ry
            elif rank_temp[rx] > rank_temp[ry]:
                parent_temp[ry] = rx
            else:
                parent_temp[ry] = rx
                rank_temp[rx] += 1
            return True
        
        union_temp(u, v)
        new_mst = []
        bad_count_new = 0
        
        for edge in mst_edges3:
            u_mst, v_mst, idx_mst, t_mst = edge
            if find_temp(u_mst) != find_temp(v_mst):
                union_temp(u_mst, v_mst)
                new_mst.append(idx_mst)
                if t_mst == 2:
                    bad_count_new += 1
        
        if len(new_mst) == n - 1 and bad_count_new % 2 == 0:
            new_mst.sort()
            for res in new_mst:
                print(res)
            return
    
    print(-1)

if __name__ == "__main__":
    main()
