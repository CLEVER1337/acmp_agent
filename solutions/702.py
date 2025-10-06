
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    rects = []
    index = 1
    for i in range(n):
        x1 = int(data[index])
        y1 = int(data[index+1])
        x2 = int(data[index+2])
        y2 = int(data[index+3])
        index += 4
        rects.append((x1, y1, x2, y2))
    
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
            return
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        elif rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
    
    for i in range(n):
        for j in range(i+1, n):
            x1_i, y1_i, x2_i, y2_i = rects[i]
            x1_j, y1_j, x2_j, y2_j = rects[j]
            
            if (x2_i < x1_j or x2_j < x1_i or y2_i < y1_j or y2_j < y1_i):
                continue
            
            if (x2_i == x1_j or x2_j == x1_i) and (y2_i == y1_j or y2_j == y1_i):
                continue
            
            union(i, j)
    
    groups = {}
    for i in range(n):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    
    max_area = 0
    for group in groups.values():
        if not group:
            continue
            
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        
        for idx in group:
            x1, y1, x2, y2 = rects[idx]
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
        
        area = (max_x - min_x) * (max_y - min_y)
        if area > max_area:
            max_area = area
    
    print(max_area)

if __name__ == "__main__":
    main()
