
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def solve():
    data = sys.stdin.read().splitlines()
    index = 0
    output_lines = []
    while index < len(data):
        line1 = data[index].strip()
        if not line1:
            index += 1
            continue
        if line1 == '0 0 0 0':
            break
        line2 = data[index+1].strip()
        if line2 == '0 0 0 0':
            break
            
        x1, y1, x2, y2 = map(int, line1.split())
        x3, y3, x4, y4 = map(int, line2.split())
        index += 2
        
        seg1 = ((x1, y1), (x2, y2))
        seg2 = ((x3, y3), (x4, y4))
        
        p1, p2 = seg1
        p3, p4 = seg2
        
        if cross(p1, p2, p3) * cross(p1, p2, p4) > 0:
            a = p2[1] - p1[1]
            b = p1[0] - p2[0]
            c = p1[1]*p2[0] - p1[0]*p2[1]
            output_lines.append(f"{a} {b} {c}")
            continue
            
        if cross(p3, p4, p1) * cross(p3, p4, p2) > 0:
            a = p4[1] - p3[1]
            b = p3[0] - p4[0]
            c = p3[1]*p4[0] - p3[0]*p4[1]
            output_lines.append(f"{a} {b} {c}")
            continue
            
        mid1 = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        mid2 = ((p3[0] + p4[0])/2, (p3[1] + p4[1])/2)
        
        dx = mid2[0] - mid1[0]
        dy = mid2[1] - mid1[1]
        
        if abs(dx) < 1e-9 and abs(dy) < 1e-9:
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            a = -dy
            b = dx
            c = -(a*mid1[0] + b*mid1[1])
        else:
            a = -dy
            b = dx
            c = -(a*mid1[0] + b*mid1[1])
            
        a_int = round(a * 2)
        b_int = round(b * 2)
        c_int = round(c * 2)
        
        g = abs(__gcd(__gcd(a_int, b_int), c_int))
        if g != 0:
            a_int //= g
            b_int //= g
            c_int //= g
        
        if a_int < 0 or (a_int == 0 and b_int < 0):
            a_int = -a_int
            b_int = -b_int
            c_int = -c_int
            
        output_lines.append(f"{a_int} {b_int} {c_int}")
    
    print("\n".join(output_lines))

def __gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

solve()
