
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    volumes = list(map(int, data[2:2+n]))
    actions = []
    index = 2 + n
    for i in range(m):
        a = int(data[index]); b = int(data[index+1])
        index += 2
        actions.append((a, b))
    
    parent = list(range(n + 1))
    volume_map = [0] * (n + 1)
    for i in range(1, n + 1):
        volume_map[i] = volumes[i - 1]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    for a, b in actions:
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            continue
            
        if root_a < root_b:
            parent[root_a] = root_b
            volume_map[root_b] += volume_map[root_a]
            volume_map[root_a] = 0
        else:
            parent[root_b] = root_a
            volume_map[root_a] += volume_map[root_b]
            volume_map[root_b] = 0
    
    result = []
    for i in range(1, n + 1):
        if parent[i] == i and volume_map[i] > 0:
            result.append((i, volume_map[i]))
    
    result.sort()
    for num, vol in result:
        print(f"{num} {vol}")

if __name__ == "__main__":
    main()
