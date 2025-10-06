
import sys
import math

def readints():
    return list(map(int, sys.stdin.readline().split()))

def dot(v, w):
    return v[0]*w[0] + v[1]*w[1]

def length(v):
    return math.sqrt(v[0]**2 + v[1]**2)

def normalize(v):
    l = length(v)
    return (v[0]/l, v[1]/l)

def dist_point_to_segment(p, a, b):
    ab = (b[0]-a[0], b[1]-a[1])
    ap = (p[0]-a[0], p[1]-a[1])
    if dot(ab, ap) <= 0:
        return length(ap)
    bp = (p[0]-b[0], p[1]-b[1])
    if dot(ab, bp) >= 0:
        return length(bp)
    n_ab = normalize(ab)
    projection = dot(ap, n_ab)
    closest = (a[0] + n_ab[0]*projection, a[1] + n_ab[1]*projection)
    return math.sqrt((p[0]-closest[0])**2 + (p[1]-closest[1])**2)

def find_circle_for_segments(a1, a2, b1, b2):
    left = -1e5
    right = 1e5
    for _ in range(100):
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        
        p1 = (mid1, 0)
        d1a = dist_point_to_segment(p1, a1, a2)
        d1b = dist_point_to_segment(p1, b1, b2)
        f1 = abs(d1a - d1b)
        
        p2 = (mid2, 0)
        d2a = dist_point_to_segment(p2, a1, a2)
        d2b = dist_point_to_segment(p2, b1, b2)
        f2 = abs(d2a - d2b)
        
        if f1 < f2:
            right = mid2
        else:
            left = mid1
    
    best_x = (left + right) / 2
    center = (best_x, 0)
    r1 = dist_point_to_segment(center, a1, a2)
    r2 = dist_point_to_segment(center, b1, b2)
    radius = (r1 + r2) / 2
    return center[0], center[1], radius

def main():
    data = sys.stdin.read().splitlines()
    index = 0
    output_lines = []
    while True:
        line1 = data[index].strip()
        line2 = data[index+1].strip()
        if line1 == '0 0 0 0' and line2 == '0 0 0 0':
            break
        coords1 = list(map(int, line1.split()))
        coords2 = list(map(int, line2.split()))
        a1 = (coords1[0], coords1[1])
        a2 = (coords1[2], coords1[3])
        b1 = (coords2[0], coords2[1])
        b2 = (coords2[2], coords2[3])
        
        cx, cy, r = find_circle_for_segments(a1, a2, b1, b2)
        output_lines.append(f"{cx:.6f} {cy:.6f} {r:.6f}")
        index += 2
    
    print("\n".join(output_lines))

if __name__ == "__main__":
    main()
