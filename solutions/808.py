
import math

def readints():
    return list(map(int, input().split()))

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]

def subtract(a, b):
    return (a[0]-b[0], a[1]-b[1])

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def multiply(v, k):
    return (v[0]*k, v[1]*k)

def length(v):
    return math.sqrt(v[0]*v[0] + v[1]*v[1])

def distance_point_to_segment(p, a, b):
    ab = subtract(b, a)
    ap = subtract(p, a)
    bp = subtract(p, b)
    
    if dot(ap, ab) <= 0:
        return length(ap)
    if dot(bp, ab) >= 0:
        return length(bp)
    
    return abs(cross(ab, ap)) / length(ab)

def segments_distance(a1, a2, b1, b2):
    d1 = distance_point_to_segment(a1, b1, b2)
    d2 = distance_point_to_segment(a2, b1, b2)
    d3 = distance_point_to_segment(b1, a1, a2)
    d4 = distance_point_to_segment(b2, a1, a2)
    return min(d1, d2, d3, d4)

def solve():
    data = readints()
    x1, y1, x2, y2, x3, y3, x4, y4, v1x, v1y, v2x, v2y = data
    
    a1 = (x1, y1)
    a2 = (x2, y2)
    b1 = (x3, y3)
    b2 = (x4, y4)
    v1 = (v1x, v1y)
    v2 = (v2x, v2y)
    v_rel = subtract(v1, v2)
    
    if length(v_rel) < 1e-12:
        initial_dist = segments_distance(a1, a2, b1, b2)
        if initial_dist < 1e-12:
            print(0.0)
        else:
            print(-1)
        return
    
    def f(t):
        new_a1 = add(a1, multiply(v1, t))
        new_a2 = add(a2, multiply(v1, t))
        new_b1 = add(b1, multiply(v2, t))
        new_b2 = add(b2, multiply(v2, t))
        return segments_distance(new_a1, new_a2, new_b1, new_b2)
    
    left, right = 0.0, 1e8
    for _ in range(100):
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if f(mid1) < f(mid2):
            right = mid2
        else:
            left = mid1
    
    min_t = (left + right) / 2
    min_dist = f(min_t)
    
    if min_dist < 1e-8:
        low, high = 0.0, min_t
        for _ in range(100):
            mid = (low + high) / 2
            if f(mid) <= 1e-8:
                high = mid
            else:
                low = mid
        print("{:.10f}".format((low + high) / 2))
    else:
        print(-1)

solve()
