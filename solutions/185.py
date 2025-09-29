
def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().splitlines()
    
    n, k = map(int, data[0].split())
    edges = []
    for line in data[1:]:
        if line == '0':
            break
        x, y = map(int, line.split())
        edges.append((x, y))
    
    faster = {i: set() for i in range(1, n+1)}
    slower = {i: set() for i in range(1, n+1)}
    
    for x, y in edges:
        faster[x].add(y)
        slower[y].add(x)
    
    changed = True
    while changed:
        changed = False
        for horse in range(1, n+1):
            for fast_horse in list(faster[horse]):
                for h in faster[fast_horse]:
                    if h not in faster[horse]:
                        faster[horse].add(h)
                        changed = True
            
            for slow_horse in list(slower[horse]):
                for h in slower[slow_horse]:
                    if h not in slower[horse]:
                        slower[horse].add(h)
                        changed = True
    
    if len(faster[k]) == n - 1:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('Yes')
    else:
        with open('OUTPUT.TXT', 'w') as f:
            f.write('No')

if __name__ == '__main__':
    main()
