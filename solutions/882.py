
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, k = map(int, data[0].split())
    buildings = []
    for i in range(1, n + 1):
        parts = data[i].split()
        a = float(parts[0])
        b = int(parts[1])
        buildings.append((a, b, i))
    
    def compare(x, y):
        a1, b1, idx1 = x
        a2, b2, idx2 = y
        
        term1 = (a1 - 1) * (k * (a2 - 1) - b2)
        term2 = (a2 - 1) * (k * (a1 - 1) - b1)
        
        if abs(term1 - term2) < 1e-9:
            return idx1 - idx2
        return -1 if term1 > term2 else 1
    
    sorted_buildings = sorted(buildings, key=lambda x: (
        -((x[0] - 1) * (k * (x[0] - 1) - x[1])),
        x[2]
    ))
    
    for building in sorted_buildings:
        print(building[2])

if __name__ == "__main__":
    main()
