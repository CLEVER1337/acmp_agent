
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
        
    n, m, k = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())
    
    from itertools import permutations
    
    boys = list(range(n))
    girls = list(range(m))
    
    count = 0
    for perm in permutations(girls, k):
        used_boys = set()
        used_girls = set(perm)
        valid = True
        for boy_idx, girl_idx in enumerate(perm):
            if grid[boy_idx][girl_idx] != 'Y':
                valid = False
                break
            used_boys.add(boy_idx)
        
        if not valid:
            continue
            
        if len(used_boys) != k or len(used_girls) != k:
            continue
            
        count += 1
    
    print(count)

if __name__ == "__main__":
    main()
