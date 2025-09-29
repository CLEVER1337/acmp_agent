
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def point_on_segment(p, a, b):
    if abs((b[0]-a[0])*(p[1]-a[1]) - (p[0]-a[0])*(b[1]-a[1])) > 1e-9:
        return False
    if min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]):
        return True
    return False

def segments_intersect(a1, a2, b1, b2):
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    
    def sign(x):
        return 1 if x > 1e-9 else -1 if x < -1e-9 else 0
    
    c1 = cross(a1, a2, b1)
    c2 = cross(a1, a2, b2)
    c3 = cross(b1, b2, a1)
    c4 = cross(b1, b2, a2)
    
    if sign(c1)*sign(c2) < 0 and sign(c3)*sign(c4) < 0:
        return True
    
    if abs(c1) < 1e-9 and point_on_segment(b1, a1, a2):
        return True
    if abs(c2) < 1e-9 and point_on_segment(b2, a1, a2):
        return True
    if abs(c3) < 1e-9 and point_on_segment(a1, b1, b2):
        return True
    if abs(c4) < 1e-9 and point_on_segment(a2, b1, b2):
        return True
    
    return False

def point_in_rect(p, rect):
    x1, y1, x2, y2 = rect
    return x1 <= p[0] <= x2 and y1 <= p[1] <= y2

def line_intersects_obstacle(a, b, obstacles):
    for rect in obstacles:
        x1, y1, x2, y2 = rect
        corners = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
        edges = [(corners[0], corners[1]), (corners[1], corners[2]), 
                (corners[2], corners[3]), (corners[3], corners[0])]
        
        for edge in edges:
            if segments_intersect(a, b, edge[0], edge[1]):
                return True
    return False

def can_see(a, b, obstacles):
    return not line_intersects_obstacle(a, b, obstacles)

def find_viewpoint(m, l, obstacles):
    if can_see(m, l, obstacles):
        return (m[0], m[1])
    
    for rect in obstacles:
        x1, y1, x2, y2 = rect
        corners = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
        
        for corner in corners:
            if not any(point_in_rect(corner, other_rect) for other_rect in obstacles if other_rect != rect):
                if can_see(m, corner, obstacles) and can_see(l, corner, obstacles):
                    return corner
    
    for rect1 in obstacles:
        for rect2 in obstacles:
            if rect1 == rect2:
                continue
            x11, y11, x12, y12 = rect1
            x21, y21, x22, y22 = rect2
            
            if x12 == x21 and max(y11, y21) <= min(y12, y22):
                y_low = max(y11, y21)
                y_high = min(y12, y22)
                if y_low <= y_high:
                    for y in [y_low, y_high]:
                        p = (x12, y)
                        if can_see(m, p, obstacles) and can_see(l, p, obstacles):
                            return p
            
            if y12 == y21 and max(x11, x21) <= min(x12, x22):
                x_low = max(x11, x21)
                x_high = min(x12, x22)
                if x_low <= x_high:
                    for x in [x_low, x_high]:
                        p = (x, y12)
                        if can_see(m, p, obstacles) and can_see(l, p, obstacles):
                            return p
    
    return None

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("NO")
        return
        
    m = tuple(map(int, data[0].split()))
    l = tuple(map(int, data[1].split()))
    n = int(data[2])
    obstacles = []
    for i in range(3, 3 + n):
        parts = list(map(int, data[i].split()))
        obstacles.append(parts)
    
    viewpoint = find_viewpoint(m, l, obstacles)
    
    if viewpoint is not None:
        print("YES")
        print(f"{viewpoint[0]:.6f} {viewpoint[1]:.6f}")
    else:
        print("NO")

if __name__ == "__main__":
    main()
