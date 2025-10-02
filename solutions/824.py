
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    def find(x, parent):
        if parent[x] != x:
            parent[x] = find(parent[x], parent)
        return parent[x]
    
    def union(x, y, parent, rank):
        rx = find(x, parent)
        ry = find(y, parent)
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
    
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for i in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        edges.append((u, v))
        index += 2
    
    total = 0
    for mask in range(1 << m):
        parent = list(range(n))
        rank = [0] * n
        cnt = 0
        for i in range(m):
            if mask & (1 << i):
                u, v = edges[i]
                if union(u, v, parent, rank):
                    cnt += 1
        if cnt == n - 1:
            connected = True
            root = find(0, parent)
            for i in range(1, n):
                if find(i, parent) != root:
                    connected = False
                    break
            if connected:
                total += 1
                
    print(total)

if __name__ == '__main__':
    main()
