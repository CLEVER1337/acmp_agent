
import sys
import math

def read_input():
    data = sys.stdin.read().split()
    if not data:
        return None, None, []
    
    R = float(data[0])
    K = int(data[1])
    points = []
    index = 2
    for _ in range(K):
        x1, y1, x2, y2 = map(float, data[index:index+4])
        index += 4
        points.append(((x1, y1), (x2, y2)))
    return R, K, points

def on_circle(x, y, R):
    return abs(x*x + y*y - R*R) < 1e-9

def normalize_angle(angle):
    while angle < 0:
        angle += 2 * math.pi
    while angle >= 2 * math.pi:
        angle -= 2 * math.pi
    return angle

def main():
    R, K, points = read_input()
    if R is None:
        print(0)
        return
    
    angles = set()
    for (p1, p2) in points:
        x1, y1 = p1
        x2, y2 = p2
        
        if not (on_circle(x1, y1, R) and on_circle(x2, y2, R)):
            continue
            
        angle1 = math.atan2(y1, x1)
        angle2 = math.atan2(y2, x2)
        
        if angle1 > angle2:
            angle1, angle2 = angle2, angle1
            
        if angle2 - angle1 > math.pi:
            angles.add((angle2, 2*math.pi))
            angles.add((0, angle1))
        else:
            angles.add((angle1, angle2))
    
    sorted_angles = sorted(angles)
    merged = []
    for start, end in sorted_angles:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    cuts = len(merged)
    parts = cuts + 1
    print(parts)

if __name__ == "__main__":
    main()
