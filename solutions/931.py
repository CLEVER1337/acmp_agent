
import sys
import math

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    points = []
    for i in range(n):
        x = int(data[1 + 2*i])
        y = int(data[2 + 2*i])
        points.append((x, y))
    
    if n == 2:
        print("1")
        print("2")
        return
    
    p0 = points[0]
    p1 = points[1]
    
    circle1 = [1]
    circle2 = []
    
    for i in range(2, n):
        x0, y0 = p0
        x1, y1 = p1
        x2, y2 = points[i]
        
        A = x1 - x0
        B = y1 - y0
        C = x2 - x0
        D = y2 - y0
        
        det = A * D - B * C
        if abs(det) > 1e-9:
            circle2.append(i+1)
        else:
            circle1.append(i+1)
    
    if not circle2:
        circle2.append(2)
    else:
        circle1.append(2)
    
    print(" ".join(map(str, circle1)))
    print(" ".join(map(str, circle2)))

if __name__ == "__main__":
    main()
