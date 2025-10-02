
import math

def main():
    with open('INPUT.TXT', 'r') as f:
        data = f.read().split()
    
    n = int(data[0])
    phi0 = float(data[1])
    alpha = math.radians(phi0)
    
    buildings = []
    index = 2
    for i in range(n):
        x1 = float(data[index])
        y1 = float(data[index+1])
        x2 = float(data[index+2])
        y2 = float(data[index+3])
        h = float(data[index+4])
        index += 5
        buildings.append((x1, y1, x2, y2, h))
    
    corners = []
    for b in buildings:
        x1, y1, x2, y2, h = b
        corners.extend([(x1, y1, h), (x1, y2, h), (x2, y1, h), (x2, y2, h)])
    
    def is_covered(H, gx, gy):
        for cx, cy, ch in corners:
            dx = cx - gx
            dy = cy - gy
            dz = ch - H
            if dz > 0:
                return False
            dist_xy = math.sqrt(dx*dx + dy*dy)
            if dist_xy == 0:
                if dz == 0:
                    angle = 0
                else:
                    angle = math.pi/2
            else:
                angle = math.atan2(-dz, dist_xy)
            if angle > alpha:
                return False
        return True
    
    def check_height(H):
        for b in buildings:
            x1, y1, x2, y2, h = b
            points = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            for px, py in points:
                if is_covered(H, px, py):
                    return True
        return False
    
    low = 0.0
    high = 10000.0
    for _ in range(100):
        mid = (low + high) / 2.0
        if check_height(mid):
            high = mid
        else:
            low = mid
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write("{:.10f}".format(high))

if __name__ == '__main__':
    main()
