
import math

def read_points():
    points = []
    for _ in range(4):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def circle_from_three_points(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    
    E = A*(x1 + x2) + B*(y1 + y2)
    F = C*(x1 + x3) + D*(y1 + y3)
    
    G = 2*(A*(y3 - y1) - B*(x3 - x1))
    
    if abs(G) < 1e-10:
        return None
    
    cx = (D*E - B*F) / G
    cy = (A*F - C*E) / G
    
    r = distance((cx, cy), p1)
    return (cx, cy, r)

def are_points_cocircular(points):
    p1, p2, p3, p4 = points
    circle = circle_from_three_points(p1, p2, p3)
    if circle is None:
        return False
    cx, cy, r = circle
    return abs(distance((cx, cy), p4) - r) < 1e-10

def solve():
    points = read_points()
    
    if are_points_cocircular(points):
        print("Infinity")
        p1, p2, p3, p4 = points
        circle = circle_from_three_points(p1, p2, p3)
        cx, cy, r = circle
        print(f"{cx:.10f} {cy:.10f} {r:.10f}")
        return
    
    solutions = set()
    min_circle = None
    min_radius = float('inf')
    
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                circle = circle_from_three_points(points[i], points[j], points[k])
                if circle is None:
                    continue
                
                cx, cy, r = circle
                distances = [abs(distance((cx, cy), p) - r) for p in points]
                
                if all(abs(d) < 1e-10 for d in distances):
                    solutions.add((round(cx, 8), round(cy, 8), round(r, 8)))
                    if r < min_radius:
                        min_radius = r
                        min_circle = (cx, cy, r)
    
    for i in range(4):
        for j in range(i+1, 4):
            p1, p2 = points[i], points[j]
            mid = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
            
            for k in range(4):
                if k == i or k == j:
                    continue
                
                p3 = points[k]
                dx, dy = p2[0] - p1[0], p2[1] - p1[1]
                if abs(dx) < 1e-10 and abs(dy) < 1e-10:
                    continue
                
                normal = (-dy, dx)
                normal_len = math.sqrt(normal[0]**2 + normal[1]**2)
                normal = (normal[0]/normal_len, normal[1]/normal_len)
                
                d1 = distance(mid, p1)
                d2 = distance(mid, p3)
                
                if abs(d2 - d1) < 1e-10:
                    cx, cy = mid
                    r = d1
                    distances = [abs(distance((cx, cy), p) - r) for p in points]
                    if all(abs(d) < 1e-10 for d in distances):
                        solutions.add((round(cx, 8), round(cy, 8), round(r, 8)))
                        if r < min_radius:
                            min_radius = r
                            min_circle = (cx, cy, r)
    
    print(len(solutions))
    if min_circle:
        cx, cy, r = min_circle
        print(f"{cx:.10f} {cy:.10f} {r:.10f}")

if __name__ == "__main__":
    solve()
