
import math

def read_points():
    points = []
    for _ in range(4):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def circumcircle_center(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    
    d = 2*(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
    if abs(d) < 1e-10:
        return None
        
    ux = ((ax*ax + ay*ay)*(by-cy) + (bx*bx + by*by)*(cy-ay) + (cx*cx + cy*cy)*(ay-by)) / d
    uy = ((ax*ax + ay*ay)*(cx-bx) + (bx*bx + by*by)*(ax-cx) + (cx*cx + cy*cy)*(bx-ax)) / d
    
    return (ux, uy)

def check_circle(center, points, r_sq):
    if center is None:
        return False
        
    cx, cy = center
    distances = []
    for p in points:
        dx = p[0] - cx
        dy = p[1] - cy
        dist_sq = dx*dx + dy*dy
        distances.append(dist_sq)
    
    ref = distances[0]
    for d in distances[1:]:
        if abs(d - ref) > 1e-10:
            return False
            
    actual_r_sq = ref - r_sq
    if abs(actual_r_sq) < 1e-10:
        return True
    return False

def solve():
    points = read_points()
    
    solutions = set()
    min_length_circle = None
    min_radius_sq = float('inf')
    
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                center = circumcircle_center(points[i], points[j], points[k])
                if center is None:
                    continue
                    
                cx, cy = center
                r_sq = distance(center, points[i])**2
                
                if check_circle(center, points, r_sq):
                    key = (round(cx, 10), round(cy, 10), round(r_sq, 10))
                    solutions.add(key)
                    
                    if r_sq < min_radius_sq:
                        min_radius_sq = r_sq
                        min_length_circle = (cx, cy, math.sqrt(r_sq))
    
    if len(solutions) == 0:
        for i in range(4):
            for j in range(i+1, 4):
                p1, p2 = points[i], points[j]
                mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
                
                valid = True
                distances = []
                for p in points:
                    dx = p[0] - mid[0]
                    dy = p[1] - mid[1]
                    dist_sq = dx*dx + dy*dy
                    distances.append(dist_sq)
                
                ref = distances[0]
                for d in distances[1:]:
                    if abs(d - ref) > 1e-10:
                        valid = False
                        break
                
                if valid:
                    r_sq = ref
                    key = (round(mid[0], 10), round(mid[1], 10), round(r_sq, 10))
                    solutions.add(key)
                    
                    if r_sq < min_radius_sq:
                        min_radius_sq = r_sq
                        min_length_circle = (mid[0], mid[1], math.sqrt(r_sq))
    
    if len(solutions) > 100:
        print("Infinity")
    else:
        print(len(solutions))
    
    if min_length_circle:
        cx, cy, r = min_length_circle
        print(f"{cx:.10f} {cy:.10f} {r:.10f}")
    else:
        print("0.000000 0.000000 0.000000")

solve()
