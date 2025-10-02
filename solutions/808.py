
import math

def read_input():
    with open('INPUT.TXT', 'r') as f:
        data = list(map(float, f.read().split()))
    return data

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]

def subtract(a, b):
    return (a[0]-b[0], a[1]-b[1])

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def multiply(v, t):
    return (v[0]*t, v[1]*t)

def segments_intersect(a, b, c, d):
    def orientation(p, q, r):
        val = (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
        if val == 0: return 0
        return 1 if val > 0 else 2
    
    def on_segment(p, q, r):
        return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and 
                min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))
    
    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)
    
    if o1 != o2 and o3 != o4:
        return True
    
    if o1 == 0 and on_segment(a, c, b): return True
    if o2 == 0 and on_segment(a, d, b): return True
    if o3 == 0 and on_segment(c, a, d): return True
    if o4 == 0 and on_segment(c, b, d): return True
    
    return False

def point_to_segment_distance(p, a, b):
    ab = subtract(b, a)
    ap = subtract(p, a)
    bp = subtract(p, b)
    
    if dot(ap, ab) <= 0:
        return math.sqrt(ap[0]**2 + ap[1]**2)
    
    if dot(bp, ab) >= 0:
        return math.sqrt(bp[0]**2 + bp[1]**2)
    
    return abs(cross(ab, ap)) / math.sqrt(ab[0]**2 + ab[1]**2)

def solve():
    data = read_input()
    x1, y1, x2, y2 = data[0], data[1], data[2], data[3]
    x3, y3, x4, y4 = data[4], data[5], data[6], data[7]
    v1x, v1y, v2x, v2y = data[8], data[9], data[10], data[11]
    
    A = (x1, y1)
    B = (x2, y2)
    C = (x3, y3)
    D = (x4, y4)
    v1 = (v1x, v1y)
    v2 = (v2x, v2y)
    v_rel = subtract(v1, v2)
    
    def f(t):
        if t < 0:
            return float('inf')
        A_t = add(A, multiply(v1, t))
        B_t = add(B, multiply(v1, t))
        C_t = add(C, multiply(v2, t))
        D_t = add(D, multiply(v2, t))
        return segments_intersect(A_t, B_t, C_t, D_t)
    
    left, right = 0.0, 1e6
    best_t = float('inf')
    
    for _ in range(100):
        mid = (left + right) / 2
        if f(mid):
            right = mid
            best_t = min(best_t, mid)
        else:
            left = mid
    
    if best_t == float('inf'):
        left, right = 0.0, 1e6
        best_t = float('inf')
        
        def distance_at_time(t):
            if t < 0:
                return float('inf')
            A_t = add(A, multiply(v1, t))
            B_t = add(B, multiply(v1, t))
            C_t = add(C, multiply(v2, t))
            D_t = add(D, multiply(v2, t))
            
            d1 = point_to_segment_distance(A_t, C_t, D_t)
            d2 = point_to_segment_distance(B_t, C_t, D_t)
            d3 = point_to_segment_distance(C_t, A_t, B_t)
            d4 = point_to_segment_distance(D_t, A_t, B_t)
            return min(d1, d2, d3, d4)
        
        def derivative(t):
            h = 1e-8
            return (distance_at_time(t+h) - distance_at_time(t)) / h
        
        t = 0.0
        learning_rate = 1e-3
        for _ in range(100000):
            grad = derivative(t)
            t_new = t - learning_rate * grad
            if t_new < 0:
                t_new = 0
            t = t_new
            
        if distance_at_time(t) < 1e-8:
            best_t = t
    
    if best_t == float('inf'):
        result = -1
    else:
        result = best_t
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{result:.10f}")

if __name__ == "__main__":
    solve()
