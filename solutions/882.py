
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, k = map(int, data[0].split())
    buildings = []
    for i in range(1, n + 1):
        parts = data[i].split()
        ai = float(parts[0])
        bi = int(parts[1])
        buildings.append((ai, bi, i))
    
    def compare(x, y):
        a1, b1, idx1 = x
        a2, b2, idx2 = y
        
        term1 = (a1 - 1) * (a2 * k - b2) - b1 * (a2 - 1)
        term2 = (a2 - 1) * (a1 * k - b1) - b2 * (a1 - 1)
        
        if term1 > term2:
            return -1
        elif term1 < term2:
            return 1
        else:
            return 0
    
    from functools import cmp_to_key
    sorted_buildings = sorted(buildings, key=cmp_to_key(compare))
    
    for building in sorted_buildings:
        print(building[2])

if __name__ == "__main__":
    main()
