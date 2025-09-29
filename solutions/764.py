
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def main():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        points = []
        for _ in range(n):
            x, y = map(int, f.readline().split())
            points.append((x, y))
    
    if n == 0:
        print(0)
        return
        
    max_count = 0
    
    for i in range(n):
        x1, y1 = points[i]
        g = gcd(x1, y1)
        if g == 0:
            continue
        dx = x1 // g
        dy = y1 // g
        
        count = 0
        for j in range(n):
            x2, y2 = points[j]
            if x2 * dy == y2 * dx:
                count += 1
                
        max_count = max(max_count, count)
    
    print(max_count)

if __name__ == "__main__":
    main()
