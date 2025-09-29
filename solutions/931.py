
import sys
import math

def readints():
    return list(map(int, sys.stdin.read().split()))

def find_circles(points):
    n = len(points)
    if n <= 2:
        return [list(range(1, n+1))], []
    
    def circle_from_3_points(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        
        A = x1*(y2-y3) - y1*(x2-x3) + x2*y3 - x3*y2
        B = (x1*x1 + y1*y1)*(y3-y2) + (x2*x2 + y2*y2)*(y1-y3) + (x3*x3 + y3*y3)*(y2-y1)
        C = (x1*x1 + y1*y1)*(x2-x3) + (x2*x2 + y2*y2)*(x3-x1) + (x3*x3 + y3*y3)*(x1-x2)
        D = (x1*x1 + y1*y1)*(x3*y2 - x2*y3) + (x2*x2 + y2*y2)*(x1*y3 - x3*y1) + (x3*x3 + y3*y3)*(x2*y1 - x1*y2)
        
        if abs(A) < 1e-12:
            return None
            
        cx = -B/(2*A)
        cy = -C/(2*A)
        r = math.sqrt((cx-x1)**2 + (cy-y1)**2)
        
        return (cx, cy, r)
    
    def point_on_circle(point, circle, tol=1e-6):
        if circle is None:
            return False
        cx, cy, r = circle
        x, y = point
        dist = math.sqrt((x-cx)**2 + (y-cy)**2)
        return abs(dist - r) < tol
    
    for i in range(min(50, n)):
        for j in range(i+1, min(50, n)):
            for k in range(j+1, min(50, n)):
                circle1 = circle_from_3_points(points[i], points[j], points[k])
                if circle1 is None:
                    continue
                
                circle1_points = []
                circle2_points = []
                
                for idx, point in enumerate(points):
                    if point_on_circle(point, circle1):
                        circle1_points.append(idx+1)
                    else:
                        circle2_points.append(idx+1)
                
                if len(circle2_points) == 0:
                    continue
                
                if len(circle2_points) == 1:
                    continue
                
                if len(set(circle2_points)) < len(circle2_points):
                    continue
                
                circle2_candidates = []
                for a in range(len(circle2_points)):
                    for b in range(a+1, len(circle2_points)):
                        for c in range(b+1, len(circle2_points)):
                            idx_a = circle2_points[a]-1
                            idx_b = circle2_points[b]-1
                            idx_c = circle2_points[c]-1
                            circle2 = circle_from_3_points(points[idx_a], points[idx_b], points[idx_c])
                            if circle2 is not None:
                                circle2_candidates.append(circle2)
                
                if not circle2_candidates:
                    continue
                
                circle2_found = False
                for circle2 in circle2_candidates:
                    valid = True
                    for idx in circle2_points:
                        if not point_on_circle(points[idx-1], circle2):
                            valid = False
                            break
                    if valid:
                        circle2_found = True
                        break
                
                if circle2_found:
                    return circle1_points, circle2_points
    
    return list(range(1, n//2+1)), list(range(n//2+1, n+1))

def main():
    data = readints()
    n = data[0]
    points = []
    index = 1
    for i in range(n):
        x = data[index]
        y = data[index+1]
        index += 2
        points.append((x, y))
    
    circle1, circle2 = find_circles(points)
    
    print(' '.join(map(str, circle1)))
    print(' '.join(map(str, circle2)))

if __name__ == '__main__':
    main()
