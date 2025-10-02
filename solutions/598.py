
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    adj = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        adj.append(row)
        index += n
    
    groups = []
    assigned = [-1] * n
    
    def is_clique(mask):
        nodes = []
        for i in range(n):
            if mask & (1 << i):
                nodes.append(i)
        k = len(nodes)
        for i in range(k):
            for j in range(i+1, k):
                if not adj[nodes[i]][nodes[j]]:
                    return False
        return True
    
    max_size = 0
    best_mask = 0
    for mask in range(1, 1 << n):
        cnt = bin(mask).count('1')
        if cnt > 5:
            continue
        if is_clique(mask):
            if cnt > max_size:
                max_size = cnt
                best_mask = mask
    
    group_id = 1
    remaining = set(range(n))
    
    while remaining:
        best_size = 0
        best_set = None
        
        for mask in range(1, 1 << n):
            cnt = bin(mask).count('1')
            if cnt > 5:
                continue
            nodes = []
            for i in range(n):
                if mask & (1 << i) and i in remaining:
                    nodes.append(i)
            if len(nodes) != cnt:
                continue
            if is_clique(mask):
                if cnt > best_size:
                    best_size = cnt
                    best_set = set(nodes)
        
        if best_set:
            for node in best_set:
                assigned[node] = group_id
                remaining.remove(node)
            group_id += 1
    
    print(group_id - 1)
    print(' '.join(map(str, assigned)))

if __name__ == '__main__':
    main()
