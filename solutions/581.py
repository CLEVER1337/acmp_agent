
import math

def read_input():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline().strip())
        line = list(map(int, f.readline().split()))
        xp1, yp1, xp2, yp2 = line
        plates = []
        for i in range(n):
            data = list(map(int, f.readline().split()))
            plates.append((data[0], data[1], data[2], i + 1))
        return n, (xp1, yp1), (xp2, yp2), plates

def distance_point_to_line(px, py, x1, y1, x2, y2):
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    
    numerator = abs(A * px + B * py + C)
    denominator = math.sqrt(A * A + B * B)
    
    if denominator == 0:
        return math.sqrt((px - x1)**2 + (py - y1)**2)
    
    return numerator / denominator

def point_on_segment(px, py, x1, y1, x2, y2):
    cross = (px - x1) * (y2 - y1) - (py - y1) * (x2 - x1)
    if abs(cross) > 1e-10:
        return False
    
    dot1 = (px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)
    dot2 = (px - x2) * (x1 - x2) + (py - y2) * (y1 - y2)
    
    return dot1 >= 0 and dot2 >= 0

def main():
    n, p1, p2, plates = read_input()
    x1, y1 = p1
    x2, y2 = p2
    
    destroyed = []
    
    for x, y, r, idx in plates:
        dist = distance_point_to_line(x, y, x1, y1, x2, y2)
        
        if dist <= r:
            destroyed.append(idx)
        else:
            d1 = math.sqrt((x - x1)**2 + (y - y1)**2)
            d2 = math.sqrt((x - x2)**2 + (y - y2)**2)
            
            if d1 <= r or d2 <= r:
                destroyed.append(idx)
            else:
                dx = x2 - x1
                dy = y2 - y1
                
                t = ((x - x1) * dx + (y - y1) * dy) / (dx*dx + dy*dy)
                
                if 0 <= t <= 1:
                    proj_x = x1 + t * dx
                    proj_y = y1 + t * dy
                    dist_to_proj = math.sqrt((x - proj_x)**2 + (y - proj_y)**2)
                    if dist_to_proj <= r:
                        destroyed.append(idx)
    
    destroyed.sort()
    
    with open('OUTPUT.TXT', 'w') as f:
        f.write(f"{len(destroyed)}\n")
        if destroyed:
            f.write(" ".join(map(str, destroyed)))
        else:
            f.write("")

if __name__ == "__main__":
    main()
