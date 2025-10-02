
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    points = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        points.append((x, y))
    
    area = 0
    boundary_points = 0
    
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        
        area += (x1 * y2 - x2 * y1)
        
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        
        if dx == 0 and dy == 0:
            continue
            
        gcd_val = gcd(dx, dy)
        boundary_points += gcd_val
    
    area = abs(area) // 2
    
    interior_points = area - boundary_points // 2 + 1
    
    print(interior_points)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    main()
