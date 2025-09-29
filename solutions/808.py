
import math

def read_input():
    with open('INPUT.TXT', 'r') as f:
        data = list(map(float, f.readline().split()))
    return data

def write_output(result):
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{result:.10f}")

def point_on_segment(px, py, x1, y1, x2, y2):
    if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
        cross = (px - x1) * (y2 - y1) - (py - y1) * (x2 - x1)
        if abs(cross) < 1e-9:
            return True
    return False

def segments_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    def orientation(ax, ay, bx, by, cx, cy):
        val = (by - ay) * (cx - bx) - (bx - ax) * (cy - by)
        if abs(val) < 1e-9:
            return 0
        return 1 if val > 0 else 2

    o1 = orientation(x1, y1, x2, y2, x3, y3)
    o2 = orientation(x1, y1, x2, y2, x4, y4)
    o3 = orientation(x3, y3, x4, y4, x1, y1)
    o4 = orientation(x3, y3, x4, y4, x2, y2)
    
    if o1 != o2 and o3 != o4:
        return True
    
    if o1 == 0 and point_on_segment(x3, y3, x1, y1, x2, y2):
        return True
    if o2 == 0 and point_on_segment(x4, y4, x1, y1, x2, y2):
        return True
    if o3 == 0 and point_on_segment(x1, y1, x3, y3, x4, y4):
        return True
    if o4 == 0 and point_on_segment(x2, y2, x3, y3, x4, y4):
        return True
    
    return False

def distance_point_to_segment(px, py, x1, y1, x2, y2):
    l2 = (x2 - x1)**2 + (y2 - y1)**2
    if l2 == 0:
        return math.sqrt((px - x1)**2 + (py - y1)**2)
    
    t = max(0, min(1, ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / l2))
    proj_x = x1 + t * (x2 - x1)
    proj_y = y1 + t * (y2 - y1)
    return math.sqrt((px - proj_x)**2 + (py - proj_y)**2)

def distance_between_segments(x1, y1, x2, y2, x3, y3, x4, y4):
    if segments_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
        return 0.0
    
    d1 = min(distance_point_to_segment(x1, y1, x3, y3, x4, y4),
             distance_point_to_segment(x2, y2, x3, y3, x4, y4))
    d2 = min(distance_point_to_segment(x3, y3, x1, y1, x2, y2),
             distance_point_to_segment(x4, y4, x1, y1, x2, y2))
    return min(d1, d2)

def solve():
    data = read_input()
    x1, y1, x2, y2, x3, y3, x4, y4, v1x, v1y, v2x, v2y = data
    
    vx = v1x - v2x
    vy = v1y - v2y
    
    if vx == 0 and vy == 0:
        d0 = distance_between_segments(x1, y1, x2, y2, x3, y3, x4, y4)
        if d0 < 1e-9:
            return 0.0
        else:
            return -1.0
    
    def f(t):
        new_x1 = x1 + v1x * t
        new_y1 = y1 + v1y * t
        new_x2 = x2 + v1x * t
        new_y2 = y2 + v1y * t
        new_x3 = x3 + v2x * t
        new_y3 = y3 + v2y * t
        new_x4 = x4 + v2x * t
        new_y4 = y4 + v2y * t
        return distance_between_segments(new_x1, new_y1, new_x2, new_y2, new_x3, new_y3, new_x4, new_y4)
    
    left, right = 0.0, 1e9
    best_t = -1.0
    
    for _ in range(100):
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        f1 = f(mid1)
        f2 = f(mid2)
        
        if f1 < 1e-9:
            best_t = mid1
            right = mid1
        elif f2 < 1e-9:
            best_t = mid2
            left = mid2
        elif f1 < f2:
            right = mid2
        else:
            left = mid1
    
    if best_t != -1:
        return best_t
    
    left, right = 0.0, 1e9
    min_distance = f(0)
    
    if min_distance < 1e-9:
        return 0.0
    
    for _ in range(100):
        mid = (left + right) / 2
        if f(mid) < min_distance:
            left = mid
            min_distance = f(mid)
        else:
            right = mid
    
    if min_distance < 1e-9:
        return left
    
    return -1.0

result = solve()
write_output(result)
