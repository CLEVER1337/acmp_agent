
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    for i in range(m):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        edges.append((c, a-1, b-1))
    
    edges.sort()
    
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
    
    total_weight = 0
    count = 0
    
    for c, a, b in edges:
        if union(a, b):
            total_weight += c
            count += 1
            if count == n - 1:
                break
    
    print(total_weight)

if __name__ == "__main__":
    main()
