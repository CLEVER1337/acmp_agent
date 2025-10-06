
import sys
import math

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    points = []
    for i in range(1, n+1):
        x, y = map(int, data[i].split())
        points.append((x, y, i))
    
    if n == 2:
        print(f"{points[0][2]}")
        print(f"{points[1][2]}")
        return
        
    def find_circle(p1, p2, p3):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        x3, y3 = p3[0], p3[1]
        
        A = x2 - x1
        B = y2 - y1
        C = x3 - x1
        D = y3 - y1
        
        E = A*(x1 + x2) + B*(y1 + y2)
        F = C*(x1 + x3) + D*(y1 + y3)
        G = 2*(A*(y3 - y1) - B*(x3 - x1))
        
        if abs(G) < 1e-12:
            return None
            
        cx = (D*E - B*F) / G
        cy = (A*F - C*E) / G
        r = math.sqrt((x1 - cx)**2 + (y1 - cy)**2)
        
        return (cx, cy, r)
    
    def point_on_circle(cx, cy, r, point, tol=1e-9):
        x, y = point[0], point[1]
        dist = math.sqrt((x - cx)**2 + (y - cy)**2)
        return abs(dist - r) < tol
    
    for i in range(min(10, n)):
        for j in range(i+1, min(i+10, n)):
            for k in range(j+1, min(j+10, n)):
                circle = find_circle(points[i], points[j], points[k])
                if circle is None:
                    continue
                    
                cx, cy, r = circle
                circle1_points = []
                circle2_points = []
                
                for idx, p in enumerate(points):
                    if point_on_circle(cx, cy, r, p):
                        circle1_points.append(p[2])
                    else:
                        circle2_points.append(p[2])
                
                if len(circle1_points) > 0 and len(circle2_points) > 0:
                    print(" ".join(map(str, circle1_points)))
                    print(" ".join(map(str, circle2_points)))
                    return
                    
    circle1_points = [points[0][2]]
    circle2_points = [p[2] for p in points[1:]]
    print(" ".join(map(str, circle1_points)))
    print(" ".join(map(str, circle2_points)))

if __name__ == "__main__":
    main()
