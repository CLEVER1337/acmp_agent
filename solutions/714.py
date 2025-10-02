
import math

def read_points():
    points = []
    for _ in range(4):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def circle_from_three_points(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    
    E = A * (x1 + x2) + B * (y1 + y2)
    F = C * (x1 + x3) + D * (y1 + y3)
    
    G = 2 * (A * (y3 - y1) - C * (y2 - y1))
    
    if abs(G) < 1e-10:
        return None
    
    cx = (D * E - B * F) / G
    cy = (A * F - C * E) / G
    
    r = math.sqrt((x1 - cx)**2 + (y1 - cy)**2)
    
    return (cx, cy, r)

def point_to_circle_distance(point, circle):
    cx, cy, r = circle
    px, py = point
    distance = math.sqrt((px - cx)**2 + (py - cy)**2)
    return abs(distance - r)

def are_points_on_circle(points, circle, tolerance=1e-8):
    cx, cy, r = circle
    for point in points:
        px, py = point
        distance = math.sqrt((px - cx)**2 + (py - cy)**2)
        if abs(distance - r) > tolerance:
            return False
    return True

def are_points_concyclic(points):
    p1, p2, p3, p4 = points
    
    circle1 = circle_from_three_points(p1, p2, p3)
    if circle1 is None:
        return False
    
    return are_points_on_circle([p4], circle1)

def solve():
    points = read_points()
    
    if are_points_concyclic(points):
        print("Infinity")
        circle = circle_from_three_points(points[0], points[1], points[2])
        print(f"{circle[0]:.10f} {circle[1]:.10f} {circle[2]:.10f}")
        return
    
    min_length = float('inf')
    best_circle = None
    count = 0
    
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                circle = circle_from_three_points(points[i], points[j], points[k])
                if circle is None:
                    continue
                
                cx, cy, r = circle
                
                distances = []
                for l in range(4):
                    dist = point_to_circle_distance(points[l], circle)
                    distances.append(dist)
                
                if max(distances) - min(distances) < 1e-8:
                    count += 1
                    if r < min_length:
                        min_length = r
                        best_circle = circle
    
    print(count)
    if best_circle:
        print(f"{best_circle[0]:.10f} {best_circle[1]:.10f} {best_circle[2]:.10f}")

if __name__ == "__main__":
    solve()
