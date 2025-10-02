
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    first_line = data[0].split()
    n = int(first_line[0])
    k = float(first_line[1])
    
    buildings = []
    for i in range(1, n + 1):
        parts = data[i].split()
        a = float(parts[0])
        b = float(parts[1])
        buildings.append((a, b, i))
    
    def compare(x, y):
        a1, b1, idx1 = x
        a2, b2, idx2 = y
        
        term1 = (a1 - 1) * (a2 * k - b2) - b1 * (a2 - 1)
        term2 = (a2 - 1) * (a1 * k - b1) - b2 * (a1 - 1)
        
        if term1 < term2:
            return -1
        elif term1 > term2:
            return 1
        else:
            return 0
    
    sorted_buildings = sorted(buildings, key=lambda x: (-((x[0] - 1) * (k) - x[1]) / (x[0] - 1) if x[0] != 1 else float('inf')))
    
    for building in sorted_buildings:
        print(building[2])

if __name__ == "__main__":
    main()
