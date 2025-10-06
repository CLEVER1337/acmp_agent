
import sys
from math import gcd

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        points.append((x, y))
    
    total = 0
    for i in range(n):
        vectors = []
        for j in range(n):
            if i == j:
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            g = gcd(dx, dy)
            if g == 0:
                continue
            dx //= g
            dy //= g
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
            vectors.append((dx, dy))
        
        vectors.sort()
        count = 1
        for k in range(1, len(vectors)):
            if vectors[k] == vectors[k-1]:
                count += 1
            else:
                total += count * (count - 1) // 2
                count = 1
        total += count * (count - 1) // 2
    
    print(total)

if __name__ == "__main__":
    main()
